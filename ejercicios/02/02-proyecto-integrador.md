# Proyecto Integrador: Planificador de Ruta Geográfica

Un proyecto paso a paso para construir un programa interactivo que gestiona rutas de viaje con múltiples destinos.

---

## Descripción del proyecto

Vamos a construir un programa que:
- Permite agregar destinos a una ruta (con validación de coordenadas)
- Muestra la lista de destinos de la ruta
- Calcula la distancia total del recorrido
- Genera estadísticas (destino más al norte, más al sur, etc.)
- Permite eliminar destinos
- Usa un menú interactivo que se repite hasta que el usuario decida salir

Este proyecto integra conceptos de la Unidad 2: listas, tuplas, diccionarios, condicionales y bucles. También reutiliza funciones de la Unidad 1.

---

## Paso 1: Estructura de datos básica

**Objetivo**: Crear la estructura de datos para almacenar la ruta. Usaremos una lista de diccionarios, donde cada diccionario representa un destino.

**Tareas**:
1. Crear una lista vacía llamada `ruta`
2. Crear un diccionario de ejemplo con nombre, latitud y longitud
3. Agregar el diccionario a la lista
4. Mostrar la lista

**Ejemplo de código**:
```python
# Lista para almacenar los destinos
ruta = []

# Un destino es un diccionario
destino = {
    "nombre": "Buenos Aires",
    "lat": -34.6,
    "lon": -58.4
}

# Agregar a la ruta
ruta.append(destino)

print(ruta)
```

**Salida esperada**:
```
[{'nombre': 'Buenos Aires', 'lat': -34.6, 'lon': -58.4}]
```

---

## Paso 2: Función para validar coordenadas

**Objetivo**: Crear una función que verifique si las coordenadas son válidas antes de agregar un destino.

**Reglas**:
- Latitud válida: entre -90 y 90
- Longitud válida: entre -180 y 180

**Tareas**:
1. Crear función `es_coordenada_valida(lat, lon)` que retorne `True` o `False`
2. Probarla con coordenadas válidas e inválidas

**Ejemplo de uso**:
```python
print(es_coordenada_valida(-34.6, -58.4))  # True
print(es_coordenada_valida(-100, 50))       # False (latitud inválida)
print(es_coordenada_valida(45, 200))        # False (longitud inválida)
```

**Hint**: Usá `and` para combinar las dos condiciones (latitud válida Y longitud válida).

---

## Paso 3: Función para agregar destino

**Objetivo**: Crear una función que pida los datos de un destino al usuario, los valide, y lo agregue a la ruta.

**Tareas**:
1. Crear función `agregar_destino(ruta)` que modifique la lista recibida
2. Pedir nombre, latitud y longitud al usuario
3. Validar las coordenadas antes de agregar
4. Si son inválidas, mostrar mensaje de error y no agregar

**Ejemplo de ejecución**:
```
Nombre del destino: Córdoba
Latitud: -31.4
Longitud: -64.2
✓ Destino "Córdoba" agregado a la ruta!
```

```
Nombre del destino: Lugar Inválido
Latitud: -100
Longitud: 50
✗ Coordenadas inválidas. El destino no fue agregado.
```

**Hint**: Usá `if` para verificar si las coordenadas son válidas antes de hacer `append()`.

---

## Paso 4: Función para mostrar la ruta

**Objetivo**: Crear una función que muestre todos los destinos de la ruta, numerados.

**Tareas**:
1. Crear función `mostrar_ruta(ruta)`
2. Si la ruta está vacía, mostrar un mensaje apropiado
3. Si tiene destinos, mostrarlos numerados con `enumerate()`

**Ejemplo de ejecución** (con 3 destinos):
```
=== RUTA ACTUAL (3 destinos) ===
1. Buenos Aires (-34.6, -58.4)
2. Córdoba (-31.4, -64.2)
3. Mendoza (-32.9, -68.8)
```

**Ejemplo de ejecución** (sin destinos):
```
La ruta está vacía. Agregá destinos para comenzar.
```

**Hint**: Usá `len(ruta) == 0` o simplemente `not ruta` para verificar si está vacía.

---

## Paso 5: Función para calcular distancia entre dos puntos

**Objetivo**: Crear (o reutilizar de la Unidad 1) una función que calcule la distancia entre dos coordenadas.

**Fórmula euclidiana simplificada**:
```
distancia = √[(lat2-lat1)² + (lon2-lon1)²]
```

