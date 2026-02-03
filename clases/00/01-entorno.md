# Clase 0: Entorno de trabajo

Configuración inicial del entorno de desarrollo Python.

---
## Resumen de comandos

| Acción | Mac/Linux | Windows |
|--------|-----------|---------|
| Crear venv | `python3 -m venv venv` | `python -m venv venv` |
| Activar | `source venv/bin/activate` | `venv\Scripts\activate` |
| Desactivar | `deactivate` | `deactivate` |
| Instalar black | `pip install black` | `pip install black` |
| Formatear | `black .` | `black .` |

---

## 1. Crear un entorno virtual

Un entorno virtual aísla las dependencias de cada proyecto.

### Mac / Linux

```bash
# Crear el entorno
python3 -m venv venv

# Activar
source venv/bin/activate

# Verificar (debe mostrar la ruta del venv)
which python
```

### Windows

```powershell
# Crear el entorno
python -m venv venv

# Activar
venv\Scripts\activate

# Verificar
where python
```

### Desactivar (ambos sistemas)

```bash
deactivate
```

---

## 2. Instalar dependencias

Con el entorno activado:

```bash
pip install black
```

Verificar instalación:

```bash
black --version
```

---

## 3. Usar Black

Black es un formateador automático de código Python.

### Formatear un archivo

```bash
black archivo.py
```

### Formatear todos los archivos de un directorio

```bash
black .
```

### Ver cambios sin aplicar (dry-run)

```bash
black --check .
black --diff archivo.py
```

---

## 4. PEP 8

PEP 8 es la guía de estilo oficial de Python. Black aplica automáticamente la mayoría de las reglas.

Reglas principales:
- Indentación: 4 espacios
- Líneas: máximo 88 caracteres (Black) o 79 (PEP 8 estricto)
- Imports: uno por línea, agrupados (stdlib, terceros, locales)
- Espacios: después de comas, alrededor de operadores

---

## 5. Flujo de trabajo recomendado

```bash
# 1. Crear proyecto
mkdir mi_proyecto
cd mi_proyecto

# 2. Crear y activar entorno
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# o: venv\Scripts\activate  # Windows

# 3. Instalar dependencias
pip install black

# 4. Trabajar en el código
# ... editar archivos .py ...

# 5. Formatear antes de guardar/commitear
black .
```

---

