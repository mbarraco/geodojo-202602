#!/usr/bin/env python3
"""
Migra archivos Markdown existentes a formato YAML.
Uso: python scripts/migrate_to_yaml.py
"""

import re
import yaml
from pathlib import Path
from typing import Optional


def represent_str(dumper, data):
    """Custom representer for multiline strings."""
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


yaml.add_representer(str, represent_str)


def parse_ejercicios_markdown(content: str) -> dict:
    """Parse an ejercicios markdown file into structured data."""
    lines = content.split('\n')
    
    data = {
        'unit': {},
        'categories': []
    }
    
    # Parse unit header
    for i, line in enumerate(lines):
        if line.startswith('# '):
            # Extract unit number and title
            match = re.match(r'# Unidad (\d+): (.+)', line)
            if match:
                data['unit']['number'] = int(match.group(1))
                data['unit']['title'] = match.group(2)
            else:
                # Fallback for different format
                data['unit']['title'] = line[2:].strip()
            
            # Next non-empty, non-separator line is description
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('---'):
                    data['unit']['description'] = lines[j].strip()
                    break
            break
    
    # Find all categories (## Categoría X)
    category_pattern = re.compile(r'^## Categoría ([ABC]) [-–] (.+)$')
    block_pattern = re.compile(r'^### Bloque (\d+): (.+)$')
    exercise_pattern = re.compile(r'^### ([ABC]\d+)\. (.+)$')
    
    current_category = None
    current_block = None
    current_exercise = None
    current_section = None  # 'enunciado', 'ejemplo', 'hint'
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for category
        cat_match = category_pattern.match(line)
        if cat_match:
            if current_category:
                # Save previous category
                if current_block and current_category.get('blocks'):
                    pass  # block already added
                data['categories'].append(current_category)
            
            current_category = {
                'id': cat_match.group(1),
                'title': cat_match.group(2),
            }
            
            # Get description (next non-empty, non-separator line)
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('---') and not lines[j].startswith('#'):
                    current_category['description'] = lines[j].strip()
                    break
            
            # Category A has blocks, B and C have direct exercises
            if cat_match.group(1) == 'A':
                current_category['blocks'] = []
            else:
                current_category['exercises'] = []
            
            current_block = None
            current_exercise = None
            i += 1
            continue
        
        # Check for block (only in category A)
        block_match = block_pattern.match(line)
        if block_match and current_category and current_category['id'] == 'A':
            if current_block:
                current_category['blocks'].append(current_block)
            
            current_block = {
                'name': block_match.group(2),
                'exercises': []
            }
            current_exercise = None
            i += 1
            continue
        
        # Check for exercise
        ex_match = exercise_pattern.match(line)
        if ex_match:
            # Save previous exercise
            if current_exercise:
                _save_exercise(current_exercise, current_category, current_block)
            
            current_exercise = {
                'id': ex_match.group(1),
                'title': ex_match.group(2),
                'enunciado': '',
                'ejemplo': {},
            }
            current_section = None
            i += 1
            continue
        
        # Parse exercise content
        if current_exercise:
            if line.startswith('**Enunciado**:'):
                current_section = 'enunciado'
                # Rest of line after ": " is the enunciado
                enunciado_start = line[len('**Enunciado**: '):]
                if enunciado_start:
                    current_exercise['enunciado'] = enunciado_start
                i += 1
                continue
            
            elif line.startswith('**Ejemplo**:'):
                current_section = 'ejemplo'
                i += 1
                continue
            
            elif line.startswith('**Hint**:'):
                hint_text = line[len('**Hint**: '):]
                if hint_text:
                    current_exercise['hint'] = hint_text
                current_section = 'hint'
                i += 1
                continue
            
            elif line.startswith('---'):
                # End of exercise, save it
                _save_exercise(current_exercise, current_category, current_block)
                current_exercise = None
                current_section = None
                i += 1
                continue
            
            # Continue current section
            if current_section == 'enunciado' and line.strip():
                if current_exercise['enunciado']:
                    current_exercise['enunciado'] += '\n' + line
                else:
                    current_exercise['enunciado'] = line
            
            elif current_section == 'ejemplo':
                _parse_ejemplo_line(line, current_exercise)
            
            elif current_section == 'hint' and line.strip():
                if 'hint' in current_exercise:
                    current_exercise['hint'] += '\n' + line.strip()
                else:
                    current_exercise['hint'] = line.strip()
        
        i += 1
    
    # Save last items
    if current_exercise:
        _save_exercise(current_exercise, current_category, current_block)
    
    if current_block and current_category and 'blocks' in current_category:
        current_category['blocks'].append(current_block)
    
    if current_category:
        data['categories'].append(current_category)
    
    return data


