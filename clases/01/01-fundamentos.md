# Clase 1: Fundamentos de Python

Guía para la clase sobre tipos de datos, operadores y funciones básicas.

---

## 1. Temario

### 1.1 Variables y tipos de datos
- Qué es una variable y cómo asignar valores
- Tipos básicos: `str` (texto), `int` (entero), `float` (decimal), `bool` (booleano)
- Función `type()` para inspeccionar tipos
- Convención de nombres: snake_case, nombres descriptivos

### 1.2 Operadores aritméticos
- Básicos: `+`, `-`, `*`, `/`
- División entera: `//`https://www.google.com/maps?q=-34.6037,-58.3816
- Módulo (resto): `%`
- Potenciación: `**`

### 1.3 Funciones numéricas
- `round(valor, decimales)` - redondeo
- `abs(valor)` - valor absoluto
- `int(valor)` - conversión a entero
- `float(valor)` - conversión a decimal

### 1.4 Strings (cadenas de texto)
- Comillas simples o dobles
- Concatenación con `+`
- Repetición con `*`
- f-strings: `f"texto {variable}"`
- Métodos: `.upper()`, `.lower()`, `len()`

### 1.5 Entrada y salida
- `print()` - mostrar en pantalla
- `input()` - pedir datos al usuario
- Conversión de input (siempre devuelve str)

### 1.6 Comparaciones y booleanos
- Operadores: `>`, `<`, `>=`, `<=`, `==`, `!=`
- Operadores lógicos: `and`, `or`, `not`
- Resultados: `True` o `False`

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Variables básicas
Crear variables para almacenar el nombre, latitud y longitud de Buenos Aires. Mostrar cada una.

---

#### Ejemplo 2: Tipos de datos
Usando las variables anteriores, mostrar el tipo de cada una con `type()`.

---

#### Ejemplo 3: Operaciones aritméticas
Calcular el promedio de tres temperaturas: 25.5, 28.3 y 22.1 grados. Mostrar el resultado redondeado a 1 decimal.

---

#### Ejemplo 4: Potenciación y raíz cuadrada
Dado un terreno cuadrado de 150 m de lado, calcular:
- El área (lado²)
- La diagonal (lado × √2, usando potenciación)

---

#### Ejemplo 5: División entera y módulo
Un vuelo de 2750 km se divide en tramos de 400 km. Calcular cuántos tramos completos hay y cuántos km quedan.

---

#### Ejemplo 6: Strings y concatenación
Crear variables para país y ciudad. Mostrar el texto "Ciudad: [ciudad], País: [país]" de dos formas: con `+` y con f-string.

---

#### Ejemplo 7: Métodos de string
Dado el nombre "cerro aconcagua", mostrarlo en mayúsculas, en formato título (primera letra de cada palabra en mayúscula), y mostrar su longitud.

---

#### Ejemplo 8: Input y conversión
Pedir al usuario una latitud, convertirla a número, y mostrar su valor absoluto (para saber la distancia al ecuador).

---

#### Ejemplo 9: Comparaciones simples
Dadas dos altitudes (Aconcagua: 6962 m, Everest: 8849 m), mostrar:
- ¿Es Aconcagua más alto que 6000?
- ¿Son iguales?
- ¿Cuál es más alto?

---

#### Ejemplo 10: Booleanos y operadores lógicos
Verificar si las coordenadas (-34.6, -58.4) representan un punto válido:
- Latitud entre -90 y 90
- Longitud entre -180 y 180
Mostrar si ambas condiciones se cumplen.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Variables básicas

**Enunciado**: Crear variables para almacenar el nombre, latitud y longitud de Buenos Aires. Mostrar cada una.

```python
nombre = "Buenos Aires"
latitud = -34.6
longitud = -58.4

print(nombre)
print(latitud)
print(longitud)
```

**Salida**:
```
Buenos Aires
-34.6
-58.4
```

---

#### Ejemplo 2: Tipos de datos

**Enunciado**: Usando las variables anteriores, mostrar el tipo de cada una con `type()`.

```python
nombre = "Buenos Aires"
latitud = -34.6
longitud = -58.4

print(type(nombre))
print(type(latitud))
print(type(longitud))
```

**Salida**:
```
<class 'str'>
<class 'float'>
<class 'float'>
```

---

#### Ejemplo 3: Operaciones aritméticas

**Enunciado**: Calcular el promedio de tres temperaturas: 25.5, 28.3 y 22.1 grados. Mostrar el resultado redondeado a 1 decimal.

