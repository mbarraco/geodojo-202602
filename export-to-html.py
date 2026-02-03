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
    },
    "toc": {
        "permalink": False,
        "toc_depth": 3,  # Solo h1, h2, h3
    }
}

# Pico CSS desde CDN + estilos personalizados para syntax highlighting
CSS_LINK = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">'

# Estilos adicionales para syntax highlighting, sidebar TOC y ajustes
CUSTOM_STYLE = """
<style>
    /* Tipografía general más suave */
    :root {
        --pico-font-size: 0.9375rem;
    }
    
    body {
        font-weight: 400;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-weight: 500;
    }
    
    strong, b {
        font-weight: 500;
    }
    
    /* Layout con sidebar */
    .page-layout {
        display: grid;
        grid-template-columns: 220px 1fr;
        gap: 2rem;
        max-width: 1400px;
        margin: 0 auto;
        padding: 1rem;
    }
    
    /* Sidebar con TOC */
    .sidebar {
        position: sticky;
        top: 1rem;
        height: fit-content;
        max-height: calc(100vh - 2rem);
        overflow-y: auto;
        padding-right: 1rem;
        border-right: 1px solid var(--pico-muted-border-color);
    }
    
    .sidebar nav {
        font-size: 0.8125rem;
    }
    
    .sidebar .toc-title {
        font-weight: 500;
        margin-bottom: 0.75rem;
        color: var(--pico-muted-color);
        text-transform: uppercase;
        font-size: 0.6875rem;
        letter-spacing: 0.05em;
    }
    
    .sidebar .toc ul {
        list-style: none;
        padding-left: 0;
        margin: 0;
    }
    
    .sidebar .toc ul ul {
        padding-left: 0.875rem;
        margin-top: 0.125rem;
    }
    
    .sidebar .toc li {
        margin: 0.125rem 0;
    }
    
    .sidebar .toc a {
        color: var(--pico-muted-color);
        text-decoration: none;
        display: block;
        padding: 0.125rem 0;
        transition: color 0.2s;
    }
    
    .sidebar .toc a:hover {
        color: var(--pico-primary);
    }
    
    /* Contenido principal */
    .main-content {
        min-width: 0;
    }
    
    /* Navbar superior */
    .navbar {
        background-color: var(--pico-card-background-color);
        border-bottom: 1px solid var(--pico-muted-border-color);
        padding: 0.5rem 1.5rem;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    
    .navbar-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .navbar-brand {
        font-weight: 500;
        font-size: 0.9375rem;
        color: var(--pico-muted-color);
        text-decoration: none;
    }
    
    .navbar-brand:hover {
        color: var(--pico-color);
    }
    
    .navbar-nav {
        display: flex;
        gap: 1.25rem;
        list-style: none;
        margin: 0;
        padding: 0;
    }
    
    .navbar-nav a {
        color: var(--pico-muted-color);
        text-decoration: none;
        font-size: 0.8125rem;
    }
    
    .navbar-nav a:hover {
        color: var(--pico-color);
    }
    
    /* Index page styles */
    .container header h1 {
        font-size: 1.75rem;
        font-weight: 500;
        margin-bottom: 0.25rem;
    }
    
    .container header p {
        font-size: 0.875rem;
        color: var(--pico-muted-color);
    }
    
    .container h2 {
        font-size: 1.125rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    details summary {
        font-weight: 400;
        font-size: 0.875rem;
    }
    
    details ul {
        font-size: 0.8125rem;
    }
    
    /* Navegación en sidebar */
    .nav-home {
        margin-bottom: 1.5rem;
    }
    
    .nav-home a {
        font-size: 0.8125rem;
        color: var(--pico-muted-color);
    }
    
    /* Responsive: ocultar sidebar en móvil */
    @media (max-width: 900px) {
        .page-layout {
            grid-template-columns: 1fr;
        }
        
        .sidebar {
            display: none;
        }
    }
    
    /* Syntax highlighting (Pygments) - Light mode */
    .highlight {
        background-color: var(--pico-code-background-color);
        padding: 1rem;
        border-radius: var(--pico-border-radius);
        overflow-x: auto;
        margin-bottom: 1rem;
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
    .highlight .n { color: var(--pico-color); } /* Names */
    .highlight .nf, .highlight .nb { color: #6f42c1; } /* Functions */
    .highlight .mi, .highlight .mf { color: #005cc5; } /* Numbers */
    .highlight .o, .highlight .p { color: var(--pico-color); } /* Operators */
    .highlight .bp { color: #005cc5; } /* Built-in pseudo */
    
    /* Dark mode syntax highlighting */
    @media (prefers-color-scheme: dark) {
        .highlight .c, .highlight .c1, .highlight .cm { color: #8b949e; }
        .highlight .k, .highlight .kn, .highlight .kd { color: #ff7b72; }
        .highlight .s, .highlight .s1, .highlight .s2 { color: #a5d6ff; }
        .highlight .nf, .highlight .nb { color: #d2a8ff; }
        .highlight .mi, .highlight .mf { color: #79c0ff; }
        .highlight .bp { color: #79c0ff; }
    }
    
    /* Print styles */
    @media print {
        .sidebar {
            display: none;
        }
        
        .page-layout {
            display: block;
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


def convert_md_to_html(md_path: Path, depth: int = 2) -> str:
    """Convierte un archivo Markdown a HTML con estilo.
    
    Args:
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
    
    # Obtener tabla de contenidos generada por la extensión toc
    # El atributo 'toc' es añadido dinámicamente por la extensión
    toc_html = getattr(md, 'toc', "") or ""
    
    # Crear documento HTML completo
    title = md_path.stem.replace("-", " ").title()
    
    # Calcular ruta relativa al index
    home_path = "../" * depth + "index.html"
    
    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GeoDojo</title>
    {CSS_LINK}
    {CUSTOM_STYLE}
