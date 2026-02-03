.PHONY: html clean install clean-all

# Directorio de salida
OUTPUT_DIR = web
VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# Crear entorno virtual
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

# Instalar dependencias de Python
install: $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

# Convertir Markdown a HTML
html: install
	$(PYTHON) scripts/export_to_html.py $(OUTPUT_DIR)

# Limpiar archivos generados
clean:
	rm -rf $(OUTPUT_DIR)
	rm -f test.html

# Limpiar todo (incluyendo venv)
clean-all: clean
	rm -rf $(VENV)
