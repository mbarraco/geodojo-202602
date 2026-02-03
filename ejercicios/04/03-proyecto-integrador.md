# Proyecto Integrador: Análisis de Vegetación con NDVI

Un proyecto paso a paso para construir un analizador de imágenes satelitales que calcula índices de vegetación.

---

## Descripción del proyecto

Vamos a construir un programa que:
- Carga datos de bandas espectrales desde archivos CSV
- Calcula el índice NDVI (Normalized Difference Vegetation Index)
- Clasifica pixels según nivel de vegetación
- Genera estadísticas por zona geográfica
- Visualiza resultados (opcional, con matplotlib)
- Exporta resultados procesados

Este proyecto integra conceptos de la Unidad 4: NumPy arrays, operaciones vectorizadas, máscaras booleanas y funciones estadísticas. También reutiliza conceptos de archivos y Pandas de la Unidad 3.

---

## Contexto: ¿Qué es el NDVI?

El **NDVI** (Índice de Vegetación de Diferencia Normalizada) es un indicador que se calcula a partir de imágenes satelitales:

```
NDVI = (NIR - RED) / (NIR + RED)
```

Donde:
- **NIR** = reflectancia en infrarrojo cercano
- **RED** = reflectancia en rojo visible

**Interpretación**:
| Valor NDVI | Interpretación |
|------------|----------------|
| -1.0 a 0.0 | Agua, nubes, nieve |
| 0.0 a 0.2 | Suelo desnudo, rocas, urbano |
| 0.2 a 0.4 | Vegetación escasa o estresada |
| 0.4 a 0.6 | Vegetación moderada |
| 0.6 a 1.0 | Vegetación densa y saludable |

---

## Paso 1: Estructura de datos

**Objetivo**: Entender cómo representamos una imagen satelital como arrays NumPy.

**Concepto**: Una imagen satelital es una matriz donde cada celda (pixel) tiene valores para diferentes bandas espectrales.

**Tareas**:
1. Crear arrays NumPy simulando una imagen de 5x5 pixels
2. Cada pixel tiene valores NIR y RED (0.0 a 1.0)

**Ejemplo de código**:
```python
import numpy as np

# Simulamos una imagen 5x5
# Valores de reflectancia entre 0 y 1
np.random.seed(42)  # Para reproducibilidad

nir = np.random.uniform(0.1, 0.8, (5, 5))
red = np.random.uniform(0.05, 0.5, (5, 5))

print("Banda NIR (5x5):")
print(np.round(nir, 2))
print(f"\nForma: {nir.shape}")
```

---

## Paso 2: Cargar datos desde CSV

**Objetivo**: Crear y cargar datos de bandas espectrales desde archivos CSV.

**Tareas**:
1. Crear un CSV con columnas: fila, columna, nir, red
2. Cargar con Pandas y convertir a arrays NumPy
3. Reconstruir las matrices 2D

**Formato del CSV** (`bandas.csv`):
```csv
fila,columna,nir,red,zona
0,0,0.45,0.12,A
0,1,0.52,0.15,A
0,2,0.38,0.20,B
...
```

**Ejemplo de código**:
```python
import pandas as pd
import numpy as np

# Cargar datos
df = pd.read_csv("bandas.csv")

# Determinar dimensiones
filas = df["fila"].max() + 1
cols = df["columna"].max() + 1

# Crear matrices vacías
nir = np.zeros((filas, cols))
red = np.zeros((filas, cols))

# Llenar matrices
for _, row in df.iterrows():
    nir[row["fila"], row["columna"]] = row["nir"]
    red[row["fila"], row["columna"]] = row["red"]

print(f"Imagen cargada: {filas}x{cols} pixels")
```

---

## Paso 3: Calcular NDVI

**Objetivo**: Implementar el cálculo del NDVI de forma vectorizada.

**Tareas**:
1. Crear función `calcular_ndvi(nir, red)` que retorne la matriz NDVI
2. Manejar división por cero (cuando NIR + RED = 0)
3. Verificar que los valores estén en el rango [-1, 1]

