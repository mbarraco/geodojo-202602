# Unidad 3: Módulos y Manejo de Errores

Ejercicios sobre importación de módulos y manejo de excepciones con try/except.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Importar módulos

---

### A1. Importar módulo completo

**Enunciado**: Importá el módulo `math` y usá `math.sqrt()` para calcular la raíz cuadrada de 144.

**Ejemplo**:
- Salida esperada: `12.0`

**Hint**: Usá `import math` y luego `math.sqrt(144)`.

---

### A2. Importar función específica

**Enunciado**: Importá solo la función `sqrt` del módulo `math` y usala para calcular la raíz cuadrada de 225.

**Ejemplo**:
- Salida esperada: `15.0`

**Hint**: Usá `from math import sqrt` y luego `sqrt(225)` directamente.

---

### A3. Importar con alias

**Enunciado**: Importá el módulo `math` con el alias `m` y usá `m.pi` para mostrar el valor de π.

**Ejemplo**:
- Salida esperada: `3.141592653589793`

**Hint**: Usá `import math as m`.

---

### A4. Importar múltiples funciones

**Enunciado**: Importá `sqrt`, `pow` y `pi` del módulo `math` en una sola línea. Calculá la circunferencia de un círculo de radio 5 (2 × π × r).

**Ejemplo**:
- Salida esperada: `31.41592653589793`

**Hint**: `from math import sqrt, pow, pi`.

---

### A5. Listar contenido de módulo

**Enunciado**: Usá `dir(math)` para ver todas las funciones disponibles en el módulo math. Mostrá las primeras 10.

**Ejemplo**:
- Salida esperada: lista de nombres de funciones

**Hint**: `dir()` devuelve una lista de nombres disponibles en un módulo.

---

### Bloque 2: Módulos estándar útiles

---

### A6. Módulo os - directorio actual

**Enunciado**: Usá el módulo `os` para mostrar el directorio de trabajo actual.

**Ejemplo**:
- Salida esperada: `/home/usuario/proyecto` (o similar)

**Hint**: Usá `os.getcwd()`.

---

### A7. Módulo os - listar archivos

**Enunciado**: Usá `os.listdir()` para listar los archivos del directorio actual.

**Ejemplo**:
- Salida esperada: `['archivo1.py', 'datos.csv', ...]`

---

### A8. Módulo random - número aleatorio

**Enunciado**: Usá el módulo `random` para generar una coordenada de latitud aleatoria entre -90 y 90.

**Ejemplo**:
- Salida esperada: `-34.567` (número aleatorio diferente cada vez)

**Hint**: Usá `random.uniform(-90, 90)`.

---

### A9. Módulo random - elección aleatoria

**Enunciado**: Dada una lista de ciudades `["Buenos Aires", "Córdoba", "Rosario", "Mendoza"]`, usá `random.choice()` para elegir una ciudad al azar.

**Ejemplo**:
- Salida esperada: `Córdoba` (o cualquier ciudad de la lista)

---

### A10. Módulo datetime - fecha actual

**Enunciado**: Usá el módulo `datetime` para obtener y mostrar la fecha y hora actual.

**Ejemplo**:
- Salida esperada: `2026-02-03 14:30:45.123456`

**Hint**: Usá `datetime.datetime.now()`.

---

### Bloque 3: Try/except básico

---

### A11. Capturar error de división

**Enunciado**: Escribí un programa que intente dividir 10 por 0. Usá try/except para capturar el error y mostrar un mensaje amigable.

**Ejemplo**:
- Salida esperada: `Error: No se puede dividir por cero`

**Hint**: El error de división por cero es `ZeroDivisionError`.

---

### A12. Capturar error de conversión

**Enunciado**: Intentá convertir el string "abc" a entero usando `int()`. Capturá el error y mostrá un mensaje apropiado.

**Ejemplo**:
- Salida esperada: `Error: No se puede convertir 'abc' a número`

**Hint**: El error de conversión es `ValueError`.

---

### A13. Capturar error de archivo

