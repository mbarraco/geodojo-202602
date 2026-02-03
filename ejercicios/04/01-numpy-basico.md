# Unidad 4: NumPy Básico

Ejercicios sobre arrays, creación y operaciones básicas con NumPy.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Crear arrays

---

### A1. Primer array

**Enunciado**: Importá NumPy con el alias `np` y creá un array con las latitudes de tres ciudades: -34.6, -31.4, -32.9.

**Ejemplo**:
- Salida esperada: `array([-34.6, -31.4, -32.9])`

**Hint**: `import numpy as np` y luego `np.array([...])`.

---

### A2. Array de enteros

**Enunciado**: Creá un array con las poblaciones de tres ciudades: 2890000, 1430000, 1270000. Verificá que el tipo de dato sea entero.

**Ejemplo**:
- Salida esperada:
  ```
  array([2890000, 1430000, 1270000])
  - Tipo: `int64`
  ```

**Hint**: Usá `array.dtype` para ver el tipo.

---

### A3. Array con tipo específico

**Enunciado**: Creá el mismo array de poblaciones pero forzando el tipo a `float64`.

**Ejemplo**:
- Salida esperada: `array([2890000., 1430000., 1270000.])`

**Hint**: `np.array([...], dtype=np.float64)` o `dtype=float`.

---

### A4. Array desde rango

**Enunciado**: Creá un array con los números del 0 al 9 usando `np.arange()`.

**Ejemplo**:
- Salida esperada: `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])`

---

### A5. Array con paso

**Enunciado**: Creá un array con latitudes desde -40 hasta -20 con paso de 5 grados.

**Ejemplo**:
- Salida esperada: `array([-40, -35, -30, -25, -20])`

**Hint**: `np.arange(inicio, fin, paso)`. El fin no se incluye.

---

### Bloque 2: Forma y dimensiones

---

### A6. Ver forma del array

**Enunciado**: Creá un array con 6 elementos y mostrá su forma (shape).

**Ejemplo**:
- Salida esperada: `(6,)`

**Hint**: `array.shape` retorna una tupla con las dimensiones.

---

### A7. Array 2D (matriz)

**Enunciado**: Creá una matriz de 2x3 con coordenadas de dos puntos: `[[-34.6, -58.4], [-31.4, -64.2], [-32.9, -68.8]]`. Mostrá su forma.

**Ejemplo**:
- Salida esperada: `(3, 2)`

---

### A8. Reshape

**Enunciado**: Creá un array del 1 al 12 y transformalo en una matriz de 3x4 usando `reshape()`.

**Ejemplo**:
- Salida esperada:
  ```
  array([[ 1,  2,  3,  4],
  [ 5,  6,  7,  8],
  [ 9, 10, 11, 12]])
  ```

---

### A9. Flatten

**Enunciado**: Tomá la matriz del ejercicio anterior y convertila de vuelta a un array 1D usando `flatten()`.

**Ejemplo**:
- Salida esperada: `array([ 1,  2,  3, ..., 12])`

---

### A10. Número de elementos

**Enunciado**: Creá una matriz de 4x5 y mostrá el número total de elementos con `size`.

**Ejemplo**:
- Salida esperada: `20`

---

### Bloque 3: Arrays especiales

---

### A11. Array de ceros

**Enunciado**: Creá un array de 5 ceros que representará valores de elevación sin datos.

**Ejemplo**:
- Salida esperada: `array([0., 0., 0., 0., 0.])`

**Hint**: `np.zeros(5)`.

---

### A12. Matriz de ceros

**Enunciado**: Creá una matriz de 3x4 de ceros.

**Ejemplo**:
- Salida esperada: `matriz de ceros con forma (3, 4)`

**Hint**: `np.zeros((3, 4))` - notar los paréntesis dobles.

---

### A13. Array de unos

**Enunciado**: Creá un array de 10 unos usando `np.ones()`.

**Ejemplo**:
- Salida esperada: `array([1., 1., 1., ..., 1.])`

---

### A14. Array con linspace

**Enunciado**: Creá un array con 5 valores equiespaciados entre -90 (polo sur) y 90 (polo norte).

**Ejemplo**:
- Salida esperada: `array([-90., -45.,   0.,  45.,  90.])`

