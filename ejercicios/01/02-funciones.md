# Unidad 2: Funciones

Ejercicios sobre definición de funciones, argumentos, retorno, type hints y scope.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Funciones sin argumentos ni return

---

### A1. Saludo simple

**Enunciado**: Definí una función llamada `saludar` que imprima "Bienvenido a GeoDojo". Luego llamala.

**Ejemplo**:
- Salida esperada: `Bienvenido a GeoDojo`

**Hint**: Usá `def nombre_funcion():` para definir una función.

---

### A2. Línea divisoria

**Enunciado**: Definí una función llamada `linea` que imprima una línea de 40 guiones. Llamala dos veces.

**Ejemplo**:
- Salida esperada:
  ```
  ----------------------------------------
  ----------------------------------------
  ```

---

### A3. Encabezado de reporte

**Enunciado**: Definí una función llamada `encabezado` que imprima:
```
==============================
    REPORTE GEOGRÁFICO
==============================
```
Llamala una vez.

---

### A4. Coordenadas de ejemplo

**Enunciado**: Definí una función llamada `mostrar_buenos_aires` que imprima las coordenadas de Buenos Aires en tres líneas: nombre, latitud y longitud.

**Ejemplo**:
- Salida esperada:
  ```
  Ciudad: Buenos Aires
  Latitud: -34.6
  Longitud: -58.4
  ```

---

### A5. Menú de opciones

**Enunciado**: Definí una función llamada `mostrar_menu` que imprima un menú con 3 opciones:
1. Ver ciudades
2. Calcular distancia
3. Salir

Llamala una vez.

**Ejemplo**:
- Salida esperada:
  ```
  === MENÚ ===
  1. Ver ciudades
  2. Calcular distancia
  3. Salir
  ```

---

### Bloque 2: Funciones con argumentos

---

### A6. Saludo personalizado

**Enunciado**: Definí una función llamada `saludar_ciudad` que reciba un argumento `ciudad` e imprima "Bienvenido a [ciudad]".

**Ejemplo**:
- Llamada: `saludar_ciudad("Mendoza")`
- Salida esperada: `Bienvenido a Mendoza`

---

### A7. Mostrar coordenada

**Enunciado**: Definí una función llamada `mostrar_latitud` que reciba una latitud como argumento e imprima "Latitud: [valor]°".

**Ejemplo**:
- Llamada: `mostrar_latitud(-34.6)`
- Salida esperada: `Latitud: -34.6°`

---

### A8. Ficha de ciudad

**Enunciado**: Definí una función llamada `ficha_ciudad` que reciba tres argumentos: `nombre`, `latitud` y `longitud`. Debe imprimir una ficha formateada.

**Ejemplo**:
- Llamada: `ficha_ciudad("Córdoba", -31.4, -64.2)`
- Salida esperada:
  ```
  Ciudad: Córdoba
  Coordenadas: (-31.4, -64.2)
  ```

---

### A9. Repetir texto

**Enunciado**: Definí una función llamada `repetir` que reciba un texto y un número, e imprima el texto repetido esa cantidad de veces (uno por línea).

**Ejemplo**:
- Llamada: `repetir("Hola", 3)`
- Salida esperada:
  ```
  Hola
  Hola
  Hola
  ```

**Hint**: Usá un bucle `for` dentro de la función.

---

### A10. Línea personalizada

**Enunciado**: Definí una función llamada `linea_custom` que reciba un carácter y un largo, e imprima una línea con ese carácter repetido.

**Ejemplo**:
- Llamada: `linea_custom("=", 20)`
- Salida esperada: `====================`

---

### Bloque 3: Funciones con return

---

### A11. Doble de un número

**Enunciado**: Definí una función llamada `doble` que reciba un número y retorne su doble.

**Ejemplo**:
- Llamada: `resultado = doble(25)`
- Valor de `resultado`: `50`

**Hint**: Usá `return valor` para retornar.

---

### A12. Distancia al ecuador

