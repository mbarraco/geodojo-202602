# Clase 2: Estructuras de datos y control de flujo

Guía para la clase sobre listas, tuplas, diccionarios, condicionales y bucles.

---

## 1. Temario

### 1.1 Listas

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Crear lista | Colección ordenada y mutable | `ciudades = ["BA", "Cba"]` |
| Acceso por índice | Primer elemento: 0, último: -1 | `ciudades[0]` → `"BA"` |
| `len()` | Cantidad de elementos | `len(ciudades)` → `2` |
| `append()` | Agregar elemento al final | `ciudades.append("Mza")` |
| `insert()` | Insertar en posición específica | `ciudades.insert(0, "Ros")` |
| `remove()` | Eliminar por valor | `ciudades.remove("BA")` |
| `pop()` | Eliminar por índice (retorna el valor) | `ciudades.pop(0)` |
| Slicing | Sublista | `ciudades[1:3]` |

### 1.2 Tuplas

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Crear tupla | Colección ordenada e inmutable | `punto = (-34.6, -58.4)` |
| Acceso | Igual que listas | `punto[0]` → `-34.6` |
| Desempaquetado | Asignar elementos a variables | `lat, lon = punto` |
| Inmutabilidad | No se pueden modificar | `punto[0] = 0` → Error |
| Uso común | Coordenadas, datos que no cambian | `rgb = (255, 128, 0)` |

### 1.3 Diccionarios

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Crear diccionario | Pares clave-valor | `ciudad = {"nombre": "BA", "lat": -34.6}` |
| Acceso por clave | Obtener valor | `ciudad["nombre"]` → `"BA"` |
| `.get()` | Acceso seguro (no da error) | `ciudad.get("pob", 0)` → `0` |
| Agregar/modificar | Asignar a clave | `ciudad["pob"] = 3000000` |
| `.keys()` | Obtener claves | `ciudad.keys()` |
| `.values()` | Obtener valores | `ciudad.values()` |
| `.items()` | Obtener pares (clave, valor) | `ciudad.items()` |
| `del` | Eliminar clave | `del ciudad["pob"]` |

### 1.4 Condicionales

| Estructura | Descripción | Ejemplo |
|------------|-------------|---------|
| `if` | Ejecuta si condición es True | `if lat < 0:` |
| `else` | Ejecuta si condición es False | `else:` |
| `elif` | Condición alternativa | `elif lat == 0:` |
| Condición compuesta | Combinar con `and`, `or` | `if lat > -90 and lat < 90:` |
| Operador ternario | Condicional en una línea | `"Sur" if lat < 0 else "Norte"` |

### 1.5 Bucles for

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Iterar lista | Recorrer elementos | `for ciudad in ciudades:` |
| `range()` | Secuencia de números | `for i in range(5):` → 0,1,2,3,4 |
| `range(a, b)` | Desde a hasta b-1 | `for i in range(1, 6):` → 1,2,3,4,5 |
| `range(a, b, step)` | Con paso | `for i in range(0, 10, 2):` → 0,2,4,6,8 |
| `enumerate()` | Índice y valor | `for i, c in enumerate(ciudades):` |
| Iterar string | Recorrer caracteres | `for letra in "Hola":` |
| Iterar diccionario | Recorrer claves | `for clave in dicc:` |

### 1.6 Bucles while

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| `while` | Repite mientras condición sea True | `while contador < 5:` |
| Contador | Variable que controla el bucle | `contador += 1` |
| `break` | Sale del bucle inmediatamente | `if encontrado: break` |
| `continue` | Salta a la siguiente iteración | `if invalido: continue` |
| Bucle infinito | Condición siempre True (¡cuidado!) | `while True:` (necesita `break`) |

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Crear y manipular una lista
Crear una lista con 3 ciudades argentinas. Mostrar la lista, agregar una cuarta ciudad, y mostrar cuántas ciudades hay.

---

#### Ejemplo 2: Acceso a elementos de lista
Dada una lista de 5 provincias, mostrar la primera, la última, y las del medio (de la segunda a la cuarta).