**Enunciado**: Intentá abrir un archivo que no existe (`archivo_inexistente.txt`). Capturá el error y mostrá un mensaje.

**Ejemplo**:
- Salida esperada: `Error: El archivo no fue encontrado`

**Hint**: El error es `FileNotFoundError`.

---

### A14. Capturar error de índice

**Enunciado**: Dada la lista `ciudades = ["Buenos Aires", "Córdoba"]`, intentá acceder al índice 10. Capturá el error.

**Ejemplo**:
- Salida esperada: `Error: Índice fuera de rango`

**Hint**: El error es `IndexError`.

---

### A15. Capturar error de clave

**Enunciado**: Dado el diccionario `punto = {"lat": -34.6, "lon": -58.4}`, intentá acceder a la clave "nombre". Capturá el error.

**Ejemplo**:
- Salida esperada: `Error: La clave 'nombre' no existe`

**Hint**: El error es `KeyError`.

---

### Bloque 4: Excepciones específicas y else/finally

---

### A16. Múltiples excepciones

**Enunciado**: Escribí un programa que pida al usuario un número y lo use como divisor de 100. Manejá tanto el caso de división por cero como de entrada inválida (texto en lugar de número).

**Ejemplo**:
- Entrada: `0` → Salida: `Error: División por cero`
- Entrada: `abc` → Salida: `Error: Entrada inválida`
- Entrada: `5` → Salida: `Resultado: 20.0`

---

### A17. Bloque else en try

**Enunciado**: Escribí un programa que intente abrir y leer un archivo. Si tiene éxito (no hay error), mostrá "Archivo leído correctamente" en el bloque `else`.

**Ejemplo**:
- Si el archivo existe: `Contenido: ... Archivo leído correctamente`
- Si no existe: `Error: Archivo no encontrado`

**Hint**: El bloque `else` se ejecuta solo si no hubo excepciones.

---

### A18. Bloque finally

**Enunciado**: Escribí un programa que intente abrir un archivo y use `finally` para mostrar "Operación finalizada" siempre, haya o no error.

**Ejemplo**:
- Si el archivo existe: `Contenido: ... Operación finalizada`
- Si no existe: `Error: ... Operación finalizada`

**Hint**: El bloque `finally` se ejecuta siempre, haya o no excepción.

---

### A19. Obtener mensaje de error

**Enunciado**: Capturá un error de archivo y mostrá el mensaje de error original usando `as e`.

**Ejemplo**:
- Salida esperada: `Error: [Errno 2] No such file or directory: 'noexiste.txt'`

**Hint**: Usá `except FileNotFoundError as e:` y luego `print(e)`.

---

### A20. Capturar cualquier excepción

**Enunciado**: Escribí un programa que capture cualquier tipo de excepción usando `except Exception`. Probalo con una división por cero.

**Ejemplo**:
- Salida esperada: `Ocurrió un error: division by zero`

**Hint**: `Exception` es la clase base de la mayoría de errores.

---

### Bloque 5: Funciones robustas con manejo de errores

---

### A21. Función con validación

**Enunciado**: Creá una función `convertir_coordenada(texto)` que convierta un string a float. Si falla, debe retornar `None` en lugar de fallar.

**Ejemplo**:
- `convertir_coordenada("-34.6")` → `-34.6`
- `convertir_coordenada("invalido")` → `None`

---

### A22. Leer archivo seguro

**Enunciado**: Creá una función `leer_archivo_seguro(path)` que retorne el contenido del archivo, o un string vacío si el archivo no existe.

**Ejemplo**:
- Si el archivo existe: retorna contenido
- Si no existe: retorna `""`

---

### A23. Obtener valor de diccionario seguro

**Enunciado**: Creá una función `obtener_valor(diccionario, clave, default=None)` que retorne el valor de la clave, o el valor por defecto si la clave no existe.

**Ejemplo**:
- `obtener_valor({"a": 1}, "a")` → `1`
- `obtener_valor({"a": 1}, "b")` → `None`
- `obtener_valor({"a": 1}, "b", 0)` → `0`

