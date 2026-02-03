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

Este proyecto integra conceptos de la Unidad 1: variables, tipos, operadores, strings, f-strings, input/output y funciones.

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

**Ejemplo de ejecución**:
```
Distancia: 6.68 grados
Distancia aproximada: 741 km

```

**Hint**: - La raíz cuadrada se puede calcular con `** 0.5`
- Para convertir grados a km aproximados, multiplicá por 111 (1 grado ≈ 111 km)
- Usá type hints: `def distancia_euclidiana(lat1: float, lon1: float, ...) -> float:`
- Fórmula: distancia = √[(lat2-lat1)² + (lon2-lon1)²]

---

## Paso 4: Función para calcular punto medio

**Objetivo**: Crear una función `punto_medio` que reciba las coordenadas de dos puntos y retorne el punto medio como una tupla.

**Ejemplo de ejecución**:
```
Punto medio: (-33.0, -61.3)

```

**Hint**: Retorná una tupla con `return (lat_media, lon_media)`. Después podés acceder a los valores con `resultado[0]` y `resultado[1]`.

---

## Paso 5: Función para generar link de Google Maps

**Objetivo**: Crear una función `generar_link_maps` que reciba latitud y longitud y retorne un link de Google Maps.

**Ejemplo de ejecución**:
```
Link Buenos Aires: https://www.google.com/maps?q=-34.6,-58.4
Link Córdoba: https://www.google.com/maps?q=-31.4,-64.2

```

**Hint**: El formato del link es: `https://www.google.com/maps?q={lat},{lon}`

---

## Paso 6: Función para formatear coordenadas

**Objetivo**: Crear una función `formatear_coordenada` que reciba lat/lon y retorne un string con formato cardinal (N/S, E/W).

**Ejemplo de ejecución**:
```
Buenos Aires: 34.6°S, 58.4°W
Nueva York: 40.7°N, 74.0°W

```

**Hint**: Usá `abs()` para el valor absoluto y determiná la dirección según el signo.

---

## Paso 7: Reporte final completo

**Objetivo**: Integrar todo en un programa con salida bien formateada.

**Ejemplo de ejecución**:
```
============================================
      CALCULADORA DE COORDENADAS
============================================

=== Punto 1 ===
Nombre del lugar: Buenos Aires
Latitud: -34.6
Longitud: -58.4

=== Punto 2 ===
Nombre del lugar: Córdoba
Latitud: -31.4
Longitud: -64.2

============================================
              RESULTADOS
============================================

Punto 1: Buenos Aires (34.6°S, 58.4°W)
Punto 2: Córdoba (31.4°S, 64.2°W)

Distancia: 6.68 grados (~741 km)
Punto medio: 33.0°S, 61.3°W

Links de Google Maps:
- Buenos Aires: https://www.google.com/maps?q=-34.6,-58.4
- Córdoba: https://www.google.com/maps?q=-31.4,-64.2
- Punto medio: https://www.google.com/maps?q=-33.0,-61.3

============================================

```

---

## Conceptos utilizados

| Concepto | Dónde se usa |
|----------|--------------|
| Variables y tipos | Almacenar nombres, latitudes, longitudes |
| Operadores aritméticos | Cálculo de distancia y punto medio |
| f-strings | Formatear el reporte y los links |
| input() y print() | Entrada de datos y salida del reporte |
| Funciones con parámetros | distancia_euclidiana(), punto_medio(), etc. |
| return y tuplas | Retornar múltiples valores desde punto_medio() |
| Type hints | Documentar tipos en las funciones |

---

## Desafíos extra
1. Agregar validación básica: verificar que latitud esté entre -90 y 90, y longitud entre -180 y 180
2. Calcular el rumbo inicial entre los dos puntos (requiere investigar fórmulas de navegación)
3. Agregar un tercer punto y calcular el centroide del triángulo
4. Convertir la distancia a otras unidades (millas náuticas, millas terrestres)
5. Agregar docstrings completos a todas las funciones
6. Crear una función que genere un link de Google Maps con marcadores para ambos puntos

---

*Fin del proyecto integrador - Unidad 1*
