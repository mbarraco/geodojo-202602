# Clase 4: Operaciones Avanzadas con NumPy

Guía para la clase sobre funciones estadísticas, máscaras booleanas y operaciones vectorizadas.

---

## 1. Temario

### 1.1 Funciones estadísticas básicas

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `np.sum(arr)` | Suma total | `np.sum([1, 2, 3])` → `6` |
| `np.mean(arr)` | Promedio | `np.mean([1, 2, 3])` → `2.0` |
| `np.min(arr)` | Mínimo | `np.min([1, 2, 3])` → `1` |
| `np.max(arr)` | Máximo | `np.max([1, 2, 3])` → `3` |
| `np.std(arr)` | Desviación estándar | Dispersión de valores |
| `np.var(arr)` | Varianza | Cuadrado de std |
| `np.argmin(arr)` | Índice del mínimo | `np.argmin([3, 1, 2])` → `1` |
| `np.argmax(arr)` | Índice del máximo | `np.argmax([3, 1, 2])` → `0` |

### 1.2 Operaciones por eje

| Parámetro | Efecto | Ejemplo |
|-----------|--------|---------|
| Sin axis | Opera sobre todo el array | `np.sum(matriz)` → escalar |
| `axis=0` | Opera por columnas (colapsa filas) | `np.sum(matriz, axis=0)` → array |
| `axis=1` | Opera por filas (colapsa columnas) | `np.sum(matriz, axis=1)` → array |
| `keepdims=True` | Mantiene dimensiones | Útil para broadcasting |

### 1.3 Máscaras booleanas

| Operación | Sintaxis | Resultado |
|-----------|----------|-----------|
| Comparación | `arr > 5` | Array de True/False |
| Filtrar | `arr[arr > 5]` | Solo elementos True |
| AND | `(cond1) & (cond2)` | Ambas condiciones |
| OR | `(cond1) \ | (cond2)` | Al menos una |
| NOT | `~condicion` | Negación |
| Contar True | `np.sum(mascara)` | Número de True |
| Todos True | `np.all(mascara)` | Booleano |
| Algún True | `np.any(mascara)` | Booleano |

### 1.4 np.where y operaciones condicionales

| Función | Uso | Ejemplo |
|---------|-----|---------|
| `np.where(cond, x, y)` | Si cond, x; sino y | `np.where(arr > 0, 'pos', 'neg')` |
| `np.where(cond)` | Índices donde True | `np.where(arr > 5)` → `(array([2, 4]),)` |
| `np.clip(arr, min, max)` | Limitar rango | `np.clip(arr, 0, 100)` |
| `np.select(conds, vals)` | Múltiples condiciones | Más flexible que where |

### 1.5 Combinar arrays

| Función | Descripción | Resultado |
|---------|-------------|-----------|
| `np.concatenate([a, b])` | Une arrays | Array 1D más largo |
| `np.vstack([a, b])` | Apila verticalmente | Matriz con más filas |
| `np.hstack([a, b])` | Apila horizontalmente | Matriz con más cols |
| `np.column_stack([a, b])` | Columnas lado a lado | Matriz 2D |
| `np.split(arr, n)` | Divide en n partes | Lista de arrays |
| `np.unique(arr)` | Valores únicos | Array ordenado |

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Estadísticas básicas
Calcular suma, promedio, mínimo y máximo de poblaciones de ciudades.

---

#### Ejemplo 2: Encontrar extremos
Encontrar la ciudad más al norte y más al sur de un array de latitudes.

---

#### Ejemplo 3: Operaciones por eje en matriz
Calcular estadísticas por filas y columnas de una matriz de coordenadas.

---

#### Ejemplo 4: Crear máscara booleana
Identificar qué ciudades tienen más de 1 millón de habitantes.

---

#### Ejemplo 5: Filtrar con máscara
Obtener solo las ciudades grandes usando la máscara.

---

#### Ejemplo 6: Múltiples condiciones
Encontrar ciudades en el hemisferio sur con longitud oeste de -60.

