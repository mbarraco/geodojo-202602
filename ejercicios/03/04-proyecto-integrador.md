# Proyecto Integrador: Gestor de Rutas con Persistencia

Un proyecto paso a paso para construir un gestor de rutas geográficas que guarda y carga datos desde archivos.

---

## Descripción del proyecto

Vamos a construir un programa que:
- Carga rutas guardadas desde archivos CSV
- Permite agregar, editar y eliminar destinos
- Guarda los cambios automáticamente
- Genera reportes en diferentes formatos (TXT, CSV)
- Maneja errores de forma robusta (archivos corruptos, datos inválidos)
- Analiza datos con Pandas

Este proyecto integra conceptos de la Unidad 3: archivos, CSV, módulos, manejo de errores y Pandas. También reutiliza funciones de las unidades anteriores.

---

## Paso 1: Estructura del proyecto

**Objetivo**: Crear la estructura de archivos del proyecto con módulos separados.

**Tareas**:
1. Crear un directorio `planificador/`
2. Crear los archivos:
   - `main.py` - Programa principal con el menú
   - `datos.py` - Funciones de lectura/escritura de archivos
   - `calculos.py` - Funciones de cálculo (distancia, punto medio)
   - `validacion.py` - Funciones de validación de datos

**Estructura**:
```
planificador/
├── main.py
├── datos.py
├── calculos.py
├── validacion.py
└── rutas/           # Directorio para guardar rutas
    └── .gitkeep
```

**Hint**: Empezá creando archivos vacíos y luego agregá funciones gradualmente.

---

## Paso 2: Módulo de validación

**Objetivo**: Crear funciones de validación reutilizables en `validacion.py`.

**Tareas**:
1. Crear función `es_coordenada_valida(lat, lon)` que retorne True/False
2. Crear función `validar_nombre(nombre)` que verifique que no esté vacío
3. Crear función `convertir_coordenada(texto)` que convierta string a float o retorne None

**Ejemplo de código**:
```python
# validacion.py

def es_coordenada_valida(lat, lon):
    """Verifica si las coordenadas están en rangos válidos."""
    try:
        lat = float(lat)
        lon = float(lon)
        return -90 <= lat <= 90 and -180 <= lon <= 180
    except (ValueError, TypeError):
        return False

def convertir_coordenada(texto):
    """Convierte string a float, retorna None si falla."""
    try:
        return float(texto)
    except ValueError:
        return None
```

---

## Paso 3: Módulo de cálculos

**Objetivo**: Mover las funciones de cálculo de unidades anteriores a `calculos.py`.

**Tareas**:
1. Crear función `distancia_entre(lat1, lon1, lat2, lon2)`
2. Crear función `punto_medio(lat1, lon1, lat2, lon2)`
3. Crear función `generar_link_maps(lat, lon)`

**Ejemplo de código**:
```python
# calculos.py

def distancia_entre(lat1, lon1, lat2, lon2):
    """Calcula distancia euclidiana simplificada entre dos puntos."""
    return ((lat2 - lat1)**2 + (lon2 - lon1)**2) ** 0.5

def distancia_km(lat1, lon1, lat2, lon2):
    """Convierte distancia en grados a km aproximados."""
    grados = distancia_entre(lat1, lon1, lat2, lon2)
    return round(grados * 111, 1)

def generar_link_maps(lat, lon):
    """Genera link de Google Maps para una coordenada."""
    return f"https://www.google.com/maps?q={lat},{lon}"
```

---

## Paso 4: Guardar ruta a CSV

**Objetivo**: Crear función para guardar una ruta a archivo CSV en `datos.py`.

**Tareas**:
1. Crear función `guardar_ruta(ruta, nombre_archivo)`
2. Usar `csv.DictWriter` para escribir los destinos
3. Manejar errores de escritura

**Ejemplo de código**:
```python
# datos.py
import csv
import os

def guardar_ruta(ruta, nombre_archivo):
    """Guarda una lista de destinos a un archivo CSV."""
    try:
        with open(nombre_archivo, "w", newline="") as f:
            campos = ["nombre", "lat", "lon"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(ruta)
        return True
    except IOError as e:
        print(f"Error al guardar: {e}")
        return False
```

**Ejemplo de archivo generado** (`rutas/mi_ruta.csv`):
```csv
nombre,lat,lon
Buenos Aires,-34.6,-58.4
Córdoba,-31.4,-64.2
Mendoza,-32.9,-68.8
```

