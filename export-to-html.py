#!/usr/bin/env python3
"""
Exporta archivos Markdown a HTML con estilo.
Uso: python export-to-html.py [directorio_salida]
"""

import markdown
from pathlib import Path
import sys
import re

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
    }
}

# CSS para el estilo del documento
CSS_STYLE = """
<style>
    :root {
        --bg-color: #ffffff;
        --text-color: #24292e;
        --code-bg: #f6f8fa;
        --border-color: #e1e4e8;
        --link-color: #0366d6;
        --heading-color: #24292e;
    }
    
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
        font-size: 16px;
        line-height: 1.6;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px 20px;
        color: var(--text-color);
        background-color: var(--bg-color);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--heading-color);
        margin-top: 24px;
        margin-bottom: 16px;
        font-weight: 600;
        line-height: 1.25;
    }
    
    h1 {
        font-size: 2em;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 0.3em;
    }
    
    h2 {
        font-size: 1.5em;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 0.3em;
    }
    
    h3 {
        font-size: 1.25em;
    }
    
    code {
        font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
        font-size: 85%;
        background-color: var(--code-bg);
        padding: 0.2em 0.4em;
        border-radius: 6px;
    }
    
    pre {
        background-color: var(--code-bg);
        padding: 16px;
        overflow: auto;
        font-size: 85%;
        line-height: 1.45;
        border-radius: 6px;
        border: 1px solid var(--border-color);
    }
    
    pre code {
        background-color: transparent;
        padding: 0;
        font-size: 100%;
    }
    
    /* Syntax highlighting (Pygments) */
    .highlight {
        background-color: var(--code-bg);
        padding: 16px;
        border-radius: 6px;
        overflow-x: auto;
        border: 1px solid var(--border-color);
    }
    
    .highlight pre {
        margin: 0;
        padding: 0;
        background: transparent;
        border: none;
    }
    
    .highlight .c, .highlight .c1, .highlight .cm { color: #6a737d; } /* Comments */
    .highlight .k, .highlight .kn, .highlight .kd { color: #d73a49; } /* Keywords */
    .highlight .s, .highlight .s1, .highlight .s2 { color: #032f62; } /* Strings */
    .highlight .n { color: #24292e; } /* Names */
    .highlight .nf, .highlight .nb { color: #6f42c1; } /* Functions */
    .highlight .mi, .highlight .mf { color: #005cc5; } /* Numbers */
    .highlight .o, .highlight .p { color: #24292e; } /* Operators */
    .highlight .bp { color: #005cc5; } /* Built-in pseudo */
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 16px 0;
    }
    
    th, td {
        border: 1px solid var(--border-color);
        padding: 8px 12px;
        text-align: left;
    }
    
    th {
        background-color: var(--code-bg);
        font-weight: 600;
    }
    
    tr:nth-child(even) {
        background-color: #f6f8fa;
    }
    
    blockquote {
        margin: 0;
        padding: 0 1em;
        color: #6a737d;
        border-left: 0.25em solid var(--border-color);
    }
    
    hr {
        height: 0.25em;
        padding: 0;
        margin: 24px 0;
        background-color: var(--border-color);
        border: 0;
    }
    
    a {
        color: var(--link-color);
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    ul, ol {
        padding-left: 2em;
    }
    
    li + li {
        margin-top: 0.25em;
    }
    
    strong {
        font-weight: 600;
    }
    
    /* Print styles */
    @media print {
        body {
            max-width: 100%;
            padding: 20px;
        }
        
        pre, .highlight {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        h1, h2, h3 {
            page-break-after: avoid;
        }
        
        pre, table {
            page-break-inside: avoid;
        }
    }
</style>
"""


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


def convert_md_to_html(md_path: Path) -> str:
    """Convierte un archivo Markdown a HTML con estilo."""
    md_content = md_path.read_text(encoding="utf-8")
    
    # Preprocesar para arreglar bloques de código indentados
    md_content = preprocess_markdown(md_content)
    
    # Convertir Markdown a HTML
    md = markdown.Markdown(
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS
    )
    html_body = md.convert(md_content)
    
    # Crear documento HTML completo
    title = md_path.stem.replace("-", " ").title()
    
    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {CSS_STYLE}
