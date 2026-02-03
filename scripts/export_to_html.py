#!/usr/bin/env python3
"""
Exporta archivos Markdown a HTML con estilo usando Jinja2 templates.
Uso: python scripts/export_to_html.py [directorio_salida]
"""

import markdown
from pathlib import Path
import sys
import re
import shutil
from jinja2 import Environment, FileSystemLoader

# Directorio base del script
SCRIPT_DIR = Path(__file__).parent

# Directorios a procesar
DIRS_TO_EXPORT = ["ejercicios", "clases"]

# Extensiones de markdown para mejor renderizado
MD_EXTENSIONS = [
    "tables",           # Tablas
    "fenced_code",      # Bloques de código con ```
    "codehilite",       # Syntax highlighting
    "toc",              # Tabla de contenidos
    "nl2br",            # Newlines a <br>
]

# Configuración de extensiones
MD_EXTENSION_CONFIGS = {
    "codehilite": {
        "css_class": "highlight",
        "linenums": False,
        "guess_lang": True,
    },
    "toc": {
        "permalink": False,
        "toc_depth": 3,  # Solo h1, h2, h3
    }
}

# Nombres descriptivos para las unidades
UNIT_NAMES = {
    "00": "Preparación del Entorno",
    "01": "Fundamentos de Python",
    "02": "Estructuras de Control",
    "03": "Archivos y Pandas",
    "04": "NumPy",
}


def get_jinja_env() -> Environment:
    """Crea y retorna el entorno Jinja2 con los templates."""
    template_dir = SCRIPT_DIR / "templates"
    return Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=False,  # No escapar HTML generado por markdown
    )


def preprocess_markdown(content: str) -> str:
    """
    Preprocesa el markdown para arreglar bloques de código indentados.
    Los bloques ``` dentro de listas a veces no se parsean bien.
    """
    lines = content.split('\n')
    result = []
    in_code_block = False
    code_block_indent = 0
    
    for line in lines:
        # Detectar inicio de bloque de código (puede estar indentado)
        stripped = line.lstrip()
        current_indent = len(line) - len(stripped)
        
        if stripped.startswith('```'):
            if not in_code_block:
                # Inicio de bloque de código
                in_code_block = True
                code_block_indent = current_indent
                # Agregar el bloque sin indentación extra
                lang = stripped[3:].strip()
                if not lang:
                    lang = "text"  # Agregar lenguaje por defecto
                result.append(f'```{lang}')
            else:
                # Fin de bloque de código
                in_code_block = False
                result.append('```')
        elif in_code_block:
            # Dentro de bloque de código, quitar la indentación del bloque
            if line.startswith(' ' * code_block_indent):
                result.append(line[code_block_indent:])
            else:
                result.append(line)
        else:
            result.append(line)
    
    return '\n'.join(result)


def wrap_headings_in_details(html: str, level: int) -> str:
    """
    Envuelve los headings de un nivel específico en elementos <details>.
    Procesa recursivamente los niveles inferiores dentro del contenido.
    """
    tag = f'h{level}'
    pattern = re.compile(rf'<{tag}([^>]*)>(.*?)</{tag}>', re.DOTALL)
    
    matches = list(pattern.finditer(html))
    if not matches:
        return html
    
    result = []
    last_end = 0
    
    for i, match in enumerate(matches):
        # Agregar contenido antes de este heading
        result.append(html[last_end:match.start()])
        
        # Determinar dónde termina el contenido de esta sección
        if i + 1 < len(matches):
            section_end = matches[i + 1].start()
        else:
            section_end = len(html)
        
        # Contenido de la sección (después del heading)
        section_content = html[match.end():section_end]
        
        # Si hay nivel inferior, procesar recursivamente
        if level < 3:
            section_content = wrap_headings_in_details(section_content, level + 1)
        
        # Crear el elemento details
        attrs = match.group(1)
        title = match.group(2)
        
        result.append(f'<details class="section-collapsible">')
        result.append(f'<summary><{tag}{attrs}>{title}</{tag}></summary>')
        result.append(f'<div class="section-content">')
        result.append(section_content.strip())
        result.append('</div>')
        result.append('</details>')
        
        last_end = section_end
    
    # Agregar cualquier contenido restante después del último heading
    if last_end < len(html):
        result.append(html[last_end:])
    
    return '\n'.join(result)


def make_sections_collapsible(html_body: str) -> str:
    """
    Post-procesa el HTML para convertir secciones h2/h3 en elementos <details> colapsables.
    El h1 (título principal) no se colapsa.
    """
    # Encontrar dónde empieza el primer h2
    first_h2 = re.search(r'<h2[^>]*>', html_body)
    if not first_h2:
        return html_body
    
    # Dividir: contenido antes del primer h2 (incluye h1) y el resto
    before_h2 = html_body[:first_h2.start()]
    from_h2 = html_body[first_h2.start():]
    
    # Procesar h2 (y recursivamente h3 dentro de cada h2)
    processed = wrap_headings_in_details(from_h2, 2)
    
    return before_h2 + processed