</head>
<body>
    <header class="navbar">
        <div class="navbar-content">
            <a href="{home_path}" class="navbar-brand">GeoDojo</a>
            <ul class="navbar-nav">
                <li><a href="{home_path}">Inicio</a></li>
                <li><a href="{home_path}#clases">Clases</a></li>
                <li><a href="{home_path}#ejercicios">Ejercicios</a></li>
            </ul>
        </div>
    </header>
    <div class="page-layout">
        <aside class="sidebar">
            <div class="toc-title">En esta página</div>
            <nav class="toc">
                {toc_html}
            </nav>
        </aside>
        <main class="main-content">
            {html_body}
        </main>
    </div>
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
        
        # Calcular profundidad (ej: clases/01/archivo.html = 2 niveles)
        depth = len(relative_path.parts)
        
        # Crear directorio si no existe
        html_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convertir y guardar
        html_content = convert_md_to_html(md_file, depth=depth)
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
    
    # Generar HTML del contenido
    html_content = []
    html_content.append('<header>')
    html_content.append('  <h1>GeoDojo</h1>')
    html_content.append('  <p>Curso de Python orientado a aplicaciones geográficas</p>')
    html_content.append('</header>')
    
    # Grid de dos columnas para Clases y Ejercicios
    html_content.append('<div class="grid">')
    
    # Sección de Clases
    if "clases" in sections:
        html_content.append('<section>')
        html_content.append('<h2 id="clases">Clases</h2>')
        for unit_num, files in sorted(sections["clases"].items()):
            unit_name = UNIT_NAMES.get(unit_num, f"Unidad {unit_num}")
            html_content.append(f'<details open>')
            html_content.append(f'  <summary>Unidad {unit_num}: {unit_name}</summary>')
            html_content.append('  <ul>')
            for html_file in files:
                rel_path = f"clases/{unit_num}/{html_file.name}"
                display_name = format_file_name(html_file.name)
                html_content.append(f'    <li><a href="{rel_path}">{display_name}</a></li>')
            html_content.append('  </ul>')
            html_content.append('</details>')
        html_content.append('</section>')
    
    # Sección de Ejercicios
    if "ejercicios" in sections:
        html_content.append('<section>')
        html_content.append('<h2 id="ejercicios">Ejercicios</h2>')
        for unit_num, files in sorted(sections["ejercicios"].items()):
            unit_name = UNIT_NAMES.get(unit_num, f"Unidad {unit_num}")
            html_content.append(f'<details open>')
            html_content.append(f'  <summary>Unidad {unit_num}: {unit_name}</summary>')
            html_content.append('  <ul>')
            for html_file in files:
                rel_path = f"ejercicios/{unit_num}/{html_file.name}"
                display_name = format_file_name(html_file.name)
                html_content.append(f'    <li><a href="{rel_path}">{display_name}</a></li>')
            html_content.append('  </ul>')
            html_content.append('</details>')
        html_content.append('</section>')
    
    html_content.append('</div>')  # Cierre del grid
    
    # Crear documento HTML completo
    html_body = '\n'.join(html_content)
    
    html_doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GeoDojo - Python para Geografía</title>
    {CSS_LINK}
    {CUSTOM_STYLE}
</head>
<body>
    <header class="navbar">
        <div class="navbar-content">
            <a href="index.html" class="navbar-brand">GeoDojo</a>
            <ul class="navbar-nav">
                <li><a href="#clases">Clases</a></li>
                <li><a href="#ejercicios">Ejercicios</a></li>
            </ul>
        </div>
    </header>
    <main class="container">
        {html_body}
    </main>
    <footer class="container">
        <small>GeoDojo - Curso de Python para aplicaciones geográficas</small>
    </footer>
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