</head>
<body>
{html_body}
</body>
</html>
"""
    return html_doc


def export_directory(source_dir: Path, output_dir: Path):
    """Exporta todos los archivos .md de un directorio a HTML."""
    md_files = list(source_dir.rglob("*.md"))
    
    if not md_files:
        print(f"  No se encontraron archivos .md en {source_dir}")
        return
    
    for md_file in md_files:
        # Calcular ruta de salida manteniendo la estructura
        relative_path = md_file.relative_to(source_dir)
        html_path = output_dir / source_dir.name / relative_path.with_suffix(".html")
        
        # Crear directorio si no existe
        html_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convertir y guardar
        html_content = convert_md_to_html(md_file)
        html_path.write_text(html_content, encoding="utf-8")
        
        print(f"  ✓ {md_file} → {html_path}")


# Nombres descriptivos para las unidades
UNIT_NAMES = {
    "00": "Preparación del Entorno",
    "01": "Fundamentos de Python",
    "02": "Estructuras de Control",
    "03": "Archivos y Pandas",
    "04": "NumPy",
}


def format_file_name(filename: str) -> str:
    """Convierte un nombre de archivo a formato legible."""
    # Quitar extensión y número inicial (ej: "01-fundamentos.html" -> "Fundamentos")
    name = filename.replace(".html", "")
    parts = name.split("-", 1)
    if len(parts) > 1:
        name = parts[1]
    return name.replace("-", " ").title()


def generate_index_html(output_dir: Path):
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
                    sections[section][unit_num] = html_files
    
    # Generar HTML
    html_content = []
    html_content.append('<h1>GeoDojo - Python para Geografía</h1>')
    html_content.append('<p>Curso de Python orientado a aplicaciones geográficas.</p>')
    
    # Sección de Clases
    if "clases" in sections:
        html_content.append('<h2>Clases</h2>')
        for unit_num, files in sorted(sections["clases"].items()):
            unit_name = UNIT_NAMES.get(unit_num, f"Unidad {unit_num}")
            html_content.append(f'<h3>Unidad {unit_num}: {unit_name}</h3>')
            html_content.append('<ul>')
            for html_file in files:
                rel_path = f"clases/{unit_num}/{html_file.name}"
                display_name = format_file_name(html_file.name)
                html_content.append(f'  <li><a href="{rel_path}">{display_name}</a></li>')
            html_content.append('</ul>')
    
    # Sección de Ejercicios
    if "ejercicios" in sections:
        html_content.append('<h2>Ejercicios</h2>')
        for unit_num, files in sorted(sections["ejercicios"].items()):
            unit_name = UNIT_NAMES.get(unit_num, f"Unidad {unit_num}")
            html_content.append(f'<h3>Unidad {unit_num}: {unit_name}</h3>')
            html_content.append('<ul>')
            for html_file in files:
                rel_path = f"ejercicios/{unit_num}/{html_file.name}"
                display_name = format_file_name(html_file.name)
                html_content.append(f'  <li><a href="{rel_path}">{display_name}</a></li>')
            html_content.append('</ul>')
    
    # Crear documento HTML completo
    html_body = '\n'.join(html_content)
    
    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GeoDojo - Python para Geografía</title>
    {CSS_STYLE}
</head>
<body>
{html_body}
</body>
</html>
"""
    
    # Guardar index.html
    index_path = output_dir / "index.html"
    index_path.write_text(html_doc, encoding="utf-8")
    print(f"  ✓ index.html generado")


def main():
    # Directorio de salida (por defecto: web)
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("web")
    
    print(f"\n📄 Exportando Markdown a HTML...")
    print(f"   Destino: {output_dir.absolute()}\n")
    
    # Procesar cada directorio
    for dir_name in DIRS_TO_EXPORT:
        source_dir = Path(dir_name)
        if source_dir.exists():
            print(f"📁 {dir_name}/")
            export_directory(source_dir, output_dir)
        else:
            print(f"⚠️  Directorio '{dir_name}' no encontrado")
    
    # Generar landing page
    print(f"\n📄 Generando index.html...")
    generate_index_html(output_dir)
    
    print(f"\n✅ Exportación completada!")
    print(f"   Abrí los archivos HTML en tu navegador.")
    print(f"   Para guardar como PDF: Archivo → Imprimir → Guardar como PDF\n")


if __name__ == "__main__":
    main()
