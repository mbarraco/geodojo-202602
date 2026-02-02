# Clase 2: Funciones

Guía para la clase sobre definición de funciones, argumentos, retorno, type hints y scope.

---

## 1. Temario

### 1.1 Definición de funciones

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| `def` | Palabra clave para definir funciones | `def mi_funcion():` |
| Nombre | snake_case, descriptivo | `calcular_area`, `mostrar_datos` |
| Cuerpo | Código indentado dentro de la función | Ver ejemplos abajo |
| Llamada | Ejecutar la función usando paréntesis | `mi_funcion()` |

### 1.2 Argumentos (parámetros)

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| Sin argumentos | Función que no recibe datos | `def saludar():` |
| Con argumentos | Función que recibe datos | `def saludar(nombre):` |
| Múltiples args | Separados por coma | `def sumar(a, b):` |
| Valor por defecto | Si no se pasa, usa el default | `def saludar(nombre="visitante"):` |
| Argumentos con nombre | Especificar nombre al llamar | `funcion(x=10, y=20)` |

### 1.3 Retorno de valores

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| `return` | Devuelve un valor al código que llamó | `return resultado` |
| Sin return | La función retorna `None` implícitamente | `def imprimir(): print("hola")` |
| Return temprano | Puede salir antes de terminar | `if error: return None` |
| Múltiples returns | Según condiciones | `if x > 0: return "positivo"` |
| Retorno múltiple | Devuelve tupla | `return lat, lon` |

### 1.4 Type hints

| Sintaxis | Descripción | Ejemplo |
|----------|-------------|---------|
| Argumento | Tipo esperado del parámetro | `def f(x: int):` |
| Retorno | Tipo que devuelve la función | `def f() -> str:` |
| Completo | Argumentos y retorno | `def f(x: int) -> str:` |
| `Optional` | Puede ser el tipo o `None` | `def f(x: Optional[int]):` |

```python
# Ejemplo completo con type hints
def calcular_area(base: float, altura: float) -> float:
    return base * altura
```

### 1.5 Scope (alcance de variables)

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| Local | Variable definida dentro de la función | Solo existe dentro de la función |
| Global | Variable definida fuera de funciones | Accesible desde cualquier lugar |
| `global` | Palabra clave para modificar global | `global contador` |
| Constantes | Por convención, MAYÚSCULAS | `PI = 3.14159` |

### 1.6 Docstrings

| Elemento | Descripción |
|----------|-------------|
| Ubicación | Primera línea después de `def` |
| Sintaxis | Triple comillas `"""..."""` |
| Contenido | Qué hace, args, returns |

```python
def funcion(arg):
    """
    Breve descripción.
    
    Args:
        arg: Descripción del argumento.
    
    Returns:
        Descripción de lo que retorna.
    """
    pass
```

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Función sin argumentos
Crear una función `mostrar_bienvenida` que imprima "Bienvenido a GeoDojo". Llamarla dos veces.

---

#### Ejemplo 2: Función con un argumento
Crear una función `saludar_ciudad` que reciba el nombre de una ciudad e imprima "Bienvenido a [ciudad]".

---

#### Ejemplo 3: Función con múltiples argumentos
Crear una función `mostrar_coordenadas` que reciba nombre, latitud y longitud, y muestre una ficha formateada.

---

#### Ejemplo 4: Función con return
Crear una función `doble` que reciba un número y retorne su doble. Usar el valor retornado en un print.

---

#### Ejemplo 5: Función que calcula y retorna
Crear una función `celsius_a_fahrenheit` que convierta temperatura. Fórmula: F = C × 9/5 + 32

---

#### Ejemplo 6: Función con return condicional
Crear una función `hemisferio` que reciba una latitud y retorne "Norte", "Sur" o "Ecuador" según corresponda.

---

#### Ejemplo 7: Type hints básicos
Reescribir la función `celsius_a_fahrenheit` agregando type hints para los argumentos y el retorno.

