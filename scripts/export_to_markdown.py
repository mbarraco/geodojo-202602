#!/usr/bin/env python3
"""
Genera archivos Markdown a partir de YAML.
Uso: python scripts/export_to_markdown.py
"""

import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Directorio base del script
SCRIPT_DIR = Path(__file__).parent


def get_jinja_env() -> Environment:
    """Crea y retorna el entorno Jinja2 con los templates de markdown."""
    template_dir = SCRIPT_DIR / "templates" / "markdown"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env


def load_yaml(path: Path) -> dict:
    """Carga un archivo YAML."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def export_ejercicios(env: Environment, yaml_path: Path, output_dir: Path):
    """Genera un archivo markdown de ejercicios desde YAML."""
    data = load_yaml(yaml_path)
    
    # Determine output path
    relative_path = yaml_path.relative_to(Path('data/ejercicios'))
    output_path = output_dir / relative_path.with_suffix('.md')
    
    # Create directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Render template
    template = env.get_template('ejercicios.md.j2')
    content = template.render(**data)
    
    # Clean up extra blank lines
    content = _clean_markdown(content)
    
    # Write output
    output_path.write_text(content, encoding='utf-8')
    
    return output_path


def export_clase(env: Environment, yaml_path: Path, output_dir: Path):
    """Genera un archivo markdown de clase desde YAML."""
    data = load_yaml(yaml_path)
    
    # Determine output path
    relative_path = yaml_path.relative_to(Path('data/clases'))
    output_path = output_dir / relative_path.with_suffix('.md')
    
    # Create directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Render template
    template = env.get_template('clase.md.j2')
    content = template.render(**data)
    
    # Clean up extra blank lines
    content = _clean_markdown(content)
    
    # Write output
    output_path.write_text(content, encoding='utf-8')
    
    return output_path


def _clean_markdown(content: str) -> str:
    """Clean up extra blank lines in markdown."""
    import re
    # Replace 3+ consecutive newlines with 2
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Ensure file ends with single newline
    content = content.strip() + '\n'
    return content


def main():
    data_dir = Path('data')
    
    print("\n📄 Generando Markdown desde YAML...")
    
    env = get_jinja_env()
    
    # Export ejercicios
    ejercicios_data = data_dir / 'ejercicios'
    if ejercicios_data.exists():
        output_dir = Path('ejercicios')
        print(f"\n📁 ejercicios/")
        for yaml_file in sorted(ejercicios_data.rglob('*.yml')):
            output_path = export_ejercicios(env, yaml_file, output_dir)
            print(f"  ✓ {yaml_file} → {output_path}")
    
    # Export clases
    clases_data = data_dir / 'clases'
    if clases_data.exists():
        output_dir = Path('clases')
        print(f"\n📁 clases/")
        for yaml_file in sorted(clases_data.rglob('*.yml')):
            output_path = export_clase(env, yaml_file, output_dir)
            print(f"  ✓ {yaml_file} → {output_path}")
    
    print(f"\n✅ Generación de Markdown completada!")


if __name__ == "__main__":
    main()