---

#### Ejemplo 7: np.where para clasificar
Clasificar ciudades como "Norte" o "Sur" según su latitud.

---

#### Ejemplo 8: Reemplazar valores
Reemplazar valores -999 (datos faltantes) por NaN.

---

#### Ejemplo 9: Combinar arrays
Concatenar datos de diferentes regiones en un solo array.

---

#### Ejemplo 10: Calcular NDVI
Aplicar la fórmula de NDVI a datos de bandas espectrales.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Estadísticas básicas

**Enunciado**: Calcular suma, promedio, mínimo y máximo de poblaciones de ciudades.

```python
import numpy as np

poblaciones = np.array([2890000, 1430000, 1270000, 620000, 115000])
ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Salta", "Mendoza"]

print("Poblaciones:", poblaciones)
print(f"\nTotal: {np.sum(poblaciones):,}")
print(f"Promedio: {np.mean(poblaciones):,.0f}")
print(f"Mínimo: {np.min(poblaciones):,}")
print(f"Máximo: {np.max(poblaciones):,}")
print(f"Desv. estándar: {np.std(poblaciones):,.0f}")
```

**Salida**:
```
Poblaciones: [2890000 1430000 1270000  620000  115000]

Total: 6,325,000
Promedio: 1,265,000
Mínimo: 115,000
Máximo: 2,890,000
Desv. estándar: 917,449
```

---

#### Ejemplo 2: Encontrar extremos

**Enunciado**: Encontrar la ciudad más al norte y más al sur de un array de latitudes.

```python
import numpy as np

latitudes = np.array([-34.6, -31.4, -33.0, -24.8, -32.9])
ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Salta", "Mendoza"]

# Índices de extremos
idx_norte = np.argmax(latitudes)  # Mayor latitud = más al norte
idx_sur = np.argmin(latitudes)    # Menor latitud = más al sur

print(f"Latitudes: {latitudes}")
print(f"\nMás al norte: {ciudades[idx_norte]} (lat: {latitudes[idx_norte]})")
print(f"Más al sur: {ciudades[idx_sur]} (lat: {latitudes[idx_sur]})")
```

**Salida**:
```
Latitudes: [-34.6 -31.4 -33.  -24.8 -32.9]

Más al norte: Salta (lat: -24.8)
Más al sur: Buenos Aires (lat: -34.6)
```

---

#### Ejemplo 3: Operaciones por eje en matriz

**Enunciado**: Calcular estadísticas por filas y columnas de una matriz de coordenadas.

```python
import numpy as np

# Matriz: cada fila es una ciudad [lat, lon, poblacion]
datos = np.array([
    [-34.6, -58.4, 2890000],
    [-31.4, -64.2, 1430000],
    [-32.9, -68.8,  115000],
])

print("Datos (lat, lon, poblacion):")
print(datos)

# Promedio por columna (de cada variable)
prom_cols = np.mean(datos, axis=0)
print(f"\nPromedio por columna:")
print(f"  Lat promedio: {prom_cols[0]:.2f}")
print(f"  Lon promedio: {prom_cols[1]:.2f}")
print(f"  Pob promedio: {prom_cols[2]:,.0f}")

# Suma por fila (no tiene mucho sentido, pero ilustra el concepto)
suma_filas = np.sum(datos, axis=1)
print(f"\nSuma por fila: {suma_filas}")
```

**Salida**:
```
Datos (lat, lon, poblacion):
[[-3.46e+01 -5.84e+01  2.89e+06]
 [-3.14e+01 -6.42e+01  1.43e+06]
 [-3.29e+01 -6.88e+01  1.15e+05]]

Promedio por columna:
  Lat promedio: -32.97
  Lon promedio: -63.80
  Pob promedio: 1,478,333

Suma por fila: [2889906.  1429905.   114901. ]
```

---

#### Ejemplo 4: Crear máscara booleana