---

#### Ejemplo 8: Argumento con valor por defecto
Crear una función `crear_punto` que reciba nombre y coordenadas con valores por defecto (0.0, 0.0).

---

#### Ejemplo 9: Variable local vs global
Demostrar que una variable creada dentro de una función no existe fuera. Usar una constante global RADIO_TIERRA.

---

#### Ejemplo 10: Función con docstring
Crear una función `distancia_al_ecuador` con type hints y docstring completo que documente qué hace, sus argumentos y retorno.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Función sin argumentos

**Enunciado**: Crear una función `mostrar_bienvenida` que imprima "Bienvenido a GeoDojo". Llamarla dos veces.

```python
def mostrar_bienvenida():
    print("Bienvenido a GeoDojo")

mostrar_bienvenida()
mostrar_bienvenida()
```

**Salida**:
```
Bienvenido a GeoDojo
Bienvenido a GeoDojo
```

---

#### Ejemplo 2: Función con un argumento

**Enunciado**: Crear una función `saludar_ciudad` que reciba el nombre de una ciudad e imprima "Bienvenido a [ciudad]".

```python
def saludar_ciudad(ciudad):
    print(f"Bienvenido a {ciudad}")

saludar_ciudad("Mendoza")
saludar_ciudad("Córdoba")
saludar_ciudad("Rosario")
```

**Salida**:
```
Bienvenido a Mendoza
Bienvenido a Córdoba
Bienvenido a Rosario
```

---

#### Ejemplo 3: Función con múltiples argumentos

**Enunciado**: Crear una función `mostrar_coordenadas` que reciba nombre, latitud y longitud, y muestre una ficha formateada.

```python
def mostrar_coordenadas(nombre, latitud, longitud):
    print(f"Lugar: {nombre}")
    print(f"Coordenadas: ({latitud}, {longitud})")
    print("-" * 30)

mostrar_coordenadas("Buenos Aires", -34.6, -58.4)
mostrar_coordenadas("Santiago", -33.4, -70.6)
```

**Salida**:
```
Lugar: Buenos Aires
Coordenadas: (-34.6, -58.4)
------------------------------
Lugar: Santiago
Coordenadas: (-33.4, -70.6)
------------------------------
```

---

#### Ejemplo 4: Función con return

**Enunciado**: Crear una función `doble` que reciba un número y retorne su doble. Usar el valor retornado en un print.

```python
def doble(numero):
    return numero * 2

resultado = doble(25)
print(f"El doble de 25 es {resultado}")

# También se puede usar directamente
print(f"El doble de 100 es {doble(100)}")
```

**Salida**:
```
El doble de 25 es 50
El doble de 100 es 200
```

---

#### Ejemplo 5: Función que calcula y retorna

**Enunciado**: Crear una función `celsius_a_fahrenheit` que convierta temperatura.

```python
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temp_c = 25
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C equivale a {temp_f}°F")

# Temperatura de congelación
print(f"0°C equivale a {celsius_a_fahrenheit(0)}°F")
```

**Salida**:
```
25°C equivale a 77.0°F
0°C equivale a 32.0°F
```

---

#### Ejemplo 6: Función con return condicional

**Enunciado**: Crear una función `hemisferio` que reciba una latitud y retorne "Norte", "Sur" o "Ecuador".

```python
def hemisferio(latitud):
    if latitud > 0:
        return "Norte"
    elif latitud < 0:
        return "Sur"
    else:
        return "Ecuador"

print(f"Nueva York (40.7): {hemisferio(40.7)}")
print(f"Buenos Aires (-34.6): {hemisferio(-34.6)}")
print(f"Quito (0): {hemisferio(0)}")
```

**Salida**:
```
Nueva York (40.7): Norte
Buenos Aires (-34.6): Sur
Quito (0): Ecuador
```

---

#### Ejemplo 7: Type hints básicos

**Enunciado**: Reescribir la función `celsius_a_fahrenheit` con type hints.