**Ejemplo de código**:
```python
def calcular_ndvi(nir, red):
    """
    Calcula el NDVI a partir de bandas NIR y RED.
    Maneja división por cero retornando 0.
    """
    # Evitar división por cero
    denominador = nir + red
    
    # Usar np.where para manejar casos especiales
    ndvi = np.where(
        denominador != 0,
        (nir - red) / denominador,
        0  # Valor cuando denominador es 0
    )
    
    # Asegurar que esté en rango válido
    ndvi = np.clip(ndvi, -1, 1)
    
    return ndvi

# Calcular
ndvi = calcular_ndvi(nir, red)
print("NDVI calculado:")
print(np.round(ndvi, 2))
```

---

## Paso 4: Clasificar vegetación

**Objetivo**: Clasificar cada pixel según su valor de NDVI.

**Tareas**:
1. Crear función `clasificar_vegetacion(ndvi)` que retorne matriz de categorías
2. Usar np.select() o np.where() anidado
3. Contar pixels por categoría

**Ejemplo de código**:
```python
def clasificar_vegetacion(ndvi):
    """Clasifica pixels según nivel de vegetación."""
    condiciones = [
        ndvi < 0,
        (ndvi >= 0) & (ndvi < 0.2),
        (ndvi >= 0.2) & (ndvi < 0.4),
        (ndvi >= 0.4) & (ndvi < 0.6),
        ndvi >= 0.6
    ]
    
    categorias = [
        "Agua/Nubes",
        "Suelo",
        "Veg. escasa",
        "Veg. moderada",
        "Veg. densa"
    ]
    
    return np.select(condiciones, categorias, default="Sin datos")

# Clasificar
clases = clasificar_vegetacion(ndvi)
print("Clasificación:")
print(clases)
```

---

## Paso 5: Estadísticas por zona

**Objetivo**: Calcular estadísticas de NDVI agrupadas por zona geográfica.

**Tareas**:
1. Cargar o crear array de zonas (A, B, C, etc.)
2. Calcular promedio, mínimo, máximo de NDVI por zona
3. Mostrar resumen formateado

**Ejemplo de código**:
```python
def estadisticas_por_zona(ndvi, zonas):
    """Calcula estadísticas de NDVI por zona."""
    zonas_unicas = np.unique(zonas)
    
    print("=== ESTADÍSTICAS POR ZONA ===\n")
    
    for zona in zonas_unicas:
        mascara = zonas == zona
        ndvi_zona = ndvi[mascara]
        
        print(f"Zona {zona}:")
        print(f"  Pixels: {len(ndvi_zona)}")
        print(f"  NDVI promedio: {np.mean(ndvi_zona):.3f}")
        print(f"  NDVI mínimo: {np.min(ndvi_zona):.3f}")
        print(f"  NDVI máximo: {np.max(ndvi_zona):.3f}")
        print()
```

---

## Paso 6: Detectar cambios

**Objetivo**: Comparar dos imágenes NDVI de diferentes fechas para detectar cambios.

**Tareas**:
1. Cargar datos de dos fechas diferentes
2. Calcular diferencia de NDVI
3. Identificar áreas con pérdida o ganancia de vegetación

**Ejemplo de código**:
```python
def detectar_cambios(ndvi_antes, ndvi_despues, umbral=0.1):
    """
    Detecta cambios significativos en vegetación.
    
    Retorna:
    - Array con: -1 (pérdida), 0 (sin cambio), 1 (ganancia)
    """
    diferencia = ndvi_despues - ndvi_antes
    
    cambios = np.where(
        diferencia < -umbral, -1,  # Pérdida
        np.where(diferencia > umbral, 1, 0)  # Ganancia o sin cambio
    )
    
    print(f"Pixels con pérdida de vegetación: {np.sum(cambios == -1)}")
    print(f"Pixels sin cambio significativo: {np.sum(cambios == 0)}")
    print(f"Pixels con ganancia de vegetación: {np.sum(cambios == 1)}")
    
    return cambios
```

---

## Paso 7: Filtrar datos válidos