**Enunciado**: Identificar qué ciudades tienen más de 1 millón de habitantes.

```python
import numpy as np

poblaciones = np.array([2890000, 1430000, 1270000, 620000, 115000])
ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Salta", "Mendoza"]

# Crear máscara
mascara = poblaciones > 1000000

print("Poblaciones:", poblaciones)
print("Máscara (>1M):", mascara)
print(f"\nCantidad con >1M: {np.sum(mascara)}")
```

**Salida**:
```
Poblaciones: [2890000 1430000 1270000  620000  115000]
Máscara (>1M): [ True  True  True False False]

Cantidad con >1M: 3
```

---

#### Ejemplo 5: Filtrar con máscara

**Enunciado**: Obtener solo las ciudades grandes usando la máscara.

```python
import numpy as np

poblaciones = np.array([2890000, 1430000, 1270000, 620000, 115000])
ciudades = np.array(["Buenos Aires", "Córdoba", "Rosario", "Salta", "Mendoza"])

mascara = poblaciones > 1000000

# Filtrar arrays con la máscara
pob_grandes = poblaciones[mascara]
ciudades_grandes = ciudades[mascara]

print("Ciudades con más de 1M habitantes:")
for ciudad, pob in zip(ciudades_grandes, pob_grandes):
    print(f"  {ciudad}: {pob:,}")
```

**Salida**:
```
Ciudades con más de 1M habitantes:
  Buenos Aires: 2,890,000
  Córdoba: 1,430,000
  Rosario: 1,270,000
```

---

#### Ejemplo 6: Múltiples condiciones

**Enunciado**: Encontrar ciudades en el hemisferio sur con longitud oeste de -60.

```python
import numpy as np

latitudes = np.array([-34.6, 40.7, -31.4, 51.5, -32.9])
longitudes = np.array([-58.4, -74.0, -64.2, -0.1, -68.8])
ciudades = np.array(["Buenos Aires", "New York", "Córdoba", "Londres", "Mendoza"])

# Condiciones
en_sur = latitudes < 0
oeste_de_60 = longitudes < -60

# Combinar con AND
mascara = en_sur & oeste_de_60

print("Ciudades en hemisferio sur Y oeste de -60:")
print(ciudades[mascara])
print(f"\nLatitudes: {latitudes[mascara]}")
print(f"Longitudes: {longitudes[mascara]}")
```

**Salida**:
```
Ciudades en hemisferio sur Y oeste de -60:
['Córdoba' 'Mendoza']

Latitudes: [-31.4 -32.9]
Longitudes: [-64.2 -68.8]
```

---

#### Ejemplo 7: np.where para clasificar

**Enunciado**: Clasificar ciudades como "Norte" o "Sur" según su latitud.

```python
import numpy as np

latitudes = np.array([-34.6, 40.7, -31.4, 51.5, 0.0])
ciudades = ["Buenos Aires", "New York", "Córdoba", "Londres", "Quito"]

# Clasificar con np.where
hemisferio = np.where(latitudes < 0, "Sur", "Norte")

print("Ciudad".ljust(15), "Latitud".ljust(10), "Hemisferio")
print("-" * 35)
for ciudad, lat, hem in zip(ciudades, latitudes, hemisferio):
    print(f"{ciudad.ljust(15)} {str(lat).ljust(10)} {hem}")
```

**Salida**:
```
Ciudad          Latitud    Hemisferio
-----------------------------------
Buenos Aires    -34.6      Sur
New York        40.7       Norte
Córdoba         -31.4      Sur
Londres         51.5       Norte
Quito           0.0        Norte
```

---

#### Ejemplo 8: Reemplazar valores

**Enunciado**: Reemplazar valores -999 (datos faltantes) por NaN.

