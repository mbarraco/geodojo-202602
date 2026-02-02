# Unidad 2: Estructuras de datos y control de flujo

Ejercicios sobre listas, tuplas, diccionarios, condicionales y bucles.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Listas básicas

---

### A1. Lista de ciudades

**Enunciado**: Creá una lista llamada `ciudades` que contenga los nombres: "Buenos Aires", "Córdoba", "Rosario". Mostrala por pantalla.

**Ejemplo**:
- Salida esperada: `['Buenos Aires', 'Córdoba', 'Rosario']`

**Hint**: Las listas se crean con corchetes: `[elemento1, elemento2, ...]`

---

### A2. Coordenadas en lista

**Enunciado**: Creá una lista llamada `coordenadas` con los valores -34.6, -58.4 (latitud y longitud de Buenos Aires). Mostrá la lista completa.

**Ejemplo**:
- Salida esperada: `[-34.6, -58.4]`

---

### A3. Acceso por índice

**Enunciado**: Dada la lista `provincias = ["Mendoza", "Salta", "Tucumán", "Jujuy"]`, mostrá el primer elemento y el último elemento.

**Ejemplo**:
- Salida esperada:
  ```
  Mendoza
  Jujuy
  ```

**Hint**: El primer elemento tiene índice 0, el último tiene índice -1.

---

### A4. Longitud de una lista

**Enunciado**: Dada la lista `altitudes = [6962, 6893, 6779, 6720, 6658]` (alturas de los 5 cerros más altos de Argentina), mostrá cuántos elementos tiene usando `len()`.

**Ejemplo**:
- Salida esperada: `5`

---

### A5. Agregar elementos

**Enunciado**: Creá una lista vacía llamada `capitales`. Agregá "La Plata", "Córdoba" y "Santa Fe" usando el método `append()`. Mostrá la lista final.

**Ejemplo**:
- Salida esperada: `['La Plata', 'Córdoba', 'Santa Fe']`

**Hint**: Usá `lista.append(elemento)` para agregar al final.

---

### Bloque 2: Tuplas y diccionarios

---

### A6. Coordenada como tupla

**Enunciado**: Creá una tupla llamada `punto` con la latitud y longitud de Ushuaia: (-54.8, -68.3). Mostrá la tupla y luego intentá cambiar el primer valor (observá qué error aparece).

**Ejemplo**:
- Salida esperada: `(-54.8, -68.3)`
- Error al modificar: `TypeError`

**Hint**: Las tuplas se crean con paréntesis y son inmutables.

---

### A7. Desempaquetar tupla

**Enunciado**: Dada la tupla `ubicacion = ("Mendoza", -32.89, -68.83)`, desempaquetá sus valores en tres variables: `ciudad`, `lat`, `lon`. Mostrá cada variable.

**Ejemplo**:
- Salida esperada:
  ```
  Mendoza
  -32.89
  -68.83
  ```

**Hint**: Usá `var1, var2, var3 = tupla` para desempaquetar.

---

### A8. Diccionario de ciudad

**Enunciado**: Creá un diccionario llamado `buenos_aires` con las claves "nombre", "latitud" y "longitud", con los valores correspondientes. Mostrá el diccionario completo.

**Ejemplo**:
- Salida esperada: `{'nombre': 'Buenos Aires', 'latitud': -34.6, 'longitud': -58.4}`

**Hint**: Los diccionarios se crean con llaves: `{clave: valor, ...}`

---

### A9. Acceder a valores del diccionario

**Enunciado**: Dado el diccionario `cerro = {"nombre": "Aconcagua", "altura": 6962, "provincia": "Mendoza"}`, mostrá el nombre y la altura accediendo por clave.

**Ejemplo**:
- Salida esperada:
  ```
  Aconcagua
  6962
  ```

**Hint**: Usá `diccionario["clave"]` para acceder.

---

### A10. Agregar clave al diccionario

**Enunciado**: Dado el diccionario `pais = {"nombre": "Argentina", "capital": "Buenos Aires"}`, agregá una nueva clave "poblacion" con el valor 45000000. Mostrá el diccionario actualizado.

**Ejemplo**:
- Salida esperada: `{'nombre': 'Argentina', 'capital': 'Buenos Aires', 'poblacion': 45000000}`