**Enunciado**: Definí una función llamada `distancia_ecuador` que reciba una latitud y retorne su valor absoluto (la distancia al ecuador en grados).

**Ejemplo**:
- Llamada: `distancia_ecuador(-34.6)`
- Retorna: `34.6`

---

### A13. Celsius a Fahrenheit

**Enunciado**: Definí una función llamada `celsius_a_fahrenheit` que reciba una temperatura en Celsius y retorne el equivalente en Fahrenheit (F = C × 9/5 + 32).

**Ejemplo**:
- Llamada: `celsius_a_fahrenheit(25)`
- Retorna: `77.0`

---

### A14. Punto medio

**Enunciado**: Definí una función llamada `punto_medio` que reciba dos valores y retorne el promedio entre ellos.

**Ejemplo**:
- Llamada: `punto_medio(-34.6, -31.4)`
- Retorna: `-33.0`

---

### A15. Es hemisferio norte

**Enunciado**: Definí una función llamada `es_hemisferio_norte` que reciba una latitud y retorne `True` si es mayor a 0, `False` en caso contrario.

**Ejemplo**:
- Llamada: `es_hemisferio_norte(-34.6)`
- Retorna: `False`

---

### Bloque 4: Type hints básicos

---

### A16. Suma con tipos

**Enunciado**: Definí una función `sumar` que reciba dos argumentos de tipo `float` y retorne un `float`. Usá type hints en la definición.

**Ejemplo**:
```python
def sumar(a: float, b: float) -> float:
    ...
```
- Llamada: `sumar(10.5, 20.3)`
- Retorna: `30.8`

---

### A17. Formatear coordenada

**Enunciado**: Definí una función `formatear_coord` que reciba una latitud (`float`) y retorne un `str` con el formato "XX.X°".

**Ejemplo**:
```python
def formatear_coord(lat: float) -> str:
    ...
```
- Llamada: `formatear_coord(-34.6)`
- Retorna: `"-34.6°"`

---

### A18. Validar latitud

**Enunciado**: Definí una función `es_latitud_valida` que reciba un valor `float` y retorne un `bool` indicando si está entre -90 y 90.

**Ejemplo**:
```python
def es_latitud_valida(lat: float) -> bool:
    ...
```
- Llamada: `es_latitud_valida(-34.6)`
- Retorna: `True`

---

### A19. Kilómetros a millas

**Enunciado**: Definí una función `km_a_millas` con type hints que reciba kilómetros (`float`) y retorne millas (`float`). 1 km = 0.621371 millas.

**Ejemplo**:
- Llamada: `km_a_millas(100)`
- Retorna: `62.1371`

---

### A20. Contar caracteres

**Enunciado**: Definí una función `contar_caracteres` que reciba un `str` y retorne un `int` con la cantidad de caracteres.

**Ejemplo**:
```python
def contar_caracteres(texto: str) -> int:
    ...
```
- Llamada: `contar_caracteres("Buenos Aires")`
- Retorna: `12`

---

### Bloque 5: Scope y múltiples returns

---

### A21. Variable local

**Enunciado**: Definí una función `crear_mensaje` que cree una variable local `mensaje` con el texto "Coordenadas cargadas" y la retorne. Fuera de la función, intentá imprimir `mensaje` directamente (debería dar error).

**Ejemplo**:
- Llamada: `crear_mensaje()` retorna `"Coordenadas cargadas"`
- `print(mensaje)` fuera de la función → `NameError`

---

### A22. Hemisferio como texto

**Enunciado**: Definí una función `hemisferio` que reciba una latitud y retorne `"Norte"` si es positiva, `"Sur"` si es negativa, o `"Ecuador"` si es 0.

**Ejemplo**:
- `hemisferio(40.7)` → `"Norte"`
- `hemisferio(-34.6)` → `"Sur"`
- `hemisferio(0)` → `"Ecuador"`

---

### A23. Clasificar altitud