---

## Paso 5: Cargar ruta desde CSV

**Objetivo**: Crear función para cargar una ruta desde archivo CSV.

**Tareas**:
1. Crear función `cargar_ruta(nombre_archivo)` que retorne lista de diccionarios
2. Manejar `FileNotFoundError` si el archivo no existe
3. Validar que las coordenadas sean válidas al cargar

**Ejemplo de código**:
```python
def cargar_ruta(nombre_archivo):
    """Carga una ruta desde archivo CSV. Retorna lista vacía si hay error."""
    try:
        with open(nombre_archivo, "r") as f:
            reader = csv.DictReader(f)
            ruta = []
            for fila in reader:
                destino = {
                    "nombre": fila["nombre"],
                    "lat": float(fila["lat"]),
                    "lon": float(fila["lon"])
                }
                ruta.append(destino)
            return ruta
    except FileNotFoundError:
        print(f"Archivo '{nombre_archivo}' no encontrado. Creando ruta nueva.")
        return []
    except (ValueError, KeyError) as e:
        print(f"Error en formato del archivo: {e}")
        return []
```

---

## Paso 6: Listar rutas guardadas

**Objetivo**: Mostrar todas las rutas guardadas en el directorio.

**Tareas**:
1. Crear función `listar_rutas(directorio)` que retorne lista de archivos .csv
2. Usar `os.listdir()` para obtener archivos
3. Filtrar solo archivos con extensión .csv

**Ejemplo de código**:
```python
import os

def listar_rutas(directorio="rutas"):
    """Lista todos los archivos de ruta en el directorio."""
    try:
        archivos = os.listdir(directorio)
        rutas = [f for f in archivos if f.endswith(".csv")]
        return rutas
    except FileNotFoundError:
        os.makedirs(directorio, exist_ok=True)
        return []
```

**Ejemplo de salida**:
```
Rutas guardadas:
1. mi_viaje.csv
2. ruta_norte.csv
3. vacaciones.csv
```

---

## Paso 7: Autoguardado

**Objetivo**: Implementar guardado automático después de cada cambio.

**Tareas**:
1. Crear variable global o parámetro para el archivo actual
2. Llamar a `guardar_ruta()` después de agregar o eliminar destinos
3. Mostrar confirmación de guardado

**Ejemplo de flujo**:
```
> Agregar destino
Nombre: Salta
Latitud: -24.8
Longitud: -65.4
✓ Destino agregado
✓ Ruta guardada automáticamente
```

---

## Paso 8: Análisis con Pandas

**Objetivo**: Agregar funciones de análisis usando Pandas.

**Tareas**:
1. Crear función `analizar_ruta(nombre_archivo)` que use pandas
2. Calcular estadísticas: ciudad más al norte/sur, distancia total
3. Generar resumen formateado

**Ejemplo de código**:
```python
import pandas as pd

def analizar_ruta(nombre_archivo):
    """Analiza una ruta usando Pandas."""
    df = pd.read_csv(nombre_archivo)
    
    print(f"\n=== ANÁLISIS DE RUTA ===")
    print(f"Total de destinos: {len(df)}")
    
    # Ciudad más al norte (mayor latitud)
    idx_norte = df["lat"].idxmax()
    print(f"Más al norte: {df.loc[idx_norte, 'nombre']} ({df.loc[idx_norte, 'lat']})")
    
    # Ciudad más al sur (menor latitud)
    idx_sur = df["lat"].idxmin()
    print(f"Más al sur: {df.loc[idx_sur, 'nombre']} ({df.loc[idx_sur, 'lat']})")
    
    # Coordenadas promedio (centro aproximado)
    print(f"Centro aproximado: ({df['lat'].mean():.2f}, {df['lon'].mean():.2f})")
```

---

## Paso 9: Exportar reporte

**Objetivo**: Generar reportes en formato texto y CSV.

**Tareas**:
1. Crear función `exportar_reporte_txt(ruta, nombre_archivo)`
2. Crear función `exportar_reporte_csv(ruta, nombre_archivo)` con columnas adicionales
3. Incluir links de Google Maps en el reporte