**Objetivo**: Manejar valores nulos o fuera de rango en los datos.

**Tareas**:
1. Identificar pixels con valores -999 (dato faltante) o NaN
2. Crear máscara de datos válidos
3. Recalcular estadísticas excluyendo datos inválidos

**Ejemplo de código**:
```python
def limpiar_datos(nir, red, valor_nulo=-999):
    """
    Limpia datos reemplazando valores nulos por NaN.
    Retorna arrays limpios y máscara de válidos.
    """
    # Identificar nulos
    nulos_nir = (nir == valor_nulo) | (nir < 0) | (nir > 1)
    nulos_red = (red == valor_nulo) | (red < 0) | (red > 1)
    nulos = nulos_nir | nulos_red
    
    # Copiar y limpiar
    nir_limpio = nir.copy().astype(float)
    red_limpio = red.copy().astype(float)
    
    nir_limpio[nulos] = np.nan
    red_limpio[nulos] = np.nan
    
    print(f"Pixels válidos: {np.sum(~nulos)} / {nulos.size}")
    print(f"Pixels inválidos: {np.sum(nulos)}")
    
    return nir_limpio, red_limpio, ~nulos
```

---

## Paso 8: Exportar resultados

**Objetivo**: Guardar los resultados del análisis en diferentes formatos.

**Tareas**:
1. Exportar NDVI a CSV con coordenadas
2. Exportar resumen estadístico a TXT
3. Guardar array como archivo NumPy (.npy)

**Ejemplo de código**:
```python
def exportar_resultados(ndvi, clases, nombre_base):
    """Exporta resultados a múltiples formatos."""
    
    # 1. CSV con todos los pixels
    filas, cols = ndvi.shape
    datos = []
    for i in range(filas):
        for j in range(cols):
            datos.append({
                "fila": i,
                "columna": j,
                "ndvi": round(ndvi[i, j], 4),
                "clase": clases[i, j]
            })
    
    df = pd.DataFrame(datos)
    df.to_csv(f"{nombre_base}_ndvi.csv", index=False)
    
    # 2. Array NumPy
    np.save(f"{nombre_base}_ndvi.npy", ndvi)
    
    # 3. Resumen TXT
    with open(f"{nombre_base}_resumen.txt", "w") as f:
        f.write("=== RESUMEN DE ANÁLISIS NDVI ===\n\n")
        f.write(f"Dimensiones: {filas} x {cols} pixels\n")
        f.write(f"NDVI promedio: {np.nanmean(ndvi):.3f}\n")
        f.write(f"NDVI mínimo: {np.nanmin(ndvi):.3f}\n")
        f.write(f"NDVI máximo: {np.nanmax(ndvi):.3f}\n")
    
    print(f"Archivos exportados con prefijo '{nombre_base}'")
```

---

## Paso 9: Visualización (opcional)

**Objetivo**: Crear visualización del mapa de NDVI usando matplotlib.

**Nota**: Este paso requiere `pip install matplotlib`.

**Ejemplo de código**:
```python
import matplotlib.pyplot as plt

def visualizar_ndvi(ndvi, titulo="Mapa de NDVI"):
    """Crea visualización del NDVI como mapa de calor."""
    
    plt.figure(figsize=(10, 8))
    
    # Mapa de calor
    im = plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
    plt.colorbar(im, label='NDVI')
    
    plt.title(titulo)
    plt.xlabel('Columna (pixel)')
    plt.ylabel('Fila (pixel)')
    
    plt.savefig('ndvi_mapa.png', dpi=150)
    plt.show()
    
    print("Mapa guardado como 'ndvi_mapa.png'")
```

---

## Paso 10: Programa completo

**Objetivo**: Integrar todo en un programa con menú interactivo.

**Menú del programa**:
```
╔════════════════════════════════════════════════════╗
║     ANALIZADOR DE VEGETACIÓN - NDVI                ║
╚════════════════════════════════════════════════════╝

1. Cargar datos de bandas (CSV)
2. Calcular NDVI
3. Ver estadísticas generales
4. Ver estadísticas por zona
5. Clasificar vegetación
6. Detectar cambios (comparar fechas)
7. Exportar resultados
8. Visualizar mapa (requiere matplotlib)
9. Salir

Opción: 
```