**Enunciado**: Definí una función `clasificar_altitud` que reciba metros y retorne:
- `"Baja"` si es menor a 500
- `"Media"` si está entre 500 y 2000
- `"Alta"` si es mayor a 2000

**Ejemplo**:
- `clasificar_altitud(300)` → `"Baja"`
- `clasificar_altitud(1500)` → `"Media"`
- `clasificar_altitud(3500)` → `"Alta"`

---

### A24. Usar variable global

**Enunciado**: Definí una variable global `RADIO_TIERRA = 6371` (en km). Luego definí una función `circunferencia_tierra` que use esta constante para calcular la circunferencia (2 × π × radio). Usá `3.14159` para π.

**Ejemplo**:
- Llamada: `circunferencia_tierra()`
- Retorna aproximadamente: `40030.14`

**Hint**: Las constantes globales en mayúsculas son accesibles desde las funciones.

---

### A25. Validar coordenadas completas

**Enunciado**: Definí una función `validar_coordenadas` que reciba latitud y longitud, y retorne:
- `"Válidas"` si latitud está entre -90 y 90 Y longitud entre -180 y 180
- `"Latitud inválida"` si solo la latitud está fuera de rango
- `"Longitud inválida"` si solo la longitud está fuera de rango
- `"Ambas inválidas"` si ambas están fuera de rango

**Ejemplo**:
- `validar_coordenadas(-34.6, -58.4)` → `"Válidas"`
- `validar_coordenadas(-100, -58.4)` → `"Latitud inválida"`
- `validar_coordenadas(-34.6, 200)` → `"Longitud inválida"`

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Argumento por defecto

**Enunciado**: Definí una función `saludar` que reciba un nombre con valor por defecto `"visitante"`. Si no se pasa argumento, debe usar el valor por defecto.

**Ejemplo**:
- `saludar("María")` → imprime `"Hola, María"`
- `saludar()` → imprime `"Hola, visitante"`

---

### B2. Múltiples valores por defecto

**Enunciado**: Definí una función `crear_punto` que reciba `nombre`, `lat=0.0` y `lon=0.0`. Debe retornar un string formateado.

**Ejemplo**:
- `crear_punto("Origen")` → `"Origen: (0.0, 0.0)"`
- `crear_punto("Buenos Aires", -34.6, -58.4)` → `"Buenos Aires: (-34.6, -58.4)"`

---

### B3. Argumentos con nombre

**Enunciado**: Definí una función `describir_lugar` que reciba `nombre`, `pais` y `continente`. Llamala usando argumentos con nombre (kwargs) en diferente orden.

**Ejemplo**:
- `describir_lugar(continente="América", nombre="Lima", pais="Perú")`
- Salida: `"Lima, Perú - América"`

---

### B4. Función que llama función

**Enunciado**: Definí una función `es_valida` que llame a `es_latitud_valida` y `es_longitud_valida` (deberás definirlas también) para validar un par de coordenadas.

**Ejemplo**:
- `es_valida(-34.6, -58.4)` → `True`
- `es_valida(-100, -58.4)` → `False`

---

### B5. Docstring básico

**Enunciado**: Definí una función `calcular_area` que calcule el área de un rectángulo. Incluí un docstring que describa qué hace, sus parámetros y qué retorna.

**Ejemplo**:
```python
def calcular_area(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.
    
    Args:
        base: El largo del rectángulo en metros.
        altura: El ancho del rectángulo en metros.
    
    Returns:
        El área en metros cuadrados.
    """
    ...
```

---

### B6. Función con docstring y type hints

**Enunciado**: Definí una función `distancia_euclidiana` que calcule la distancia simplificada entre dos puntos (lat1, lon1) y (lat2, lon2). Incluí docstring completo y type hints.

**Ejemplo**:
- `distancia_euclidiana(-34.6, -58.4, -33.4, -70.6)` → aproximadamente `12.4`

**Hint**: distancia = √[(lat2-lat1)² + (lon2-lon1)²]