**Hint**: Usá `diccionario["nueva_clave"] = valor` para agregar.

---

### Bloque 3: Condicionales

---

### A11. Hemisferio norte o sur

**Enunciado**: Dada una variable `latitud = -34.6`, usá un condicional `if-else` para mostrar "Hemisferio Sur" si la latitud es negativa, o "Hemisferio Norte" si es positiva o cero.

**Ejemplo**:
- Salida esperada: `Hemisferio Sur`

---

### A12. Altitud con elif

**Enunciado**: Dada una variable `altitud = 2500`, clasificala usando `if-elif-else`:
- Menor a 500: "Zona baja"
- Entre 500 y 2000: "Zona media"
- Mayor a 2000: "Zona alta"

**Ejemplo**:
- Salida esperada: `Zona alta`

---

### A13. Validar latitud

**Enunciado**: Pedí al usuario una latitud. Si está entre -90 y 90 (inclusive), mostrá "Latitud válida". Si no, mostrá "Latitud inválida".

**Ejemplo**:
- Entrada: `-45.5`
- Salida esperada: `Latitud válida`

---

### A14. Ciudad costera

**Enunciado**: Dado un diccionario `ciudad = {"nombre": "Mar del Plata", "costera": True}`, verificá si la ciudad es costera y mostrá un mensaje apropiado.

**Ejemplo**:
- Salida esperada: `Mar del Plata es una ciudad costera`

---

### A15. Comparar alturas

**Enunciado**: Dados dos cerros con sus alturas: `cerro1 = 6962` (Aconcagua) y `cerro2 = 6893` (Ojos del Salado), mostrá cuál es más alto o si son iguales.

**Ejemplo**:
- Salida esperada: `El cerro 1 es más alto`

---

### Bloque 4: Bucles for

---

### A16. Iterar lista de ciudades

**Enunciado**: Dada la lista `ciudades = ["Salta", "Jujuy", "Tucumán"]`, usá un bucle `for` para mostrar cada ciudad en una línea separada.

**Ejemplo**:
- Salida esperada:
  ```
  Salta
  Jujuy
  Tucumán
  ```

---

### A17. Sumar altitudes

**Enunciado**: Dada la lista `altitudes = [1200, 850, 2100, 1500]`, usá un bucle `for` para calcular la suma total de todas las altitudes.

**Ejemplo**:
- Salida esperada: `5650`

**Hint**: Creá una variable acumuladora inicializada en 0.

---

### A18. Numerar con enumerate

**Enunciado**: Dada la lista `paises = ["Argentina", "Chile", "Uruguay", "Paraguay"]`, usá `enumerate()` para mostrar cada país con su número (empezando en 1).

**Ejemplo**:
- Salida esperada:
  ```
  1. Argentina
  2. Chile
  3. Uruguay
  4. Paraguay
  ```

**Hint**: Usá `enumerate(lista, start=1)` para empezar desde 1.

---

### A19. Recorrer con range

**Enunciado**: Usá `range()` para mostrar los números del 1 al 5, que representan los 5 continentes habitados.

**Ejemplo**:
- Salida esperada:
  ```
  1
  2
  3
  4
  5
  ```

---

### A20. Filtrar con for e if

**Enunciado**: Dada la lista `temperaturas = [25, -5, 18, -12, 30, 0]`, usá un bucle `for` para mostrar solo las temperaturas positivas (mayores a 0).

**Ejemplo**:
- Salida esperada:
  ```
  25
  18
  30
  ```

---

### Bloque 5: Bucles while y combinaciones

---

### A21. Contador con while

**Enunciado**: Usá un bucle `while` para mostrar los números del 1 al 5.

**Ejemplo**:
- Salida esperada:
  ```
  1
  2
  3
  4
  5
  ```

**Hint**: Necesitás una variable contador y una condición de parada.

---

### A22. Buscar en lista

**Enunciado**: Dada la lista `capitales = ["Lima", "Santiago", "Buenos Aires", "Montevideo"]`, usá un bucle `while` para encontrar en qué posición está "Buenos Aires".

**Ejemplo**:
- Salida esperada: `Buenos Aires está en la posición 2`

---

### A23. Salir con break