---

#### Ejemplo 3: Tupla de coordenadas
Crear una tupla con las coordenadas de Ushuaia (-54.8, -68.3). Desempaquetar los valores en variables separadas y mostrar cada una.

---

#### Ejemplo 4: Diccionario de una ciudad
Crear un diccionario con información de Córdoba: nombre, latitud, longitud y población. Mostrar el nombre y agregar una nueva clave "provincia".

---

#### Ejemplo 5: Clasificar con if-elif-else
Dada una altitud en metros, clasificarla como "baja" (< 500), "media" (500-2000), o "alta" (> 2000).

---

#### Ejemplo 6: Validar coordenadas
Dada una latitud, verificar si es válida (entre -90 y 90). Si es válida, determinar si está en el hemisferio norte o sur.

---

#### Ejemplo 7: Recorrer lista con for
Dada una lista de temperaturas, recorrerla y mostrar cada temperatura con su número de orden.

---

#### Ejemplo 8: Sumar con bucle for
Dada una lista de distancias entre ciudades, calcular la distancia total usando un bucle for.

---

#### Ejemplo 9: Buscar con while
Dada una lista de altitudes, usar un bucle while para encontrar la primera altitud mayor a 3000 metros.

---

#### Ejemplo 10: Filtrar con for y continue
Dada una lista de coordenadas (algunas inválidas con valor 0), mostrar solo las coordenadas válidas usando continue para saltar las inválidas.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Crear y manipular una lista

**Enunciado**: Crear una lista con 3 ciudades argentinas. Mostrar la lista, agregar una cuarta ciudad, y mostrar cuántas ciudades hay.

```python
ciudades = ["Buenos Aires", "Córdoba", "Rosario"]
print(ciudades)

ciudades.append("Mendoza")
print(ciudades)

cantidad = len(ciudades)
print(f"Total de ciudades: {cantidad}")
```

**Salida**:
```
['Buenos Aires', 'Córdoba', 'Rosario']
['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza']
Total de ciudades: 4
```

---

#### Ejemplo 2: Acceso a elementos de lista

**Enunciado**: Dada una lista de 5 provincias, mostrar la primera, la última, y las del medio (de la segunda a la cuarta).

```python
provincias = ["Mendoza", "Salta", "Jujuy", "Tucumán", "Córdoba"]

print(f"Primera: {provincias[0]}")
print(f"Última: {provincias[-1]}")
print(f"Del medio: {provincias[1:4]}")
```

**Salida**:
```
Primera: Mendoza
Última: Córdoba
Del medio: ['Salta', 'Jujuy', 'Tucumán']
```

---

#### Ejemplo 3: Tupla de coordenadas

**Enunciado**: Crear una tupla con las coordenadas de Ushuaia (-54.8, -68.3). Desempaquetar los valores en variables separadas y mostrar cada una.

```python
ushuaia = (-54.8, -68.3)
print(f"Coordenadas: {ushuaia}")

latitud, longitud = ushuaia
print(f"Latitud: {latitud}")
print(f"Longitud: {longitud}")
```

**Salida**:
```
Coordenadas: (-54.8, -68.3)
Latitud: -54.8
Longitud: -68.3
```

---

#### Ejemplo 4: Diccionario de una ciudad

**Enunciado**: Crear un diccionario con información de Córdoba: nombre, latitud, longitud y población. Mostrar el nombre y agregar una nueva clave "provincia".

```python
cordoba = {
    "nombre": "Córdoba",
    "latitud": -31.4,
    "longitud": -64.2,
    "poblacion": 1430000
}

print(f"Ciudad: {cordoba['nombre']}")

cordoba["provincia"] = "Córdoba"
print(cordoba)
```

**Salida**:
```
Ciudad: Córdoba
{'nombre': 'Córdoba', 'latitud': -31.4, 'longitud': -64.2, 'poblacion': 1430000, 'provincia': 'Córdoba'}
```

---

#### Ejemplo 5: Clasificar con if-elif-else