def convert_md_to_html(env: Environment, md_path: Path, depth: int = 2) -> str:
    """Convierte un archivo Markdown a HTML con estilo.
    
    Args:
        env: Entorno Jinja2
        md_path: Ruta al archivo markdown
        depth: Profundidad desde web/ para calcular ruta al index (default: 2 para clases/01/)
    """
    md_content = md_path.read_text(encoding="utf-8")
    
    # Preprocesar para arreglar bloques de código indentados
    md_content = preprocess_markdown(md_content)
    
    # Convertir Markdown a HTML
    md = markdown.Markdown(
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS
    )
    html_body = md.convert(md_content)
    
    # Hacer las secciones colapsables (h2, h3)
    html_body = make_sections_collapsible(html_body)
    
    # Obtener tabla de contenidos generada por la extensión toc
    toc_html = getattr(md, 'toc', "") or ""
    
    # Calcular rutas relativas
    title = md_path.stem.replace("-", " ").title()
    home_path = "../" * depth + "index.html"
    static_path = "../" * depth + "static/"
    
    # Renderizar template
    template = env.get_template("page.html")
    return template.render(
        title=title,
        home_path=home_path,
        static_path=static_path,
        toc_html=toc_html,
        content=html_body,
    )


def export_directory(env: Environment, source_dir: Path, output_dir: Path):
    """Exporta todos los archivos .md de un directorio a HTML."""
    md_files = list(source_dir.rglob("*.md"))
    
    if not md_files:
        print(f"  No se encontraron archivos .md en {source_dir}")
        return
    
    for md_file in md_files:
        # Calcular ruta de salida manteniendo la estructura
        relative_path = md_file.relative_to(source_dir)
        html_path = output_dir / source_dir.name / relative_path.with_suffix(".html")
        
        # Calcular profundidad (ej: clases/01/archivo.html = 2 niveles)
        depth = len(relative_path.parts)
        
        # Crear directorio si no existe
        html_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convertir y guardar
        html_content = convert_md_to_html(env, md_file, depth=depth)
        html_path.write_text(html_content, encoding="utf-8")
        
        print(f"  ✓ {md_file} → {html_path}")


def format_file_name(filename: str) -> str:
    """Convierte un nombre de archivo a formato legible."""
    # Quitar extensión y número inicial (ej: "01-fundamentos.html" -> "Fundamentos")
    name = filename.replace(".html", "")
    parts = name.split("-", 1)
    if len(parts) > 1:
        name = parts[1]
    return name.replace("-", " ").title()


def generate_index_html(env: Environment, output_dir: Path):
    """Genera el index.html con links a todo el contenido."""
    
    # Recolectar archivos HTML por sección y unidad
    sections = {}
    
    for section in ["clases", "ejercicios"]:
        section_path = output_dir / section
        if not section_path.exists():
            continue
        
        sections[section] = {}
        
        # Buscar todas las unidades (carpetas numeradas)
        for unit_dir in sorted(section_path.iterdir()):
            if unit_dir.is_dir():
                unit_num = unit_dir.name
                html_files = sorted(unit_dir.glob("*.html"))
                if html_files:
                    # Crear lista de objetos con nombre y display_name
                    sections[section][unit_num] = [
                        {"name": f.name, "display_name": format_file_name(f.name)}
                        for f in html_files
                    ]
    
    # Renderizar template
    template = env.get_template("index.html")
    html_doc = template.render(
        title="GeoDojo",
        home_path="index.html",
        static_path="static/",
        sections=sections,
        unit_names=UNIT_NAMES,
    )
    
    # Guardar index.html
    index_path = output_dir / "index.html"
    index_path.write_text(html_doc, encoding="utf-8")
    print(f"  ✓ index.html generado")


def copy_static_files(output_dir: Path):
    """Copia los archivos estáticos al directorio de salida."""
    static_src = SCRIPT_DIR / "static"
    static_dst = output_dir / "static"
    
    # Crear directorio si no existe
    static_dst.mkdir(parents=True, exist_ok=True)
    
    # Copiar archivos CSS
    for css_file in static_src.glob("*.css"):
        shutil.copy2(css_file, static_dst / css_file.name)
        print(f"  ✓ {css_file.name} → {static_dst / css_file.name}")


def main():
    # Directorio de salida (por defecto: web)
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("web")
    
    print(f"\n📄 Exportando Markdown a HTML...")
    print(f"   Destino: {output_dir.absolute()}\n")
    
    # Inicializar Jinja2
    env = get_jinja_env()
    
    # Copiar archivos estáticos
    print(f"📁 static/")
    copy_static_files(output_dir)
    
    # Procesar cada directorio
    for dir_name in DIRS_TO_EXPORT:
        source_dir = Path(dir_name)
        if source_dir.exists():
            print(f"\n📁 {dir_name}/")
            export_directory(env, source_dir, output_dir)
        else:
            print(f"⚠️  Directorio '{dir_name}' no encontrado")
    
    # Generar landing page
    print(f"\n📄 Generando index.html...")
    generate_index_html(env, output_dir)
    
    print(f"\n✅ Exportación completada!")
    print(f"   Abrí los archivos HTML en tu navegador.")
    print(f"   Para guardar como PDF: Archivo → Imprimir → Guardar como PDF\n")


if __name__ == "__main__":
    main()