**Ejemplo de ejecución completa**:
```
Opción: 1
Archivo de bandas: imagen_enero.csv
✓ Datos cargados: 100x100 pixels

Opción: 2
✓ NDVI calculado
  Rango: [-0.15, 0.82]
  Promedio: 0.38

Opción: 5
=== CLASIFICACIÓN DE VEGETACIÓN ===
Agua/Nubes:      5 pixels (0.5%)
Suelo:          120 pixels (12.0%)
Veg. escasa:    350 pixels (35.0%)
Veg. moderada:  380 pixels (38.0%)
Veg. densa:     145 pixels (14.5%)

Opción: 4
=== ESTADÍSTICAS POR ZONA ===

Zona A (Norte):
  Pixels: 2500
  NDVI promedio: 0.45
  Vegetación predominante: Moderada

Zona B (Sur):
  Pixels: 2500
  NDVI promedio: 0.32
  Vegetación predominante: Escasa

Opción: 7
Exportando resultados...
✓ imagen_enero_ndvi.csv
✓ imagen_enero_ndvi.npy
✓ imagen_enero_resumen.txt

Opción: 9
¡Hasta luego! Análisis guardado.
```

---

## Conceptos utilizados

| Concepto | Dónde se usa |
|----------|--------------|
| **np.array** | Representar bandas como matrices |
| **Operaciones vectorizadas** | Cálculo de NDVI sin bucles |
| **np.where** | Manejar división por cero, clasificación |
| **np.select** | Clasificación con múltiples categorías |
| **Máscaras booleanas** | Filtrar por zona, datos válidos |
| **np.mean, np.min, np.max** | Estadísticas por zona |
| **np.nanmean** | Estadísticas ignorando NaN |
| **np.unique** | Obtener zonas únicas |
| **np.clip** | Limitar valores a rango válido |
| **np.save/load** | Guardar/cargar arrays |
| **Pandas** | Cargar CSV, exportar resultados |

---

## Desafíos extra

1. **Histograma de NDVI**: Crear un histograma que muestre la distribución de valores NDVI.

2. **Detección de incendios**: Investigar el índice NBR (Normalized Burn Ratio) e implementarlo.

3. **Series temporales**: Cargar imágenes de múltiples fechas y graficar la evolución del NDVI promedio.

4. **Interpolación**: Rellenar pixels con datos faltantes usando interpolación de vecinos.

5. **Segmentación**: Agrupar pixels contiguos con valores similares usando algoritmos de clustering.

6. **Área real**: Dado el tamaño del pixel en metros, calcular el área total de cada categoría en km².

7. **Formato GeoTIFF**: Investigar cómo cargar imágenes satelitales reales con la librería `rasterio`.

---

## Conexión con la Unidad anterior

Este proyecto es una evolución del **Proyecto Integrador de la Unidad 3** (Gestor de Rutas con Persistencia):

| Unidad 3 | Unidad 4 |
|----------|----------|
| Datos de puntos (ciudades) | Datos de grilla (pixels) |
| Listas/diccionarios | Arrays NumPy 2D |
| Operaciones fila por fila | Operaciones vectorizadas |
| Estadísticas con Pandas | Estadísticas con NumPy |
| Archivos CSV simples | CSV + formato NumPy (.npy) |
| Contexto: rutas de viaje | Contexto: teledetección |

Funciones reutilizables de unidades anteriores:
- Lectura/escritura de CSV → cargar bandas, exportar resultados
- Manejo de errores → archivos faltantes, datos inválidos
- Pandas DataFrames → organizar datos de pixels

La evolución conceptual:
- De trabajar con puntos discretos a trabajar con matrices de datos
- De análisis geográfico vectorial a análisis raster
- Aplicación real de NumPy en ciencias de la Tierra

---

*Fin del proyecto integrador - Unidad 4*