def _save_exercise(exercise: dict, category: dict, block: Optional[dict]):
    """Save exercise to the appropriate location."""
    # Clean up exercise
    if not exercise.get('enunciado'):
        exercise['enunciado'] = ''
    else:
        exercise['enunciado'] = exercise['enunciado'].strip()
    
    if not exercise.get('ejemplo'):
        del exercise['ejemplo']
    
    if 'hint' in exercise and not exercise['hint']:
        del exercise['hint']
    
    # Add to block or category
    if block is not None:
        block['exercises'].append(exercise)
    elif category and 'exercises' in category:
        category['exercises'].append(exercise)


def _parse_ejemplo_line(line: str, exercise: dict):
    """Parse a line in the ejemplo section."""
    line = line.strip()
    
    if line.startswith('- Entrada:'):
        entrada = line[len('- Entrada:'):].strip()
        # Remove backticks
        entrada = entrada.strip('`')
        exercise['ejemplo']['entrada'] = entrada
    
    elif line.startswith('- Salida esperada:'):
        salida = line[len('- Salida esperada:'):].strip()
        if salida:
            # Single line output
            salida = salida.strip('`')
            exercise['ejemplo']['salida'] = salida
        else:
            # Multi-line output follows
            exercise['ejemplo']['salida'] = ''
    
    elif line.startswith('```') and 'salida' in exercise['ejemplo']:
        # Start or end of code block in salida
        pass
    
    elif 'salida' in exercise['ejemplo'] and exercise['ejemplo']['salida'] == '':
        # Collecting multi-line salida
        if line and not line.startswith('```'):
            exercise['ejemplo']['salida'] = line
    
    elif 'salida' in exercise['ejemplo'] and line and not line.startswith('```'):
        # Continue multi-line salida
        exercise['ejemplo']['salida'] += '\n' + line