```python
def celsius_a_fahrenheit(celsius: float) -> float:
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Los type hints son solo anotaciones, no cambian el comportamiento
temp = celsius_a_fahrenheit(100)
print(f"100°C = {temp}°F")

# Podemos ver las anotaciones
print(f"Anotaciones: {celsius_a_fahrenheit.__annotations__}")
```

**Salida**:
```
100°C = 212.0°F
Anotaciones: {'celsius': <class 'float'>, 'return': <class 'float'>}
```

---

#### Ejemplo 8: Argumento con valor por defecto

**Enunciado**: Crear una función `crear_punto` con coordenadas por defecto.

```python
def crear_punto(nombre, lat=0.0, lon=0.0):
    return f"{nombre}: ({lat}, {lon})"

# Con todos los argumentos
punto1 = crear_punto("Buenos Aires", -34.6, -58.4)
print(punto1)

# Con valores por defecto
punto2 = crear_punto("Origen")
print(punto2)

# Solo latitud
punto3 = crear_punto("Ecuador", 0.0, -78.5)
print(punto3)
```

**Salida**:
```
Buenos Aires: (-34.6, -58.4)
Origen: (0.0, 0.0)
Ecuador: (0.0, -78.5)
```

---

#### Ejemplo 9: Variable local vs global

**Enunciado**: Demostrar scope de variables y uso de constantes globales.

```python
# Constante global (por convención en MAYÚSCULAS)
RADIO_TIERRA = 6371  # km

def circunferencia_tierra():
    # Usamos la constante global
    pi = 3.14159  # variable local
    circunferencia = 2 * pi * RADIO_TIERRA
    return circunferencia

resultado = circunferencia_tierra()
print(f"Circunferencia de la Tierra: {round(resultado, 2)} km")

# RADIO_TIERRA es accesible aquí
print(f"Radio usado: {RADIO_TIERRA} km")

# Pero 'pi' no existe fuera de la función
# print(pi)  # Esto daría NameError
```

**Salida**:
```
Circunferencia de la Tierra: 40030.14 km
Radio usado: 6371 km
```

---

#### Ejemplo 10: Función con docstring

**Enunciado**: Crear una función completa con type hints y docstring.

```python
def distancia_al_ecuador(latitud: float) -> float:
    """
    Calcula la distancia en grados desde una latitud hasta el ecuador.
    
    Args:
        latitud: La latitud del punto en grados decimales.
                 Valores negativos indican hemisferio sur.
    
    Returns:
        La distancia absoluta al ecuador en grados.
    
    Example:
        >>> distancia_al_ecuador(-34.6)
        34.6
    """
    return abs(latitud)

# Usar la función
dist = distancia_al_ecuador(-34.6)
print(f"Buenos Aires está a {dist}° del ecuador")

# Ver la documentación
print("\nDocumentación de la función:")
print(distancia_al_ecuador.__doc__)
```

**Salida**:
```
Buenos Aires está a 34.6° del ecuador

Documentación de la función:

    Calcula la distancia en grados desde una latitud hasta el ecuador.
    
    Args:
        latitud: La latitud del punto en grados decimales.
                 Valores negativos indican hemisferio sur.
    
    Returns:
        La distancia absoluta al ecuador en grados.
    
    Example:
        >>> distancia_al_ecuador(-34.6)
        34.6
    
```

---

## Notas para el docente

- Los ejemplos progresan de funciones simples (solo print) a funciones completas (type hints + docstring)
- Enfatizar la diferencia entre `print` dentro de una función vs `return`
- Demostrar que `return` termina la ejecución de la función
- Los type hints son opcionales pero recomendados para código profesional
- Mostrar el error cuando se intenta acceder a una variable local fuera de la función
- Los ejercicios en `ejercicios/02-funciones.md` refuerzan estos mismos conceptos
- Contexto geográfico consistente: coordenadas, ciudades, temperaturas