**Hint**: Python ya tiene esto: `dict.get()`. Implementalo vos usando try/except.

---

### A24. Validar coordenadas

**Enunciado**: Creá una función `validar_coordenada(lat, lon)` que verifique si las coordenadas son válidas (lat entre -90 y 90, lon entre -180 y 180). Si recibe valores no numéricos, debe capturar el error y retornar `False`.

**Ejemplo**:
- `validar_coordenada(-34.6, -58.4)` → `True`
- `validar_coordenada(-100, 50)` → `False`
- `validar_coordenada("abc", -58.4)` → `False`

---

### A25. Parsear línea de CSV manualmente

**Enunciado**: Creá una función `parsear_punto(linea)` que reciba un string con formato "ciudad,lat,lon" y retorne un diccionario. Si el formato es incorrecto, debe retornar `None`.

**Ejemplo**:
- `parsear_punto("Buenos Aires,-34.6,-58.4")` → `{"ciudad": "Buenos Aires", "lat": -34.6, "lon": -58.4}`
- `parsear_punto("datos_invalidos")` → `None`

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Módulo os.path

**Enunciado**: Usá `os.path.exists()` para verificar si un archivo existe antes de intentar abrirlo.

---

### B2. Generar coordenadas aleatorias

**Enunciado**: Usá el módulo `random` para generar 5 puntos geográficos aleatorios (cada uno con lat y lon válidas).

---

### B3. Formatear fecha

**Enunciado**: Usá `datetime.strftime()` para mostrar la fecha actual en formato "03/02/2026".

**Hint**: El formato es `"%d/%m/%Y"`.

---

### B4. Calcular distancia con math

**Enunciado**: Usá `math.sqrt()` y `math.pow()` para calcular la distancia euclidiana entre dos puntos geográficos.

---

### B5. Re-lanzar excepción

**Enunciado**: Capturá una excepción, registrá el error en una variable, y luego re-lanzá la excepción usando `raise`.

---

### B6. Validar múltiples archivos

**Enunciado**: Dada una lista de nombres de archivos, verificá cuáles existen y cuáles no, mostrando un reporte.

---

### B7. Timeout simulado

**Enunciado**: Usá `time.sleep()` para simular una operación que tarda. Si tarda más de 2 segundos, mostrá un mensaje.

---

### B8. Parsear fecha de string

**Enunciado**: Usá `datetime.strptime()` para convertir el string "03-02-2026" a un objeto datetime. Manejá el error si el formato es incorrecto.

---

### B9. Crear directorio seguro

**Enunciado**: Usá `os.makedirs()` con el parámetro `exist_ok=True` para crear un directorio solo si no existe.

---

### B10. Encadenar excepciones

**Enunciado**: Capturá un error y lanzá otro error personalizado usando `raise ... from e`.

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Crear tu propio módulo

**Enunciado**: Creá un archivo `geo_utils.py` con funciones para calcular distancia y validar coordenadas. Luego importalo desde otro archivo y usá las funciones.

---

### C2. Excepción personalizada

**Enunciado**: Creá una clase `CoordenadaInvalidaError` que herede de `Exception`. Usala en una función de validación que lance este error específico.

```python
class CoordenadaInvalidaError(Exception):
    pass
```

---

### C3. Context manager personalizado

**Enunciado**: Creá un context manager usando `__enter__` y `__exit__` que registre cuánto tiempo tardó un bloque de código en ejecutarse.

---

### C4. Reintentar operación fallida

**Enunciado**: Creá una función `reintentar(funcion, intentos=3)` que ejecute una función y, si falla, reintente hasta N veces antes de rendirse.

---

### C5. Sistema de logging con niveles

**Enunciado**: Usá el módulo `logging` de Python para crear un sistema de logs con niveles DEBUG, INFO, WARNING y ERROR. Configurá para que escriba a un archivo.

---

*Fin de los ejercicios de la Unidad 3 - Módulos y Manejo de Errores*