def parse_clase_markdown(content: str) -> dict:
    """Parse a clase markdown file into structured data."""
    lines = content.split('\n')
    
    data = {
        'unit': {},
        'temario': [],
        'ejemplos': [],
        'notas_docente': []
    }
    
    # Parse unit header
    for i, line in enumerate(lines):
        if line.startswith('# '):
            match = re.match(r'# Clase (\d+): (.+)', line)
            if match:
                data['unit']['number'] = int(match.group(1))
                data['unit']['title'] = match.group(2)
            else:
                data['unit']['title'] = line[2:].strip()
            
            # Next non-empty, non-separator line is description
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('---'):
                    data['unit']['description'] = lines[j].strip()
                    break
            break
    
    # Find sections
    current_section = None
    current_temario_item = None
    current_ejemplo = None
    in_solutions_section = False
    in_code_block = False
    code_block_content = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Track code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                in_code_block = False
                if current_ejemplo and 'code' not in current_ejemplo.get('solucion', {}):
                    if in_solutions_section:
                        if 'solucion' not in current_ejemplo:
                            current_ejemplo['solucion'] = {}
                        current_ejemplo['solucion']['code'] = '\n'.join(code_block_content)
                    code_block_content = []
            else:
                in_code_block = True
                code_block_content = []
            i += 1
            continue
        
        if in_code_block:
            code_block_content.append(line)
            i += 1
            continue
        
        # Section headers
        if line.startswith('## 1. Temario'):
            current_section = 'temario'
            i += 1
            continue
        
        if line.startswith('## 2. Ejemplos'):
            current_section = 'ejemplos'
            i += 1
            continue
        
        if line.startswith('### 2.1 Enunciados'):
            in_solutions_section = False
            i += 1
            continue
        
        if line.startswith('### 2.2 Enunciados + Soluciones'):
            in_solutions_section = True
            i += 1
            continue
        
        if line.startswith('## Notas para el docente'):
            current_section = 'notas'
            i += 1
            continue
        
        # Parse temario sections
        if current_section == 'temario':
            # Check for ### header (temario topic)
            match = re.match(r'^### \d+\.\d+ (.+)$', line)
            if match:
                if current_temario_item:
                    data['temario'].append(current_temario_item)
                current_temario_item = {
                    'title': match.group(1),
                    'rows': []
                }
                i += 1
                continue
            
            # Parse table
            if current_temario_item and line.startswith('|') and not line.startswith('|--'):
                cells = [c.strip() for c in line.split('|')[1:-1]]
                if len(cells) >= 2:
                    # Check if this is header row
                    if 'columns' not in current_temario_item:
                        current_temario_item['columns'] = cells
                    else:
                        current_temario_item['rows'].append(cells)
        
        # Parse ejemplos
        if current_section == 'ejemplos':
            # Check for ejemplo header
            match = re.match(r'^#### Ejemplo (\d+): (.+)$', line)
            if match:
                ejemplo_id = int(match.group(1))
                ejemplo_title = match.group(2)
                
                if in_solutions_section:
                    # Find existing ejemplo and add solution
                    for ej in data['ejemplos']:
                        if ej['id'] == ejemplo_id:
                            current_ejemplo = ej
                            break
                else:
                    # Create new ejemplo
                    if current_ejemplo and not in_solutions_section:
                        pass  # Already added
                    current_ejemplo = {
                        'id': ejemplo_id,
                        'title': ejemplo_title,
                        'enunciado': ''
                    }
                    data['ejemplos'].append(current_ejemplo)
                i += 1
                continue
            
            # Collect enunciado or solution content
            if current_ejemplo:
                if not in_solutions_section:
                    # Collecting enunciado
                    if line.strip() and not line.startswith('---'):
                        if current_ejemplo['enunciado']:
                            current_ejemplo['enunciado'] += '\n' + line
                        else:
                            current_ejemplo['enunciado'] = line
                else:
                    # In solutions section
                    if line.startswith('**Enunciado**:'):
                        # Skip, already have enunciado
                        pass
                    elif line.startswith('**Salida**:'):
                        # Next code block is salida
                        if 'solucion' not in current_ejemplo:
                            current_ejemplo['solucion'] = {}
                        # Collect salida from next code block
                        j = i + 1
                        while j < len(lines) and not lines[j].strip().startswith('```'):
                            j += 1
                        if j < len(lines):
                            j += 1  # Skip opening ```
                            salida_lines = []
                            while j < len(lines) and not lines[j].strip().startswith('```'):
                                salida_lines.append(lines[j])
                                j += 1
                            current_ejemplo['solucion']['salida'] = '\n'.join(salida_lines)
                            i = j
        
        # Parse notas
        if current_section == 'notas':
            if line.startswith('- '):
                data['notas_docente'].append(line[2:].strip())
        
        i += 1
    
    # Save last temario item
    if current_temario_item:
        data['temario'].append(current_temario_item)
    
    # Clean up ejemplos
    for ej in data['ejemplos']:
        ej['enunciado'] = ej['enunciado'].strip()
    
    return data


def migrate_file(md_path: Path, output_base: Path, file_type: str):
    """Migrate a single markdown file to YAML."""
    content = md_path.read_text(encoding='utf-8')
    
    if file_type == 'ejercicios':
        data = parse_ejercicios_markdown(content)
    else:
        data = parse_clase_markdown(content)
    
    # Determine output path
    relative_path = md_path.relative_to(Path(file_type))
    output_path = output_base / file_type / relative_path.with_suffix('.yml')
    
    # Create directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write YAML
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=120)
    
    return output_path


def main():
    output_base = Path('data')
    
    print("\n📄 Migrando Markdown a YAML...")
    
    # Migrate ejercicios
    ejercicios_dir = Path('ejercicios')
    if ejercicios_dir.exists():
        print(f"\n📁 ejercicios/")
        for md_file in sorted(ejercicios_dir.rglob('*.md')):
            output_path = migrate_file(md_file, output_base, 'ejercicios')
            print(f"  ✓ {md_file} → {output_path}")
    
    # Migrate clases
    clases_dir = Path('clases')
    if clases_dir.exists():
        print(f"\n📁 clases/")
        for md_file in sorted(clases_dir.rglob('*.md')):
            output_path = migrate_file(md_file, output_base, 'clases')
            print(f"  ✓ {md_file} → {output_path}")
    
    print(f"\n✅ Migración completada!")
    print(f"   Los archivos YAML están en: {output_base.absolute()}")


if __name__ == "__main__":
    main()