**Ejemplo de reporte TXT**:
```
╔════════════════════════════════════════╗
║         REPORTE DE RUTA                ║
╚════════════════════════════════════════╝

Fecha: 2026-02-03
Total de destinos: 3

DESTINOS:
─────────────────────────────────────────
1. Buenos Aires
   Coordenadas: -34.6, -58.4
   Maps: https://www.google.com/maps?q=-34.6,-58.4

2. Córdoba
   Coordenadas: -31.4, -64.2
   Maps: https://www.google.com/maps?q=-31.4,-64.2

ESTADÍSTICAS:
─────────────────────────────────────────
Distancia total: ~850 km
Ciudad más al norte: Córdoba
Ciudad más al sur: Buenos Aires
```

---

## Paso 10: Programa completo

**Objetivo**: Integrar todos los módulos en un programa con menú interactivo.

**Menú del programa**:
```
╔════════════════════════════════════════╗
║     GESTOR DE RUTAS GEOGRÁFICAS        ║
╚════════════════════════════════════════╝

Ruta actual: mi_viaje.csv (3 destinos)

1. Ver ruta actual
2. Agregar destino
3. Eliminar destino
4. Nueva ruta
5. Cargar ruta existente
6. Ver análisis (Pandas)
7. Exportar reporte
8. Salir

Opción: 
```

**Ejemplo de ejecución completa**:
```
Opción: 5
Rutas disponibles:
1. mi_viaje.csv
2. vacaciones.csv
Elegir ruta (número): 1
✓ Ruta 'mi_viaje.csv' cargada (3 destinos)

Opción: 6

=== ANÁLISIS DE RUTA ===
Total de destinos: 3
Más al norte: Córdoba (-31.4)
Más al sur: Buenos Aires (-34.6)
Centro aproximado: (-32.97, -63.80)

Opción: 7
Formato (1=TXT, 2=CSV): 1
Nombre del archivo: reporte_viaje
✓ Reporte guardado en 'reportes/reporte_viaje.txt'

Opción: 8
¡Hasta luego! Ruta guardada automáticamente.
```

---

## Conceptos utilizados

| Concepto | Dónde se usa |
|----------|--------------|
| **Módulos propios** | `datos.py`, `calculos.py`, `validacion.py` |
| **import** | Importar funciones entre módulos |
| **csv.DictWriter** | Guardar ruta a CSV |
| **csv.DictReader** | Cargar ruta desde CSV |
| **try/except** | Manejo de errores de archivo y datos |
| **os.listdir** | Listar rutas guardadas |
| **os.makedirs** | Crear directorios |
| **FileNotFoundError** | Manejar archivo inexistente |
| **ValueError** | Manejar datos inválidos |
| **pandas.read_csv** | Análisis de datos |
| **DataFrame.idxmax/min** | Encontrar extremos |
| **with open()** | Context manager para archivos |

---

## Desafíos extra

1. **Backup automático**: Antes de sobrescribir un archivo, crear una copia de respaldo con fecha.

2. **Formato JSON**: Agregar opción para guardar/cargar rutas en formato JSON además de CSV.

3. **Búsqueda de destinos**: Implementar búsqueda por nombre parcial en todas las rutas guardadas.

4. **Exportar a KML**: Investigar el formato KML y exportar la ruta para abrir en Google Earth.

5. **Validación de CSV**: Crear función que verifique si un archivo CSV tiene el formato correcto antes de cargarlo.

6. **Historial de cambios**: Guardar un log de todas las operaciones realizadas (agregar, eliminar, etc.)

7. **Importar desde URL**: Permitir cargar un CSV directamente desde una URL usando `pandas.read_csv()`.

---

## Conexión con la Unidad anterior

Este proyecto es una evolución del **Proyecto Integrador de la Unidad 2** (Planificador de Ruta):

| Unidad 2 | Unidad 3 |
|----------|----------|
| Datos en memoria (se pierden al cerrar) | Datos persistentes en archivos CSV |
| Todo en un archivo | Código organizado en módulos |
| Sin manejo de errores | try/except para archivos y datos |
| Sin análisis | Estadísticas con Pandas |
| Un solo formato de salida | Múltiples formatos (TXT, CSV) |

Funciones reutilizables de unidades anteriores:
- `distancia_entre()` → en `calculos.py`
- `es_coordenada_valida()` → en `validacion.py`
- `generar_link_maps()` → en `calculos.py`
- Estructura de menú → en `main.py`

---

*Fin del proyecto integrador - Unidad 3*
