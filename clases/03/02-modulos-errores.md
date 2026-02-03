# Clase 3: Módulos y Manejo de Errores

Guía para la clase sobre importación de módulos y manejo de excepciones.

---

## 1. Temario

### 1.1 Importar módulos

| Sintaxis | Descripción | Ejemplo |
|----------|-------------|---------|
| `import modulo` | Importa módulo completo | `import math` → `math.sqrt(4)` |
| `from modulo import func` | Importa función específica | `from math import sqrt` → `sqrt(4)` |
| `from modulo import *` | Importa todo (no recomendado) | `from math import *` |
| `import modulo as alias` | Importa con alias | `import math as m` → `m.sqrt(4)` |
| `from modulo import f as a` | Función con alias | `from math import sqrt as raiz` |

### 1.2 Módulos estándar útiles

| Módulo | Funciones comunes | Uso |
|--------|-------------------|-----|
| `math` | `sqrt()`, `pow()`, `pi`, `sin()`, `cos()` | Cálculos matemáticos |
| `os` | `getcwd()`, `listdir()`, `path.exists()` | Sistema operativo |
| `random` | `random()`, `randint()`, `choice()`, `uniform()` | Números aleatorios |
| `datetime` | `datetime.now()`, `strftime()`, `strptime()` | Fechas y horas |
| `time` | `sleep()`, `time()` | Tiempo y pausas |

### 1.3 Try/except básico

### 1.4 Excepciones comunes

| Excepción | Cuándo ocurre | Ejemplo |
|-----------|---------------|---------|
| `ZeroDivisionError` | División por cero | `10 / 0` |
| `ValueError` | Valor incorrecto | `int("abc")` |
| `TypeError` | Tipo incorrecto | `"a" + 1` |
| `FileNotFoundError` | Archivo no existe | `open("noexiste.txt")` |
| `KeyError` | Clave no existe en dict | `d["clave_inexistente"]` |
| `IndexError` | Índice fuera de rango | `lista[100]` |
| `Exception` | Clase base de errores | Captura cualquier error |

### 1.5 Estructura completa try/except/else/finally

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Importar módulo math
Calcular la raíz cuadrada de la suma de los cuadrados de dos catetos (hipotenusa).

---

#### Ejemplo 2: Importar función específica
Importar solo `sqrt` y `pi` de math. Calcular el área de un círculo.

---

#### Ejemplo 3: Módulo os
Mostrar el directorio actual y listar sus archivos.

---

#### Ejemplo 4: Módulo random
Generar una coordenada geográfica aleatoria válida (lat entre -90 y 90, lon entre -180 y 180).

---

#### Ejemplo 5: Módulo datetime
Mostrar la fecha y hora actual, y formatearla como "DD/MM/YYYY HH:MM".

---

#### Ejemplo 6: Try/except simple
Pedir al usuario un número y dividir 100 por ese número. Manejar división por cero.

---

#### Ejemplo 7: Múltiples excepciones
Mejorar el ejemplo anterior para también manejar cuando el usuario ingresa texto en lugar de número.

---

#### Ejemplo 8: Capturar error de archivo
Intentar leer un archivo que puede o no existir. Mostrar contenido o mensaje de error.

---

#### Ejemplo 9: Bloque else y finally
Leer un archivo mostrando mensajes en cada etapa: éxito, error, y finalización.

---

#### Ejemplo 10: Función robusta
Crear una función que convierta coordenadas de texto a números, retornando None si falla.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Importar módulo math

**Enunciado**: Calcular la raíz cuadrada de la suma de los cuadrados de dos catetos (hipotenusa).

```python
import math

cateto_a = 3
cateto_b = 4

# Teorema de Pitágoras: c² = a² + b²
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

print(f"Catetos: {cateto_a} y {cateto_b}")
print(f"Hipotenusa: {hipotenusa}")
```

**Salida**:
```
Catetos: 3 y 4
Hipotenusa: 5.0
```

---

#### Ejemplo 2: Importar función específica

**Enunciado**: Importar solo `sqrt` y `pi` de math. Calcular el área de un círculo.

```python
from math import sqrt, pi

radio = 5

# Área = π × r²
area = pi * radio**2

print(f"Radio: {radio}")
print(f"Área: {round(area, 2)}")
```

**Salida**:
```
Radio: 5
Área: 78.54
```

---

#### Ejemplo 3: Módulo os

**Enunciado**: Mostrar el directorio actual y listar sus archivos.

