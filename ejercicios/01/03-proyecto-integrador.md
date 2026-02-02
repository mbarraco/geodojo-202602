# Proyecto Integrador: Calculadora de Coordenadas

Un proyecto paso a paso para construir una calculadora que trabaja con puntos geográficos.

---

## Descripción del proyecto

Vamos a construir un programa que:
- Pide al usuario dos puntos geográficos (nombre, latitud, longitud)
- Calcula la distancia entre ellos
- Calcula el punto medio
- Genera links de Google Maps
- Muestra un reporte completo

Este proyecto integra conceptos de las Unidades 1 y 2: variables, tipos, operadores, strings, f-strings, input/output y funciones.

**Nota**: Este proyecto NO usa estructuras de control de flujo (`if/else`, `for`, `while`). Es un programa lineal que se ejecuta de principio a fin.

---

## Paso 1: Pedir el primer punto

**Objetivo**: Pedir al usuario los datos de un punto geográfico (nombre, latitud, longitud) y mostrarlos.

**Ejemplo de ejecución**:
```
=== Punto 1 ===
Nombre del lugar: Buenos Aires
Latitud: -34.6
Longitud: -58.4

Punto 1: Buenos Aires
Coordenadas: (-34.6, -58.4)
```

**Hint**: Usá `input()` para pedir texto y `float()` para convertir las coordenadas a números.

---

## Paso 2: Pedir el segundo punto

**Objetivo**: Agregar el ingreso del segundo punto y mostrar ambos puntos al final.

**Ejemplo de ejecución**:
```
=== Punto 1 ===
Nombre del lugar: Buenos Aires
Latitud: -34.6
Longitud: -58.4

=== Punto 2 ===
Nombre del lugar: Córdoba
Latitud: -31.4
Longitud: -64.2

------------------------------
Punto 1: Buenos Aires (-34.6, -58.4)
Punto 2: Córdoba (-31.4, -64.2)
```

**Hint**: Repetí la estructura del paso 1 pero con variables diferentes (`nombre2`, `lat2`, `lon2`).

---

## Paso 3: Función para calcular distancia

**Objetivo**: Crear una función `distancia_euclidiana` que reciba las coordenadas de dos puntos y retorne la distancia simplificada.

**Fórmula**: distancia = √[(lat2-lat1)² + (lon2-lon1)²]

**Ejemplo de uso**:
```
Distancia: 6.68 grados
Distancia aproximada: 741 km
```

**Hints**:
- La raíz cuadrada se puede calcular con `** 0.5`
- Para convertir grados a km aproximados, multiplicá por 111 (1 grado ≈ 111 km)
- Usá type hints: `def distancia_euclidiana(lat1: float, lon1: float, ...) -> float:`

---

## Paso 4: Función para calcular punto medio

**Objetivo**: Crear una función `punto_medio` que reciba las coordenadas de dos puntos y retorne el punto medio como una tupla.

**Fórmula**: El punto medio es el promedio de las latitudes y el promedio de las longitudes.

**Ejemplo de uso**:
```
Punto medio: (-33.0, -61.3)
```

**Hint**: Retorná una tupla con `return (lat_media, lon_media)`. Después podés acceder a los valores con `resultado[0]` y `resultado[1]`.

---

## Paso 5: Función para generar link de Google Maps

**Objetivo**: Crear una función `generar_link_maps` que reciba latitud y longitud, y retorne un link de Google Maps.

**Formato del link**: `https://www.google.com/maps?q=LATITUD,LONGITUD`

**Ejemplo de uso**:
```
Link: https://www.google.com/maps?q=-34.6,-58.4
```

**Hint**: Usá f-strings para construir la URL.

---

## Paso 6: Función para formatear coordenadas

**Objetivo**: Crear una función `formatear_coordenada` que reciba latitud y longitud, y retorne un string con el formato `34.6°S, 58.4°W`.

**Reglas**:
- Si la latitud es negativa → Sur (S), si es positiva → Norte (N)
- Si la longitud es negativa → Oeste (W), si es positiva → Este (E)
- Mostrar el valor absoluto (sin signo)

**Ejemplo de uso**:
```
Coordenadas: 34.6°S, 58.4°W
```

**Hint avanzado**: Sin usar `if/else`, podés aprovechar que en Python `True` se comporta como `1` y `False` como `0` al multiplicar strings. Por ejemplo: `"S" * (lat < 0)` da `"S"` si lat es negativo, o `""` si no lo es.

---

## Paso 7: Programa completo

**Objetivo**: Integrar todas las funciones en un programa que genera un reporte completo y bien formateado.

**Ejemplo de ejecución completa**:
```
==================================================
       CALCULADORA DE COORDENADAS
==================================================

>>> Ingresá el primer punto:
    Nombre: Buenos Aires
    Latitud: -34.6
    Longitud: -58.4

>>> Ingresá el segundo punto:
    Nombre: Córdoba
    Latitud: -31.4
    Longitud: -64.2

==================================================
                 REPORTE
==================================================

📍 PUNTO 1: Buenos Aires
   Coordenadas: 34.6°S, 58.4°W
   Google Maps: https://www.google.com/maps?q=-34.6,-58.4

📍 PUNTO 2: Córdoba
   Coordenadas: 31.4°S, 64.2°W
   Google Maps: https://www.google.com/maps?q=-31.4,-64.2

📏 DISTANCIA:
   6.68 grados
   ~741 km (aproximado)

📌 PUNTO MEDIO:
   Coordenadas: 33.0°S, 61.3°W
   Google Maps: https://www.google.com/maps?q=-33.0,-61.3

==================================================
         Gracias por usar la calculadora!
==================================================
```

**Hints**:
- Primero definí todas las funciones
- Después pedí los datos al usuario
- Luego hacé todos los cálculos y guardalos en variables
- Finalmente mostrá el reporte usando f-strings
- Podés crear una función `linea(caracter, largo)` para generar las líneas decorativas

---

## Conceptos utilizados

| Concepto | Dónde se usa |
|----------|--------------|
| Variables | Almacenar nombres, coordenadas, resultados |
| Tipos (str, float) | Inputs y cálculos |
| Operadores aritméticos | Distancia, punto medio |
| Operador `**` | Potencia y raíz cuadrada |
| Strings y f-strings | Formateo de salida |
| `input()` / `print()` | Interacción con usuario |
| `abs()` / `round()` | Funciones numéricas |
| Funciones definidas | Encapsular lógica |
| Type hints | Documentar tipos esperados |
| Tuplas | Retornar múltiples valores |

---

## Desafíos extra

1. **Agregar un tercer punto** y calcular las tres distancias entre ellos.

2. **Mejorar la distancia** usando la fórmula de Haversine que considera la curvatura de la Tierra (requiere `import math` e investigar la fórmula).

3. **Calcular el área** de un rectángulo formado por los dos puntos como esquinas opuestas.

4. **Agregar velocidad**: pedir una velocidad en km/h y calcular el tiempo de viaje estimado.

---

*Fin del proyecto integrador - Unidad 1*