**Tareas**:
1. Crear función `distancia_entre(lat1, lon1, lat2, lon2)` que retorne la distancia en grados
2. Opcionalmente, convertir a km aproximados (1 grado ≈ 111 km)

**Ejemplo de uso**:
```python
d = distancia_entre(-34.6, -58.4, -31.4, -64.2)
print(f"Distancia: {round(d, 2)} grados")
print(f"Distancia aproximada: {round(d * 111)} km")
```

**Salida esperada**:
```
Distancia: 6.68 grados
Distancia aproximada: 741 km
```

---

## Paso 6: Función para calcular distancia total de la ruta

**Objetivo**: Crear una función que recorra la lista de destinos y sume las distancias entre puntos consecutivos.

**Tareas**:
1. Crear función `distancia_total(ruta)` que retorne la distancia total
2. Usar un bucle `for` para recorrer los destinos
3. Sumar la distancia entre cada par de destinos consecutivos

**Ejemplo de uso** (con Buenos Aires → Córdoba → Mendoza):
```python
total = distancia_total(ruta)
print(f"Distancia total: {round(total * 111)} km")
```

**Salida esperada**:
```
Distancia total: 1194 km
```

**Hint**: Recorré con `range(len(ruta) - 1)` para acceder a pares consecutivos: `ruta[i]` y `ruta[i+1]`.

---

## Paso 7: Función para encontrar extremos

**Objetivo**: Crear una función que encuentre el destino más al norte y más al sur de la ruta.

**Tareas**:
1. Crear función `encontrar_extremos(ruta)` que retorne una tupla con dos diccionarios: (más_norte, más_sur)
2. Recorrer la ruta con un bucle y comparar latitudes
3. Si la ruta está vacía, retornar `(None, None)`

**Ejemplo de uso**:
```python
norte, sur = encontrar_extremos(ruta)
print(f"Más al norte: {norte['nombre']} (lat: {norte['lat']})")
print(f"Más al sur: {sur['nombre']} (lat: {sur['lat']})")
```

**Salida esperada** (con Buenos Aires, Córdoba, Mendoza):
```
Más al norte: Córdoba (lat: -31.4)
Más al sur: Buenos Aires (lat: -34.6)
```

**Hint**: Recordá que en el hemisferio sur, una latitud mayor (menos negativa) está más al norte.

---

## Paso 8: Función para eliminar destino

**Objetivo**: Crear una función que permita eliminar un destino de la ruta por su nombre.

**Tareas**:
1. Crear función `eliminar_destino(ruta, nombre)`
2. Buscar el destino con ese nombre usando un bucle
3. Si lo encuentra, eliminarlo y mostrar confirmación
4. Si no lo encuentra, mostrar mensaje de error

**Ejemplo de ejecución**:
```
Eliminar destino: Córdoba
✓ "Córdoba" eliminado de la ruta.
```

```
Eliminar destino: Lima
✗ No se encontró "Lima" en la ruta.
```

**Hint**: Podés usar `break` para salir del bucle una vez que encontrás el destino.

---

## Paso 9: Menú interactivo

**Objetivo**: Crear un menú que se repita hasta que el usuario elija salir, usando un bucle `while`.

**Opciones del menú**:
1. Agregar destino
2. Ver ruta
3. Calcular distancia total
4. Ver estadísticas (extremos)
5. Eliminar destino
6. Salir

**Estructura básica**:
```python
while True:
    print("\n=== MENÚ ===")
    print("1. Agregar destino")
    print("2. Ver ruta")
    # ... más opciones
    print("6. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        agregar_destino(ruta)
    elif opcion == "2":
        mostrar_ruta(ruta)
    # ... más opciones
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
```

**Hint**: Usá `break` para salir del bucle cuando el usuario elige la opción de salir.

---

## Paso 10: Programa completo

**Objetivo**: Integrar todas las funciones en un programa completo con un reporte final bien formateado.

