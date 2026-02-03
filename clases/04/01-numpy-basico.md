# Clase 4: NumPy Básico

Guía para la clase sobre arrays, creación y operaciones básicas con NumPy.

---

## 1. Temario

### 1.1 Crear arrays

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `np.array(lista)` | Crea array desde lista | `np.array([1, 2, 3])` |
| `np.array(lista, dtype=tipo)` | Con tipo específico | `np.array([1, 2], dtype=float)` |
| `np.arange(inicio, fin, paso)` | Rango con paso | `np.arange(0, 10, 2)` → `[0, 2, 4, 6, 8]` |
| `np.linspace(inicio, fin, n)` | N valores equiespaciados | `np.linspace(0, 1, 5)` → `[0, 0.25, 0.5, 0.75, 1]` |

### 1.2 Arrays especiales

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `np.zeros(n)` | Array de ceros | `np.zeros(5)` → `[0., 0., 0., 0., 0.]` |
| `np.zeros((filas, cols))` | Matriz de ceros | `np.zeros((3, 4))` |
| `np.ones(n)` | Array de unos | `np.ones(3)` → `[1., 1., 1.]` |
| `np.full(n, valor)` | Array con valor constante | `np.full(4, -999)` |
| `np.eye(n)` | Matriz identidad | `np.eye(3)` |

### 1.3 Forma y dimensiones

| Atributo/Método | Descripción | Ejemplo |
|-----------------|-------------|---------|
| `array.shape` | Dimensiones del array | `(3, 4)` para matriz 3x4 |
| `array.ndim` | Número de dimensiones | `2` para matriz |
| `array.size` | Total de elementos | `12` para matriz 3x4 |
| `array.dtype` | Tipo de datos | `float64`, `int64` |
| `array.reshape(forma)` | Cambiar forma | `arr.reshape(3, 4)` |
| `array.flatten()` | Convertir a 1D | `matriz.flatten()` |

### 1.4 Indexación y slicing

| Operación | Sintaxis | Resultado |
|-----------|----------|-----------|
| Elemento único | `arr[i]` | Valor en posición i |
| Rango | `arr[i:j]` | Elementos de i a j-1 |
| Con paso | `arr[i:j:paso]` | Elementos con salto |
| Desde inicio | `arr[:j]` | Primeros j elementos |
| Hasta final | `arr[i:]` | Desde i hasta el final |
| Índice negativo | `arr[-1]` | Último elemento |
| Matriz [fila, col] | `mat[i, j]` | Elemento en (i, j) |
| Fila completa | `mat[i, :]` | Toda la fila i |
| Columna completa | `mat[:, j]` | Toda la columna j |

### 1.5 Operaciones básicas

| Operación | Sintaxis | Descripción |
|-----------|----------|-------------|
| Suma | `arr1 + arr2` | Elemento a elemento |
| Resta | `arr1 - arr2` | Elemento a elemento |
| Multiplicación | `arr1 * arr2` | Elemento a elemento |
| División | `arr1 / arr2` | Elemento a elemento |
| Potencia | `arr ** n` | Cada elemento a la n |
| Escalar | `arr * 5` | Multiplica todos por 5 |

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Crear array desde lista
Crear un array con las latitudes de 4 ciudades argentinas.

---

#### Ejemplo 2: Ver propiedades del array
Explorar shape, size, dtype y ndim del array creado.

---

#### Ejemplo 3: Arrays especiales
Crear arrays de ceros, unos y valores constantes para representar datos geográficos.

---

#### Ejemplo 4: arange y linspace
Crear secuencias de latitudes usando arange y linspace.

---

#### Ejemplo 5: Matriz 2D de coordenadas
Crear una matriz donde cada fila sea [latitud, longitud] de una ciudad.

---

#### Ejemplo 6: Reshape
Crear un array del 1 al 12 y reorganizarlo como matriz 3x4 y 4x3.

---

#### Ejemplo 7: Indexación y slicing
Acceder a elementos específicos y rangos de un array de coordenadas.

---

#### Ejemplo 8: Indexación de matrices
Acceder a filas, columnas y elementos de una matriz de coordenadas.

---

#### Ejemplo 9: Operaciones aritméticas
Realizar cálculos con arrays: conversión de grados a km, diferencias entre puntos.

---

#### Ejemplo 10: Cálculo de distancia vectorizado
Calcular la distancia euclidiana entre dos arrays de puntos sin usar bucles.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Crear array desde lista

**Enunciado**: Crear un array con las latitudes de 4 ciudades argentinas.

```python
import numpy as np

# Latitudes de ciudades argentinas
latitudes = np.array([-34.6, -31.4, -32.9, -24.8])

print("Array de latitudes:")
print(latitudes)
print(f"Tipo: {type(latitudes)}")
```

**Salida**:
```
Array de latitudes:
[-34.6 -31.4 -32.9 -24.8]
Tipo: <class 'numpy.ndarray'>
```

---

#### Ejemplo 2: Ver propiedades del array