**Hint**: `np.linspace(inicio, fin, cantidad)`.

---

### A15. Array de valores constantes

**Enunciado**: Creá un array de 6 elementos todos con el valor -999 (valor típico para datos faltantes en geografía).

**Ejemplo**:
- Salida esperada: `array([-999, -999, -999, -999, -999, -999])`

**Hint**: `np.full(6, -999)` o `np.ones(6) * -999`.

---

### Bloque 4: Indexación y slicing

---

### A16. Acceder a elemento

**Enunciado**: Dado un array de latitudes `[-34.6, -31.4, -32.9, -24.8, -38.0]`, obtené la latitud del tercer elemento (índice 2).

**Ejemplo**:
- Salida esperada: `-32.9`

---

### A17. Slicing básico

**Enunciado**: Del array anterior, obtené los primeros 3 elementos.

**Ejemplo**:
- Salida esperada: `array([-34.6, -31.4, -32.9])`

**Hint**: `array[0:3]` o `array[:3]`.

---

### A18. Slicing con paso

**Enunciado**: Del array de latitudes, obtené elementos alternados (posiciones 0, 2, 4).

**Ejemplo**:
- Salida esperada: `array([-34.6, -32.9, -38.0])`

**Hint**: `array[::2]` - paso de 2.

---

### A19. Índices negativos

**Enunciado**: Obtené el último elemento y los últimos 3 elementos del array.

**Hint**: `array[-1]` y `array[-3:]`.

---

### A20. Modificar elemento

**Enunciado**: Creá un array de ceros de tamaño 5. Modificá el elemento del medio (índice 2) para que valga 100.

**Ejemplo**:
- Salida esperada: `array([  0.,   0., 100.,   0.,   0.])`

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Array de números aleatorios

**Enunciado**: Generá un array de 10 latitudes aleatorias entre -55 y -20 (rango de Argentina).

**Hint**: `np.random.uniform(-55, -20, 10)`.

---

### B2. Copiar array

**Enunciado**: Creá una copia independiente de un array usando `copy()`. Modificá la copia y verificá que el original no cambió.

---

### B3. Array de coordenadas estructurado

**Enunciado**: Creá una matriz de 5x2 donde cada fila sea [latitud, longitud] de una ciudad.

---

### B4. Transponer matriz

**Enunciado**: Creá una matriz 3x2 y transponela a 2x3 usando `.T`.

---

### B5. Concatenar arrays

**Enunciado**: Tenés dos arrays de latitudes de diferentes regiones. Concaténalos en uno solo con `np.concatenate()`.

---

### B6. Apilar arrays

**Enunciado**: Tenés arrays separados de lat y lon. Apilalos verticalmente con `np.vstack()` y horizontalmente con `np.hstack()`.

---

### B7. Array identidad

**Enunciado**: Creá una matriz identidad 4x4 con `np.eye()`.

---

### B8. Diagonales

**Enunciado**: Creá una matriz y extraé su diagonal con `np.diag()`.

---

### B9. Repetir array

**Enunciado**: Repetí un array [1, 2, 3] tres veces con `np.tile()`.

---

### B10. Meshgrid

**Enunciado**: Creá una grilla de coordenadas usando `np.meshgrid()` para cubrir un área rectangular.

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Matriz de distancias

**Enunciado**: Dado un array de N puntos (lat, lon), creá una matriz NxN donde cada elemento [i,j] sea la distancia entre el punto i y el punto j.

---

### C2. Broadcasting avanzado

**Enunciado**: Investigá cómo funciona el broadcasting de NumPy. Creá un ejemplo donde sumes un array 1D a cada fila de una matriz 2D.

---

### C3. Memoria y vistas

**Enunciado**: Investigá la diferencia entre una vista (slice) y una copia en NumPy. Demostrá cómo un slice comparte memoria con el array original.

---

### C4. Tipos de datos personalizados

**Enunciado**: Creá un array estructurado con campos "nombre" (string), "lat" (float) y "lon" (float) usando `np.dtype`.

---

### C5. Guardar y cargar arrays

**Enunciado**: Guardá un array a archivo con `np.save()` y cargalo con `np.load()`. Probá también con `np.savetxt()` para formato texto.

---

*Fin de los ejercicios de la Unidad 4*