**Enunciado**: Dada la lista `altitudes = [500, 1200, 3500, 800, 2000]`, usá un bucle `for` con `break` para encontrar y mostrar la primera altitud mayor a 2000, y luego salir del bucle.

**Ejemplo**:
- Salida esperada: `Primera altitud alta encontrada: 3500`

---

### A24. Saltar con continue

**Enunciado**: Dada la lista `coordenadas = [(-34.6, -58.4), (0, 0), (-31.4, -64.2), (0, 0), (-32.9, -68.8)]`, usá un bucle `for` con `continue` para mostrar solo las coordenadas que NO sean (0, 0).

**Ejemplo**:
- Salida esperada:
  ```
  (-34.6, -58.4)
  (-31.4, -64.2)
  (-32.9, -68.8)
  ```

---

### A25. Tabla de multiplicar

**Enunciado**: Pedí al usuario un número entre 1 y 10 (validá con `while` que esté en ese rango). Luego mostrá su tabla de multiplicar del 1 al 10 usando un bucle `for`.

**Ejemplo**:
- Entrada: `5`
- Salida esperada:
  ```
  5 x 1 = 5
  5 x 2 = 10
  ...
  5 x 10 = 50
  ```

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Lista de coordenadas

**Enunciado**: Creá una lista que contenga 3 tuplas, cada una con el nombre y coordenadas de una ciudad argentina. Mostrá cada ciudad con sus coordenadas usando un bucle `for`.

**Ejemplo**:
- Salida esperada:
  ```
  Buenos Aires: (-34.6, -58.4)
  Córdoba: (-31.4, -64.2)
  Mendoza: (-32.9, -68.8)
  ```

---

### B2. Diccionario de altitudes

**Enunciado**: Creá un diccionario donde las claves sean nombres de cerros y los valores sean sus altitudes. Recorré el diccionario e imprimí cada cerro con su altura.

**Ejemplo**:
- Salida esperada:
  ```
  Aconcagua: 6962 m
  Ojos del Salado: 6893 m
  Monte Pissis: 6795 m
  ```

**Hint**: Usá `.items()` para recorrer claves y valores.

---

### B3. Máximo y mínimo

**Enunciado**: Dada la lista `poblaciones = [2890000, 1430000, 950000, 800000, 600000]` (poblaciones de ciudades argentinas), encontrá el valor máximo y mínimo usando bucles (sin usar `max()` ni `min()`).

**Ejemplo**:
- Salida esperada:
  ```
  Máximo: 2890000
  Mínimo: 600000
  ```

---

### B4. Contar elementos

**Enunciado**: Dada la lista `hemisferios = ["Sur", "Norte", "Sur", "Sur", "Norte", "Sur"]`, contá cuántas veces aparece "Sur" y cuántas "Norte".

**Ejemplo**:
- Salida esperada:
  ```
  Sur: 4
  Norte: 2
  ```

---

### B5. Invertir lista

**Enunciado**: Dada la lista `ciudades = ["A", "B", "C", "D"]`, creá una nueva lista con los elementos en orden inverso usando un bucle (sin usar `.reverse()` ni slicing).

**Ejemplo**:
- Salida esperada: `['D', 'C', 'B', 'A']`

---

### B6. Menú interactivo

**Enunciado**: Creá un menú que muestre 3 opciones (1. Ver ciudades, 2. Ver países, 3. Salir). Usá un bucle `while` para repetir el menú hasta que el usuario elija salir.

**Ejemplo**:
- Salida esperada:
  ```
  1. Ver ciudades
  2. Ver países
  3. Salir
  Opción: 1
  [Lista de ciudades]
  ...
  Opción: 3
  ¡Hasta luego!
  ```

---

### B7. Promedio de temperaturas

**Enunciado**: Dada la lista `temperaturas = [22.5, 25.0, 19.3, 28.1, 21.7]`, calculá el promedio usando un bucle `for` y mostralo redondeado a 1 decimal.

**Ejemplo**:
- Salida esperada: `Promedio: 23.3°C`

---

### B8. Filtrar diccionarios

**Enunciado**: Dada una lista de diccionarios de ciudades, filtrá y mostrá solo las que tienen más de 1 millón de habitantes.

```python
ciudades = [
    {"nombre": "Buenos Aires", "poblacion": 2890000},
    {"nombre": "Córdoba", "poblacion": 1430000},
    {"nombre": "Mendoza", "poblacion": 950000}
]
```