```python
import os

# Directorio actual
directorio = os.getcwd()
print(f"Directorio actual: {directorio}")

# Listar archivos
archivos = os.listdir()
print(f"\nArchivos ({len(archivos)}):")
for archivo in archivos[:5]:  # Mostrar primeros 5
    print(f"  - {archivo}")
```

**Salida**:
```
Directorio actual: /home/usuario/proyecto

Archivos (8):
  - datos.csv
  - main.py
  - README.md
  - ...
```

---

#### Ejemplo 4: Módulo random

**Enunciado**: Generar una coordenada geográfica aleatoria válida (lat entre -90 y 90, lon entre -180 y 180).

```python
import random

# Latitud: -90 a 90
latitud = random.uniform(-90, 90)

# Longitud: -180 a 180
longitud = random.uniform(-180, 180)

print(f"Coordenada aleatoria:")
print(f"  Latitud: {round(latitud, 4)}")
print(f"  Longitud: {round(longitud, 4)}")
```

**Salida**:
```
Coordenada aleatoria:
  Latitud: -34.5678
  Longitud: 125.4321
```

---

#### Ejemplo 5: Módulo datetime

**Enunciado**: Mostrar la fecha y hora actual, y formatearla como "DD/MM/YYYY HH:MM".

```python
from datetime import datetime

ahora = datetime.now()

print(f"Fecha y hora completa: {ahora}")
print(f"Formateada: {ahora.strftime('%d/%m/%Y %H:%M')}")
print(f"Solo fecha: {ahora.strftime('%d de %B de %Y')}")
```

**Salida**:
```
Fecha y hora completa: 2026-02-03 14:30:45.123456
Formateada: 03/02/2026 14:30
Solo fecha: 03 de February de 2026
```

---

#### Ejemplo 6: Try/except simple

**Enunciado**: Pedir al usuario un número y dividir 100 por ese número. Manejar división por cero.

```python
numero = input("Ingresá un número: ")
numero = int(numero)

try:
    resultado = 100 / numero
    print(f"100 / {numero} = {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
```

---

#### Ejemplo 7: Múltiples excepciones

**Enunciado**: Mejorar el ejemplo anterior para también manejar cuando el usuario ingresa texto en lugar de número.

```python
entrada = input("Ingresá un número: ")

try:
    numero = int(entrada)
    resultado = 100 / numero
    print(f"100 / {numero} = {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except ValueError:
    print(f"Error: '{entrada}' no es un número válido")
```

---

#### Ejemplo 8: Capturar error de archivo

**Enunciado**: Intentar leer un archivo que puede o no existir. Mostrar contenido o mensaje de error.

```python
nombre_archivo = "datos.txt"

try:
    with open(nombre_archivo, "r") as f:
        contenido = f.read()
        print(f"Contenido:\n{contenido}")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe")
```

---

#### Ejemplo 9: Bloque else y finally

**Enunciado**: Leer un archivo mostrando mensajes en cada etapa: éxito, error, y finalización.

```python
nombre_archivo = "datos.txt"

try:
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("❌ Error: Archivo no encontrado")
else:
    print(f"✓ Archivo leído correctamente")
    print(f"  Tamaño: {len(contenido)} caracteres")
finally:
    print("🏁 Operación finalizada")
```

---

#### Ejemplo 10: Función robusta

**Enunciado**: Crear una función que convierta coordenadas de texto a números, retornando None si falla.

```python
def convertir_coordenada(texto):
    """Convierte string a float, retorna None si falla."""
    try:
        return float(texto)
    except ValueError:
        return None

# Pruebas
print(convertir_coordenada("-34.6"))      # -34.6
print(convertir_coordenada("invalido"))   # None
print(convertir_coordenada(""))           # None

# Uso práctico
lat_texto = input("Latitud: ")
lat = convertir_coordenada(lat_texto)

if lat is not None:
    print(f"Latitud válida: {lat}")
else:
    print("Latitud inválida")
```

**Salida**:
```
-34.6
None
None
Latitud: -31.4
Latitud válida: -31.4
```

---

## Notas para el docente
- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Cada ejemplo introduce 1-2 conceptos nuevos de forma incremental
- Enfatizar que `try/except` es para errores esperados, no para evitar bugs
- Mostrar que `Exception` captura casi todo, pero es mejor ser específico
- El bloque `finally` es útil para liberar recursos (cerrar archivos, conexiones)
- Los ejercicios en `ejercicios/03/02-modulos-errores.md` refuerzan estos conceptos
- Contexto geográfico: coordenadas, validación de datos