**Enunciado**: Dada una altitud en metros, clasificarla como "baja" (< 500), "media" (500-2000), o "alta" (> 2000).

```python
altitud = 1500

if altitud < 500:
    clasificacion = "baja"
elif altitud <= 2000:
    clasificacion = "media"
else:
    clasificacion = "alta"

print(f"Altitud {altitud}m: zona {clasificacion}")
```

**Salida**:
```
Altitud 1500m: zona media
```

---

#### Ejemplo 6: Validar coordenadas

**Enunciado**: Dada una latitud, verificar si es válida (entre -90 y 90). Si es válida, determinar si está en el hemisferio norte o sur.

```python
latitud = -34.6

if latitud < -90 or latitud > 90:
    print("Latitud inválida")
else:
    print("Latitud válida")
    if latitud < 0:
        print("Hemisferio Sur")
    elif latitud > 0:
        print("Hemisferio Norte")
    else:
        print("Línea del Ecuador")
```

**Salida**:
```
Latitud válida
Hemisferio Sur
```

---

#### Ejemplo 7: Recorrer lista con for

**Enunciado**: Dada una lista de temperaturas, recorrerla y mostrar cada temperatura con su número de orden.

```python
temperaturas = [22.5, 25.0, 18.3, 28.1]

for i, temp in enumerate(temperaturas, start=1):
    print(f"Día {i}: {temp}°C")
```

**Salida**:
```
Día 1: 22.5°C
Día 2: 25.0°C
Día 3: 18.3°C
Día 4: 28.1°C
```

---

#### Ejemplo 8: Sumar con bucle for

**Enunciado**: Dada una lista de distancias entre ciudades, calcular la distancia total usando un bucle for.

```python
distancias = [300, 450, 200, 380]  # km entre ciudades

total = 0
for d in distancias:
    total += d

print(f"Distancia total del recorrido: {total} km")
```

**Salida**:
```
Distancia total del recorrido: 1330 km
```

---

#### Ejemplo 9: Buscar con while

**Enunciado**: Dada una lista de altitudes, usar un bucle while para encontrar la primera altitud mayor a 3000 metros.

```python
altitudes = [1200, 2500, 800, 3500, 4200, 1800]

i = 0
encontrada = False

while i < len(altitudes) and not encontrada:
    if altitudes[i] > 3000:
        print(f"Primera altitud > 3000m: {altitudes[i]}m (posición {i})")
        encontrada = True
    i += 1

if not encontrada:
    print("No se encontró ninguna altitud mayor a 3000m")
```

**Salida**:
```
Primera altitud > 3000m: 3500m (posición 3)
```

---

#### Ejemplo 10: Filtrar con for y continue

**Enunciado**: Dada una lista de coordenadas (algunas inválidas con valor 0), mostrar solo las coordenadas válidas usando continue para saltar las inválidas.

```python
coordenadas = [
    (-34.6, -58.4),
    (0, 0),          # inválida
    (-31.4, -64.2),
    (0, 0),          # inválida
    (-32.9, -68.8)
]

print("Coordenadas válidas:")
for lat, lon in coordenadas:
    if lat == 0 and lon == 0:
        continue  # saltar esta iteración
    print(f"  ({lat}, {lon})")
```

**Salida**:
```
Coordenadas válidas:
  (-34.6, -58.4)
  (-31.4, -64.2)
  (-32.9, -68.8)
```

---

## Notas para el docente
- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Cada ejemplo introduce 1-2 conceptos nuevos de forma incremental
- Se recomienda pedir participación: "¿Qué valor tiene la lista ahora?" o "¿Qué pasa si cambio esta condición?"
- Los ejercicios en `ejercicios/02/01-estructuras-control.md` refuerzan estos mismos conceptos
- Contexto geográfico consistente: ciudades, coordenadas, altitudes, temperaturas
- Los temas se presentan en orden: primero estructuras de datos (listas, tuplas, diccionarios), luego control de flujo (condicionales, bucles)
- Para los bucles, mostrar primero `for` (más común) y luego `while` (para casos específicos)