```python
temp1 = 25.5
temp2 = 28.3
temp3 = 22.1

promedio = (temp1 + temp2 + temp3) / 3
promedio_redondeado = round(promedio, 1)

print(f"Promedio: {promedio_redondeado}°C")
```

**Salida**:
```
Promedio: 25.3°C
```

---

#### Ejemplo 4: Potenciación y raíz cuadrada

**Enunciado**: Dado un terreno cuadrado de 150 m de lado, calcular el área (lado²) y la diagonal (lado × √2).

```python
lado = 150

area = lado ** 2
diagonal = lado * (2 ** 0.5)  # raíz de 2 = 2^0.5

print(f"Área: {area} m²")
print(f"Diagonal: {round(diagonal, 2)} m")
```

**Salida**:
```
Área: 22500 m²
Diagonal: 212.13 m
```

---

#### Ejemplo 5: División entera y módulo

**Enunciado**: Un vuelo de 2750 km se divide en tramos de 400 km. Calcular cuántos tramos completos hay y cuántos km quedan.

```python
distancia_total = 2750
km_por_tramo = 400

tramos_completos = distancia_total // km_por_tramo
km_restantes = distancia_total % km_por_tramo

print(f"Tramos completos: {tramos_completos}")
print(f"Km restantes: {km_restantes}")
```

**Salida**:
```
Tramos completos: 6
Km restantes: 350
```

---

#### Ejemplo 6: Strings y concatenación

**Enunciado**: Crear variables para país y ciudad. Mostrar el texto "Ciudad: [ciudad], País: [país]" de dos formas.

```python
pais = "Argentina"
ciudad = "Mendoza"

# Forma 1: concatenación con +
mensaje1 = "Ciudad: " + ciudad + ", País: " + pais
print(mensaje1)

# Forma 2: f-string (recomendada)
mensaje2 = f"Ciudad: {ciudad}, País: {pais}"
print(mensaje2)
```

**Salida**:
```
Ciudad: Mendoza, País: Argentina
Ciudad: Mendoza, País: Argentina
```

---

#### Ejemplo 7: Métodos de string

**Enunciado**: Dado el nombre "cerro aconcagua", mostrarlo en mayúsculas, en formato título, y mostrar su longitud.

```python
nombre = "cerro aconcagua"

print(nombre.upper())       # MAYÚSCULAS
print(nombre.title())       # Formato Título
print(len(nombre))          # Longitud (cantidad de caracteres)
```

**Salida**:
```
CERRO ACONCAGUA
Cerro Aconcagua
15
```

---

#### Ejemplo 8: Input y conversión

**Enunciado**: Pedir al usuario una latitud, convertirla a número, y mostrar su valor absoluto.

```python
entrada = input("Ingresá una latitud: ")
latitud = float(entrada)
distancia_ecuador = abs(latitud)

print(f"Distancia al ecuador: {distancia_ecuador} grados")
```

**Ejemplo de ejecución**:
```
Ingresá una latitud: -34.6
Distancia al ecuador: 34.6 grados
```

---

#### Ejemplo 9: Comparaciones simples

**Enunciado**: Dadas dos altitudes, mostrar comparaciones.

```python
aconcagua = 6962
everest = 8849

print(f"¿Aconcagua > 6000? {aconcagua > 6000}")
print(f"¿Son iguales? {aconcagua == everest}")
print(f"¿Everest es más alto? {everest > aconcagua}")
```

**Salida**:
```
¿Aconcagua > 6000? True
¿Son iguales? False
¿Everest es más alto? True
```

---

#### Ejemplo 10: Booleanos y operadores lógicos

**Enunciado**: Verificar si las coordenadas (-34.6, -58.4) son válidas.

```python
latitud = -34.6
longitud = -58.4

lat_valida = latitud >= -90 and latitud <= 90
lon_valida = longitud >= -180 and longitud <= 180
coordenadas_validas = lat_valida and lon_valida

print(f"Latitud válida: {lat_valida}")
print(f"Longitud válida: {lon_valida}")
print(f"Coordenadas válidas: {coordenadas_validas}")
```

**Salida**:
```
Latitud válida: True
Longitud válida: True
Coordenadas válidas: True
```

---

## Notas para el docente

- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Cada ejemplo introduce 1-2 conceptos nuevos de forma incremental
- Se recomienda pedir participación: "¿Qué tipo creen que tiene esta variable?"
- Los ejercicios en `ejercicios/01-fundamentos.md` refuerzan estos mismos conceptos
- Contexto geográfico consistente: coordenadas, ciudades, distancias