**Ejemplo de ejecución completa**:
```
╔════════════════════════════════════════════════════╗
║        PLANIFICADOR DE RUTA GEOGRÁFICA             ║
╚════════════════════════════════════════════════════╝

=== MENÚ ===
1. Agregar destino
2. Ver ruta
3. Calcular distancia total
4. Ver estadísticas
5. Eliminar destino
6. Generar reporte final
7. Salir

Opción: 1
Nombre del destino: Buenos Aires
Latitud: -34.6
Longitud: -58.4
✓ Destino "Buenos Aires" agregado a la ruta!

Opción: 1
Nombre del destino: Córdoba
Latitud: -31.4
Longitud: -64.2
✓ Destino "Córdoba" agregado a la ruta!

Opción: 1
Nombre del destino: Mendoza
Latitud: -32.9
Longitud: -68.8
✓ Destino "Mendoza" agregado a la ruta!

Opción: 2
=== RUTA ACTUAL (3 destinos) ===
1. Buenos Aires (-34.6, -58.4)
2. Córdoba (-31.4, -64.2)
3. Mendoza (-32.9, -68.8)

Opción: 3
=== DISTANCIA TOTAL ===
Tramos:
  Buenos Aires → Córdoba: 741 km
  Córdoba → Mendoza: 485 km
Distancia total: 1226 km

Opción: 4
=== ESTADÍSTICAS ===
Destino más al norte: Córdoba (lat: -31.4)
Destino más al sur: Buenos Aires (lat: -34.6)
Cantidad de destinos: 3

Opción: 6
╔════════════════════════════════════════════════════╗
║               REPORTE FINAL DE RUTA                ║
╚════════════════════════════════════════════════════╝

📍 DESTINOS (3):
   1. Buenos Aires
      Coordenadas: 34.6°S, 58.4°W
      Maps: https://www.google.com/maps?q=-34.6,-58.4

   2. Córdoba
      Coordenadas: 31.4°S, 64.2°W
      Maps: https://www.google.com/maps?q=-31.4,-64.2

   3. Mendoza
      Coordenadas: 32.9°S, 68.8°W
      Maps: https://www.google.com/maps?q=-32.9,-68.8

📏 DISTANCIA TOTAL: ~1226 km

📊 ESTADÍSTICAS:
   Más al norte: Córdoba
   Más al sur: Buenos Aires

╚════════════════════════════════════════════════════╝
         ¡Buen viaje!
╚════════════════════════════════════════════════════╝

Opción: 7
¡Hasta luego! Gracias por usar el Planificador de Ruta.
```

---

## Conceptos utilizados

| Concepto | Dónde se usa |
|----------|--------------|
| **Listas** | `ruta` almacena todos los destinos |
| **Diccionarios** | Cada destino es `{"nombre": ..., "lat": ..., "lon": ...}` |
| **Tuplas** | Retorno de `encontrar_extremos()` |
| **`if/elif/else`** | Validación de coordenadas, menú de opciones |
| **`for`** | Recorrer destinos, calcular distancia total |
| **`while`** | Menú interactivo que se repite |
| **`break`** | Salir del menú, terminar búsqueda |
| **`enumerate()`** | Numerar destinos al mostrar la ruta |
| **`range()`** | Acceder a pares consecutivos de destinos |
| **`len()`** | Verificar si la ruta está vacía, contar destinos |
| **`.append()`** | Agregar destinos a la ruta |
| **`.items()`** | Recorrer diccionarios (opcional) |

---

## Desafíos extra

1. **Reordenar destinos**: Agregar opción para mover un destino a otra posición en la ruta.

2. **Tiempo de viaje**: Pedir velocidad promedio en km/h y calcular el tiempo estimado de viaje para toda la ruta.

3. **Par más cercano**: Encontrar cuáles dos destinos de la ruta están más cerca entre sí.

4. **Búsqueda parcial**: Permitir buscar destinos por nombre parcial (ej: "Bue" encuentra "Buenos Aires").

5. **Ruta circular**: Agregar opción para calcular la distancia si se vuelve al punto de origen (ruta circular).

6. **Exportar ruta**: Generar una lista de todos los links de Google Maps para compartir.

7. **Cargar datos iniciales**: Iniciar el programa con una lista de ciudades argentinas precargadas y permitir seleccionar de esa lista.

---

## Conexión con la Unidad 1

Este proyecto es una evolución del **Proyecto Integrador de la Unidad 1** (Calculadora de Coordenadas):

| Unidad 1 | Unidad 2 |
|----------|----------|
| 2 puntos fijos | N puntos dinámicos |
| Programa lineal | Programa interactivo con menú |
| Sin validación (asume datos correctos) | Valida coordenadas antes de agregar |
| Variables simples | Listas de diccionarios |
| Una sola ejecución | Se repite hasta que el usuario salga |

Podés reutilizar las funciones de la Unidad 1:
- `distancia_euclidiana()` → `distancia_entre()`
- `formatear_coordenada()`
- `generar_link_maps()`

---

*Fin del proyecto integrador - Unidad 2*