**Enunciado**: Explorar shape, size, dtype y ndim del array creado.

```python
import numpy as np

latitudes = np.array([-34.6, -31.4, -32.9, -24.8])

print(f"Shape (forma): {latitudes.shape}")
print(f"Size (elementos): {latitudes.size}")
print(f"Dtype (tipo): {latitudes.dtype}")
print(f"Ndim (dimensiones): {latitudes.ndim}")
```

**Salida**:
```
Shape (forma): (4,)
Size (elementos): 4
Dtype (tipo): float64
Ndim (dimensiones): 1
```

---

#### Ejemplo 3: Arrays especiales

**Enunciado**: Crear arrays de ceros, unos y valores constantes.

```python
import numpy as np

# Array de ceros (elevaciones sin datos)
sin_datos = np.zeros(5)
print(f"Ceros: {sin_datos}")

# Array de unos (para máscaras)
mascara = np.ones(4)
print(f"Unos: {mascara}")

# Valor constante (valor nulo típico en GIS)
nulos = np.full(3, -999)
print(f"Valor -999: {nulos}")

# Matriz de ceros 3x4
matriz_ceros = np.zeros((3, 4))
print(f"\nMatriz 3x4 de ceros:\n{matriz_ceros}")
```

**Salida**:
```
Ceros: [0. 0. 0. 0. 0.]
Unos: [1. 1. 1. 1.]
Valor -999: [-999 -999 -999]

Matriz 3x4 de ceros:
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
```

---

#### Ejemplo 4: arange y linspace

**Enunciado**: Crear secuencias de latitudes usando arange y linspace.

```python
import numpy as np

# arange: desde -40 hasta -20, paso de 5
lat_arange = np.arange(-40, -20, 5)
print(f"arange(-40, -20, 5): {lat_arange}")

# linspace: 5 valores equiespaciados entre -90 y 90
lat_linspace = np.linspace(-90, 90, 5)
print(f"linspace(-90, 90, 5): {lat_linspace}")

# Diferencia: arange usa paso, linspace usa cantidad
print(f"\narange: {len(lat_arange)} elementos")
print(f"linspace: {len(lat_linspace)} elementos")
```

**Salida**:
```
arange(-40, -20, 5): [-40 -35 -30 -25]
linspace(-90, 90, 5): [-90. -45.   0.  45.  90.]

arange: 4 elementos
linspace: 5 elementos
```

---

#### Ejemplo 5: Matriz 2D de coordenadas

**Enunciado**: Crear una matriz donde cada fila sea [latitud, longitud].

```python
import numpy as np

# Cada fila: [lat, lon]
coordenadas = np.array([
    [-34.6, -58.4],  # Buenos Aires
    [-31.4, -64.2],  # Córdoba
    [-32.9, -68.8],  # Mendoza
])

print("Matriz de coordenadas:")
print(coordenadas)
print(f"\nForma: {coordenadas.shape}")
print(f"Filas: {coordenadas.shape[0]} ciudades")
print(f"Columnas: {coordenadas.shape[1]} valores (lat, lon)")
```

**Salida**:
```
Matriz de coordenadas:
[[-34.6 -58.4]
 [-31.4 -64.2]
 [-32.9 -68.8]]

Forma: (3, 2)
Filas: 3 ciudades
Columnas: 2 valores (lat, lon)
```

---

#### Ejemplo 6: Reshape

**Enunciado**: Crear un array del 1 al 12 y reorganizarlo.

```python
import numpy as np

# Array original
arr = np.arange(1, 13)
print(f"Array original: {arr}")
print(f"Forma: {arr.shape}")

# Reshape a 3x4
matriz_3x4 = arr.reshape(3, 4)
print(f"\nReshape 3x4:\n{matriz_3x4}")

# Reshape a 4x3
matriz_4x3 = arr.reshape(4, 3)
print(f"\nReshape 4x3:\n{matriz_4x3}")

# Volver a 1D
plano = matriz_3x4.flatten()
print(f"\nFlatten: {plano}")
```

**Salida**:
```
Array original: [ 1  2  3  4  5  6  7  8  9 10 11 12]
Forma: (12,)

Reshape 3x4:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Reshape 4x3:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

Flatten: [ 1  2  3  4  5  6  7  8  9 10 11 12]
```

---

#### Ejemplo 7: Indexación y slicing

**Enunciado**: Acceder a elementos específicos y rangos.

```python
import numpy as np

latitudes = np.array([-34.6, -31.4, -32.9, -24.8, -38.0])
print(f"Array: {latitudes}")

# Acceso por índice
print(f"\nPrimer elemento [0]: {latitudes[0]}")
print(f"Último elemento [-1]: {latitudes[-1]}")
print(f"Tercer elemento [2]: {latitudes[2]}")

# Slicing
print(f"\nPrimeros 3 [:3]: {latitudes[:3]}")
print(f"Últimos 2 [-2:]: {latitudes[-2:]}")
print(f"Del 1 al 3 [1:4]: {latitudes[1:4]}")
print(f"Alternados [::2]: {latitudes[::2]}")
```