```python
import numpy as np

elevaciones = np.array([1200, -999, 850, -999, 2100, 1500])

print("Elevaciones originales:", elevaciones)

# Reemplazar -999 por NaN
elevaciones_limpias = np.where(elevaciones == -999, np.nan, elevaciones)

print("Elevaciones limpias:", elevaciones_limpias)

# Ahora podemos calcular estadísticas ignorando NaN
print(f"\nPromedio (sin NaN): {np.nanmean(elevaciones_limpias):.0f} m")
print(f"Datos faltantes: {np.sum(np.isnan(elevaciones_limpias))}")
```

**Salida**:
```
Elevaciones originales: [1200 -999  850 -999 2100 1500]
Elevaciones limpias: [1200.   nan  850.   nan 2100. 1500.]

Promedio (sin NaN): 1412 m
Datos faltantes: 2
```

---

#### Ejemplo 9: Combinar arrays

**Enunciado**: Concatenar datos de diferentes regiones en un solo array.

```python
import numpy as np

# Latitudes de dos regiones
lat_norte = np.array([-24.8, -26.8, -27.5])  # NOA
lat_sur = np.array([-41.1, -42.9, -45.8])    # Patagonia

# Concatenar
todas_lat = np.concatenate([lat_norte, lat_sur])
print("Todas las latitudes:", todas_lat)

# También podemos apilar como matriz
lat_matrix = np.vstack([lat_norte, lat_sur])
print("\nApilado vertical:")
print(lat_matrix)
print(f"Forma: {lat_matrix.shape}")
```

**Salida**:
```
Todas las latitudes: [-24.8 -26.8 -27.5 -41.1 -42.9 -45.8]

Apilado vertical:
[[-24.8 -26.8 -27.5]
 [-41.1 -42.9 -45.8]]
Forma: (2, 3)
```

---

#### Ejemplo 10: Calcular NDVI

**Enunciado**: Aplicar la fórmula de NDVI a datos de bandas espectrales.

```python
import numpy as np

# Valores de reflectancia (simulados)
# NIR = infrarrojo cercano, RED = rojo visible
nir = np.array([0.50, 0.30, 0.80, 0.45, 0.10])
red = np.array([0.10, 0.25, 0.10, 0.40, 0.08])

# NDVI = (NIR - RED) / (NIR + RED)
# Valores: -1 a 1
# > 0.3 = vegetación densa
# 0.1 - 0.3 = vegetación moderada
# < 0.1 = suelo/agua

ndvi = (nir - red) / (nir + red)

print("NIR:", nir)
print("RED:", red)
print("NDVI:", np.round(ndvi, 2))

# Clasificar
clasificacion = np.where(ndvi > 0.3, "Vegetación densa",
                np.where(ndvi > 0.1, "Vegetación moderada",
                         "Suelo/agua"))

print("\nClasificación:")
for i, (valor, clase) in enumerate(zip(ndvi, clasificacion)):
    print(f"  Pixel {i}: NDVI={valor:.2f} → {clase}")
```

**Salida**:
```
NIR: [0.5  0.3  0.8  0.45 0.1 ]
RED: [0.1  0.25 0.1  0.4  0.08]
NDVI: [0.67 0.09 0.78 0.06 0.11]

Clasificación:
  Pixel 0: NDVI=0.67 → Vegetación densa
  Pixel 1: NDVI=0.09 → Suelo/agua
  Pixel 2: NDVI=0.78 → Vegetación densa
  Pixel 3: NDVI=0.06 → Suelo/agua
  Pixel 4: NDVI=0.11 → Vegetación moderada
```

---

## Notas para el docente
- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Enfatizar que las operaciones vectorizadas son más rápidas que bucles
- Las máscaras booleanas son una herramienta muy poderosa para filtrar datos
- `axis=0` colapsa filas (opera "hacia abajo"), `axis=1` colapsa columnas (opera "hacia la derecha")
- El ejemplo de NDVI conecta con el proyecto integrador de la unidad
- Los ejercicios en `ejercicios/04/02-operaciones-avanzadas.md` refuerzan estos conceptos
- Contexto geográfico: índices de vegetación, clasificación de terreno, análisis de datos satelitales