---

### B7. Type hints con Optional

**Enunciado**: Definí una función `obtener_hemisferio` que reciba una latitud opcional (puede ser `None`). Si es `None`, retorne `"Desconocido"`. Usá `Optional[float]` del módulo `typing`.

**Ejemplo**:
```python
from typing import Optional

def obtener_hemisferio(lat: Optional[float]) -> str:
    ...
```
- `obtener_hemisferio(-34.6)` → `"Sur"`
- `obtener_hemisferio(None)` → `"Desconocido"`

---

### B8. Función de formateo completo

**Enunciado**: Definí una función `formato_dms` que reciba grados decimales y retorne un string en formato grados°minutos'. Ej: -34.6 → "34°36' S"

**Ejemplo**:
- `formato_dms(-34.6)` → `"34°36' S"`
- `formato_dms(40.7)` → `"40°42' N"`

**Hint**: minutos = (valor_decimal - parte_entera) × 60

---

### B9. Función con validación interna

**Enunciado**: Definí una función `crear_coordenada` que reciba lat y lon, valide que estén en rango, y retorne un string formateado. Si son inválidas, retorne `"Coordenadas inválidas"`.

**Ejemplo**:
- `crear_coordenada(-34.6, -58.4)` → `"(-34.6, -58.4)"`
- `crear_coordenada(-100, 50)` → `"Coordenadas inválidas"`

---

### B10. Componer funciones

**Enunciado**: Usando las funciones anteriores (o creando nuevas), definí una función `generar_link_maps` que reciba nombre, lat y lon, valide las coordenadas, y retorne un link de Google Maps o un mensaje de error.

**Ejemplo**:
- `generar_link_maps("Casa", -34.6, -58.4)` → `"Casa: https://www.google.com/maps?q=-34.6,-58.4"`
- `generar_link_maps("Error", -100, 50)` → `"Coordenadas inválidas para Error"`

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Función con *args

**Enunciado**: Definí una función `promedio` que reciba cualquier cantidad de números usando `*args` y retorne su promedio.

**Ejemplo**:
- `promedio(10, 20, 30)` → `20.0`
- `promedio(5, 10, 15, 20, 25)` → `15.0`

**Hint**: `*args` es una tupla con todos los argumentos posicionales.

---

### C2. Retorno múltiple (tupla)

**Enunciado**: Definí una función `separar_coordenada` que reciba grados decimales y retorne una tupla con (grados_enteros, minutos, direccion).

**Ejemplo**:
- `separar_coordenada(-34.6)` → `(34, 36.0, "S")`
- `grados, minutos, dir = separar_coordenada(-34.6)`

---

### C3. Función como variable

**Enunciado**: Definí dos funciones: `km_a_millas` y `millas_a_km`. Luego asigná una de ellas a una variable `convertir` según una condición, y usala.

**Ejemplo**:
```python
modo = "metrico"
if modo == "metrico":
    convertir = millas_a_km
else:
    convertir = km_a_millas

resultado = convertir(100)
```

---

### C4. Recursión básica

**Enunciado**: Definí una función recursiva `cuenta_regresiva` que reciba un número e imprima la cuenta regresiva hasta 0.

**Ejemplo**:
- `cuenta_regresiva(5)` imprime:
  ```
  5
  4
  3
  2
  1
  0
  ```

**Hint**: Una función recursiva se llama a sí misma con un caso base para terminar.

---

### C5. Decorador simple

**Enunciado**: Investigá qué es un decorador en Python. Creá un decorador `@mostrar_ejecucion` que imprima "Ejecutando función..." antes de ejecutar cualquier función decorada.

**Ejemplo**:
```python
@mostrar_ejecucion
def saludar():
    print("Hola!")

saludar()
```
- Salida:
  ```
  Ejecutando función...
  Hola!
  ```

**Hint**: Un decorador es una función que recibe una función y retorna otra función.

---

*Fin de los ejercicios de la Unidad 2*