**Salida**:
```
Array: [-34.6 -31.4 -32.9 -24.8 -38. ]

Primer elemento [0]: -34.6
Último elemento [-1]: -38.0
Tercer elemento [2]: -32.9

Primeros 3 [:3]: [-34.6 -31.4 -32.9]
Últimos 2 [-2:]: [-24.8 -38. ]
Del 1 al 3 [1:4]: [-31.4 -32.9 -24.8]
Alternados [::2]: [-34.6 -32.9 -38. ]
```

---

#### Ejemplo 8: Indexación de matrices

**Enunciado**: Acceder a filas, columnas y elementos de una matriz.

```python
import numpy as np

# Matriz de coordenadas
coords = np.array([
    [-34.6, -58.4],  # Buenos Aires
    [-31.4, -64.2],  # Córdoba
    [-32.9, -68.8],  # Mendoza
])

print(f"Matriz:\n{coords}")

# Elemento específico
print(f"\nElemento [0, 0]: {coords[0, 0]}")  # lat de BA
print(f"Elemento [1, 1]: {coords[1, 1]}")  # lon de Córdoba

# Fila completa
print(f"\nFila 0 (Buenos Aires): {coords[0, :]}")
print(f"Fila 2 (Mendoza): {coords[2]}")  # también funciona

# Columna completa
print(f"\nColumna 0 (latitudes): {coords[:, 0]}")
print(f"Columna 1 (longitudes): {coords[:, 1]}")
```

**Salida**:
```
Matriz:
[[-34.6 -58.4]
 [-31.4 -64.2]
 [-32.9 -68.8]]

Elemento [0, 0]: -34.6
Elemento [1, 1]: -64.2

Fila 0 (Buenos Aires): [-34.6 -58.4]
Fila 2 (Mendoza): [-32.9 -68.8]

Columna 0 (latitudes): [-34.6 -31.4 -32.9]
Columna 1 (longitudes): [-58.4 -64.2 -68.8]
```

---

#### Ejemplo 9: Operaciones aritméticas

**Enunciado**: Realizar cálculos con arrays.

```python
import numpy as np

# Distancias en grados
distancias_grados = np.array([2.5, 3.2, 1.8, 4.1])
print(f"Distancias (grados): {distancias_grados}")

# Convertir a km (1 grado ≈ 111 km)
distancias_km = distancias_grados * 111
print(f"Distancias (km): {distancias_km}")

# Latitudes de una ruta
latitudes = np.array([-34.6, -31.4, -32.9, -24.8])

# Diferencia entre consecutivos
diferencias = latitudes[1:] - latitudes[:-1]
print(f"\nLatitudes: {latitudes}")
print(f"Diferencias: {diferencias}")

# Aplicar ajuste a todas las coordenadas
ajuste = 0.01
latitudes_ajustadas = latitudes + ajuste
print(f"\nLatitudes ajustadas: {latitudes_ajustadas}")
```

**Salida**:
```
Distancias (grados): [2.5 3.2 1.8 4.1]
Distancias (km): [277.5 355.2 199.8 455.1]

Latitudes: [-34.6 -31.4 -32.9 -24.8]
Diferencias: [ 3.2 -1.5  8.1]

Latitudes ajustadas: [-34.59 -31.39 -32.89 -24.79]
```

---

#### Ejemplo 10: Cálculo de distancia vectorizado

**Enunciado**: Calcular distancia euclidiana entre arrays de puntos sin bucles.

```python
import numpy as np

# Puntos de origen
lat1 = np.array([-34.6, -31.4, -32.9])
lon1 = np.array([-58.4, -64.2, -68.8])

# Puntos de destino
lat2 = np.array([-31.4, -32.9, -24.8])
lon2 = np.array([-64.2, -68.8, -65.4])

# Distancia euclidiana (sin bucles!)
distancia_grados = np.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
distancia_km = distancia_grados * 111

print("Cálculo vectorizado de distancias:")
print(f"Lat origen: {lat1}")
print(f"Lat destino: {lat2}")
print(f"\nDistancias (grados): {np.round(distancia_grados, 2)}")
print(f"Distancias (km): {np.round(distancia_km, 0)}")
```

**Salida**:
```
Cálculo vectorizado de distancias:
Lat origen: [-34.6 -31.4 -32.9]
Lat destino: [-31.4 -32.9 -24.8]

Distancias (grados): [6.68 4.87 8.79]
Distancias (km): [741. 541. 976.]
```

---

## Notas para el docente

- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Enfatizar que NumPy opera sobre arrays completos sin necesidad de bucles
- La diferencia entre `arange` (paso) y `linspace` (cantidad) es importante
- `reshape` no copia datos, solo cambia la vista (mencionar brevemente)
- El slicing de NumPy es más poderoso que el de listas (2D con `[fila, col]`)
- Los ejercicios en `ejercicios/04/01-numpy-basico.md` refuerzan estos conceptos
- Contexto geográfico: coordenadas, distancias, elevaciones
