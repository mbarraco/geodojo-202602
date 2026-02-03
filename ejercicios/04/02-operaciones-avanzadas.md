# Unidad 4: Operaciones Avanzadas con NumPy

Ejercicios sobre funciones estadísticas, máscaras booleanas y operaciones vectorizadas.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Funciones estadísticas básicas

---

### A1. Suma de elementos

**Enunciado**: Dado un array de poblaciones `[2890000, 1430000, 1270000, 620000]`, calculá la población total usando `np.sum()`.

**Ejemplo**:
- Salida esperada: `6210000`

---

### A2. Promedio

**Enunciado**: Calculá la latitud promedio del array `[-34.6, -31.4, -32.9, -24.8]` usando `np.mean()`.

**Ejemplo**:
- Salida esperada: `-30.925`

---

### A3. Mínimo y máximo

**Enunciado**: Encontrá la latitud más al norte (máximo) y más al sur (mínimo) del array anterior.

**Hint**: `np.min()` y `np.max()`.

---

### A4. Posición del mínimo/máximo

**Enunciado**: Encontrá el índice de la ciudad más al sur usando `np.argmin()`.

**Ejemplo**:
- Salida esperada: `0` (si Buenos Aires está en posición 0)`

---

### A5. Desviación estándar

**Enunciado**: Calculá la desviación estándar de las poblaciones para ver qué tan dispersos están los valores.

**Hint**: `np.std()`.

---

### Bloque 2: Operaciones por eje

---

### A6. Suma por columnas

**Enunciado**: Dada una matriz 3x2 de coordenadas (lat, lon), calculá la suma de cada columna (todas las latitudes, todas las longitudes).

**Hint**: `np.sum(matriz, axis=0)` suma por columnas.

---

### A7. Promedio por filas

**Enunciado**: Calculá el promedio de cada fila de la matriz anterior (promedio de lat y lon para cada ciudad).

**Hint**: `np.mean(matriz, axis=1)` promedia por filas.

---

### A8. Mínimo por columna

**Enunciado**: Encontrá la latitud mínima y longitud mínima de la matriz.

---

### A9. Diferencia entre ejes

**Enunciado**: Creá una matriz 4x3 con `np.arange(12).reshape(4,3)`. Calculá la suma total, suma por filas y suma por columnas.

---

### A10. Mantener dimensiones

**Enunciado**: Calculá el promedio por columnas de una matriz 3x4, manteniendo la forma del resultado como matriz usando `keepdims=True`.

---

### Bloque 3: Máscaras booleanas

---

### A11. Crear máscara simple

**Enunciado**: Dado un array de temperaturas `[25, 30, 15, 35, 20]`, creá una máscara booleana que indique cuáles superan 25°C.

**Ejemplo**:
- Salida esperada: `[False, True, False, True, False]`

---

### A12. Filtrar con máscara

**Enunciado**: Usando la máscara anterior, obtené solo las temperaturas mayores a 25°C.

**Ejemplo**:
- Salida esperada: `[30, 35]`

**Hint**: `array[mascara]` filtra usando la máscara.

---

### A13. Contar elementos

**Enunciado**: Contá cuántas ciudades tienen latitud menor a -30 (están más al sur).

**Ejemplo**:
- Salida esperada: `3`

**Hint**: `np.sum(mascara)` cuenta los True.

---

### A14. Máscara con múltiples condiciones

**Enunciado**: Encontrá ciudades que estén en el hemisferio sur (lat < 0) Y tengan longitud oeste de -60 (lon < -60).

---

### A15. Máscara con OR

**Enunciado**: Encontrá elementos que sean menores a -30 O mayores a -25 en un array de latitudes.

**Hint**: Usar `|` para OR entre condiciones.

---

### Bloque 4: np.where y operaciones condicionales

---

### A16. where básico

**Enunciado**: Dado un array de latitudes, usá `np.where()` para crear un array que diga "Sur" si lat < 0, o "Norte" si no.

**Hint**: `np.where(condicion, valor_si_true, valor_si_false)`.

---

### A17. where para reemplazar valores

**Enunciado**: Tenés un array de elevaciones con valores -999 que indican datos faltantes. Reemplazá los -999 por 0.

---

### A18. Obtener índices con where

**Enunciado**: Encontrá los índices donde la elevación es mayor a 200 metros.

**Hint**: `np.where(condicion)` sin los otros argumentos devuelve índices.

---

### A19. Clasificar valores

**Enunciado**: Clasificá temperaturas en "fría" (< 15), "templada" (15-25), "cálida" (> 25).

**Hint**: Usá `np.where` anidado o `np.select()`.

---

### A20. Clip de valores

**Enunciado**: Limitá un array de temperaturas para que ninguna sea menor a 0 ni mayor a 40.

**Hint**: `np.clip(array, min, max)`.

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Percentiles

**Enunciado**: Calculá los percentiles 25, 50 (mediana) y 75 de un array de elevaciones.

**Hint**: `np.percentile(arr, [25, 50, 75])`.

---

### B2. Producto acumulado

**Enunciado**: Calculá el producto acumulado de un array usando `np.cumprod()`.

---

### B3. Diferencias

**Enunciado**: Calculá las diferencias entre elementos consecutivos con `np.diff()`.

---

### B4. Ordenar array

**Enunciado**: Ordená un array de poblaciones de menor a mayor con `np.sort()`.

---

### B5. Índices de ordenamiento

**Enunciado**: Obtené los índices que ordenarían un array con `np.argsort()`.

---

### B6. Buscar valor

**Enunciado**: Usá `np.searchsorted()` para encontrar dónde insertar un valor en un array ordenado.

---

### B7. Redondeo

**Enunciado**: Redondeá coordenadas a 2 decimales con `np.round()`.

---

### B8. Funciones trigonométricas

**Enunciado**: Convertí un ángulo de grados a radianes y calculá su seno con `np.sin()`.

---

### B9. Normalizar datos

**Enunciado**: Normalizá un array para que tenga media 0 y desviación estándar 1.

---

### B10. Correlación

**Enunciado**: Calculá la correlación entre dos arrays con `np.corrcoef()`.

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Calcular NDVI

**Enunciado**: Dados arrays de valores NIR (infrarrojo cercano) y RED (rojo), calculá el NDVI usando la fórmula: `NDVI = (NIR - RED) / (NIR + RED)`. El NDVI indica vegetación: valores cercanos a 1 indican vegetación densa.

---

### C2. Distancia de Haversine

**Enunciado**: Implementá la fórmula de Haversine para calcular la distancia real entre puntos geográficos considerando la curvatura de la Tierra.

---

### C3. Matriz de covarianza

**Enunciado**: Calculá la matriz de covarianza entre latitud, longitud y elevación de un conjunto de puntos.

---

### C4. Álgebra lineal

**Enunciado**: Multiplicá dos matrices con `np.dot()` o `@`. Calculá el determinante con `np.linalg.det()`.

---

### C5. FFT básica

**Enunciado**: Investigá `np.fft.fft()` para calcular la transformada de Fourier de una señal simple.

---

*Fin de los ejercicios de la Unidad 4*