**Ejemplo**:
- Salida esperada:
  ```
  Buenos Aires: 2890000 habitantes
  Córdoba: 1430000 habitantes
  ```

---

### B9. Crear diccionario desde listas

**Enunciado**: Dadas dos listas `paises = ["Argentina", "Chile", "Uruguay"]` y `capitales = ["Buenos Aires", "Santiago", "Montevideo"]`, creá un diccionario donde cada país sea la clave y su capital el valor.

**Ejemplo**:
- Salida esperada: `{'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo'}`

**Hint**: Usá `zip()` para combinar las listas.

---

### B10. Validación completa

**Enunciado**: Pedí al usuario latitud y longitud. Validá que ambas estén en rangos correctos (lat: -90 a 90, lon: -180 a 180). Si alguna es inválida, pedí que la ingrese de nuevo hasta que sea correcta.

**Ejemplo**:
- Entrada: `100` (inválida), `-34.6` (válida)
- Salida: `Latitud inválida, intentá de nuevo...`
- Entrada: `-34.6`
- Salida: `Coordenadas válidas: (-34.6, -58.4)`

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Matriz de distancias

**Enunciado**: Creá una matriz (lista de listas) de 3x3 que represente las distancias entre 3 ciudades. Mostrá la matriz formateada como tabla.

**Ejemplo**:
- Salida esperada:
  ```
         BsAs  Cba  Mza
  BsAs      0  700  1000
  Cba     700    0   500
  Mza    1000  500     0
  ```

**Hint**: Usá bucles anidados para recorrer filas y columnas.

---

### C2. Ordenar lista (bubble sort)

**Enunciado**: Dada la lista `numeros = [64, 34, 25, 12, 22, 11, 90]`, implementá el algoritmo de ordenamiento burbuja (bubble sort) para ordenarla de menor a mayor.

**Ejemplo**:
- Salida esperada: `[11, 12, 22, 25, 34, 64, 90]`

**Hint**: Bubble sort compara pares adyacentes y los intercambia si están desordenados, repitiendo hasta que no haya intercambios.

---

### C3. Diccionario anidado

**Enunciado**: Creá un diccionario anidado que represente información completa de un país:
- Nombre, capital, coordenadas de la capital (como diccionario), lista de provincias/regiones

Luego accedé a la latitud de la capital y mostrá la tercera provincia.

**Ejemplo**:
```python
pais = {
    "nombre": "Argentina",
    "capital": {
        "nombre": "Buenos Aires",
        "coordenadas": {"lat": -34.6, "lon": -58.4}
    },
    "provincias": ["Buenos Aires", "Córdoba", "Santa Fe", ...]
}
```
- Salida esperada:
  ```
  Latitud de la capital: -34.6
  Tercera provincia: Santa Fe
  ```

---

### C4. Comprensión de listas

**Enunciado**: Investigá las "list comprehensions" de Python. Usá una comprensión de lista para:
1. Crear una lista con los cuadrados de los números del 1 al 10
2. Filtrar una lista de altitudes dejando solo las mayores a 1000

**Ejemplo**:
- Salida esperada:
  ```
  Cuadrados: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  Altitudes altas: [1200, 3500, 2000]
  ```

---

### C5. Sistema de registro de ciudades

**Enunciado**: Creá un programa que permita:
1. Agregar ciudades (nombre, latitud, longitud) a una lista de diccionarios
2. Listar todas las ciudades registradas
3. Buscar una ciudad por nombre
4. Eliminar una ciudad por nombre
5. Salir

Usá un menú interactivo con `while` y estructuras de datos apropiadas.

**Ejemplo**:
- Interacción:
  ```
  === REGISTRO DE CIUDADES ===
  1. Agregar ciudad
  2. Listar ciudades
  3. Buscar ciudad
  4. Eliminar ciudad
  5. Salir
  
  Opción: 1
  Nombre: Córdoba
  Latitud: -31.4
  Longitud: -64.2
  Ciudad agregada!
  
  Opción: 2
  1. Córdoba (-31.4, -64.2)
  
  Opción: 5
  ¡Hasta luego!
  ```

---

*Fin de los ejercicios de la Unidad 2*
