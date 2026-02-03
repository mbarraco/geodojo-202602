# Unidad 1: Fundamentos de Python

Ejercicios sobre tipos de datos, operadores y funciones básicas.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Variables y print

---

### A1. Mi primera ciudad

**Enunciado**: Creá una variable llamada `ciudad` que contenga el nombre "Mendoza" y mostrala por pantalla usando `print()`.

**Ejemplo**:
- Salida esperada: `Mendoza`

**Hint**: Usá comillas para definir un texto (string).

---

### A2. Latitud de Buenos Aires

**Enunciado**: La latitud de Buenos Aires es aproximadamente -34.6. Guardá este valor en una variable llamada `latitud` y mostralo por pantalla.

**Ejemplo**:
- Salida esperada: `-34.6`

**Hint**: Los números decimales no llevan comillas.

---

### A3. Coordenadas completas

**Enunciado**: Guardá la latitud (-34.6) y la longitud (-58.4) de Buenos Aires en dos variables separadas. Luego mostrá ambas usando dos `print()`.

**Ejemplo**:
- Salida esperada:
  ```
  -34.6
  -58.4
  ```

---

### A4. Datos de una ubicación

**Enunciado**: Creá tres variables para representar un punto geográfico:
- `nombre`: "Cerro Aconcagua"
- `latitud`: -32.65
- `longitud`: -70.01
Mostrá las tres variables, una por línea.

**Ejemplo**:
- Salida esperada:
  ```
  Cerro Aconcagua
  -32.65
  -70.01
  ```

---

### A5. Tipos de datos

**Enunciado**: Usando las variables del ejercicio anterior (nombre, latitud, longitud), mostrá el tipo de cada una usando la función `type()`.

**Ejemplo**:
- Salida esperada:
  ```
  <class 'str'>
  <class 'float'>
  <class 'float'>
  ```

**Hint**: Podés usar `print(type(variable))` para mostrar el tipo.

---

### Bloque 2: Operadores aritméticos y funciones numéricas

---

### A6. Promedio de altitudes redondeado

**Enunciado**: Tres ciudades tienen las siguientes altitudes: La Quiaca (3442 m), Jujuy (1259 m) y Salta (1187 m). Calculá el promedio y redondealo a 2 decimales usando `round()`.

**Ejemplo**:
- Salida esperada: `1962.67`

---

### A7. Distancia entre coordenadas

**Enunciado**: Calculá la diferencia absoluta entre las longitudes de Santiago (-70.6) y Buenos Aires (-58.4) usando `abs()`. Luego calculá cuántos husos horarios aproximados separan ambas ciudades (dividí la diferencia por 15 y redondeá a entero).

**Ejemplo**:
- Salida esperada:
  ```
  Diferencia: 12.2 grados
  Husos horarios: 1
  ```

---

### A8. Área y diagonal de un terreno

**Enunciado**: Un terreno rectangular mide 120 m × 80 m. Calculá:
1. El área (base × altura)
2. La diagonal usando el teorema de Pitágoras: `diagonal = (base**2 + altura**2) ** 0.5`
Redondeá la diagonal a 2 decimales.

**Ejemplo**:
- Salida esperada:
  ```
  Área: 9600 m²
  Diagonal: 144.22 m
  ```

---

### A9. División entera y resto

**Enunciado**: La distancia entre Buenos Aires y Ushuaia es de 3079 km. Si un auto recorre 450 km por día:
1. ¿Cuántos días completos de viaje son? (usá `//`)
2. ¿Cuántos km quedan para el último día? (usá `%`)

**Ejemplo**:
- Salida esperada:
  ```
  Días completos: 6
  Km restantes: 379
  ```

---

### A10. Conversión de coordenadas

**Enunciado**: La latitud -34.6037 se puede separar en parte entera y decimal. Usando `int()`, `abs()` y operaciones aritméticas:
1. Extraé la parte entera (sin signo): 34
2. Extraé la parte decimal multiplicada por 60 (minutos aproximados): 36.22

**Ejemplo**:
- Salida esperada:
  ```
  Grados: 34
  Minutos: 36.22
  ```

**Hint**: La parte decimal se obtiene con `abs(valor) - int(abs(valor))`

---

### Bloque 3: Strings y formateo

---

### A11. Concatenación de texto

**Enunciado**: Tenés dos variables: `pais = "Argentina"` y `ciudad = "Ushuaia"`. Creaá una nueva variable que contenga ambos textos separados por una coma y un espacio, y mostrala.

**Ejemplo**:
- Salida esperada: `Argentina, Ushuaia`

**Hint**: Podés unir strings con el operador `+`.

---

### A12. Descripción con f-string

**Enunciado**: Usando las variables `ciudad = "Bariloche"`, `latitud = -41.13` y `longitud = -71.31`, creá un mensaje formateado que diga: "La ciudad de Bariloche está en las coordenadas (-41.13, -71.31)"

**Ejemplo**:
- Salida esperada: `La ciudad de Bariloche está en las coordenadas (-41.13, -71.31)`

**Hint**: Usá f-strings: `f"texto {variable} más texto"`

---

### A13. Longitud de un nombre

**Enunciado**: Guardá el nombre "San Martín de los Andes" en una variable y mostrá cuántos caracteres tiene usando `len()`.

**Ejemplo**:
- Salida esperada: `22`

---

### A14. Mayúsculas y minúsculas

**Enunciado**: Dada la variable `ciudad = "Mar del Plata"`, mostrá el nombre en mayúsculas y luego en minúsculas.

**Ejemplo**:
- Salida esperada:
  ```
  MAR DEL PLATA
  mar del plata
  ```

**Hint**: Usá los métodos `.upper()` y `.lower()`.

---

### A15. Línea divisoria

**Enunciado**: Creá una línea divisoria de 40 guiones (`-`) usando el operador de repetición de strings y mostrala.

**Ejemplo**:
- Salida esperada: `----------------------------------------`

**Hint**: Podés repetir un string con `"texto" * n`.

---

### Bloque 4: Conversión de tipos e input

---

### A16. String a número

**Enunciado**: Tenés la coordenada guardada como texto: `latitud_texto = "-34.6"`. Convertila a un número decimal (float) y mostrá el resultado y su tipo.

**Ejemplo**:
- Salida esperada:
  ```
  -34.6
  <class 'float'>
  ```

**Hint**: Usá `float()` para convertir.

---

### A17. Decimal a entero

**Enunciado**: La altitud exacta del Cerro Fitz Roy es 3405.2 metros. Convertí este valor a un número entero (truncando los decimales) y mostralo.

**Ejemplo**:
- Salida esperada: `3405`

**Hint**: Usá `int()` para convertir a entero.

---

### A18. Pedir nombre de ciudad

**Enunciado**: Pedí al usuario que ingrese el nombre de su ciudad favorita y luego mostrá un mensaje que diga "Tu ciudad favorita es: [ciudad]".

**Ejemplo**:
- Salida esperada: `Tu ciudad favorita es: Córdoba`

**Hint**: Usá `input("mensaje")` para pedir datos al usuario.

---

### A19. Pedir coordenada

**Enunciado**: Pedí al usuario que ingrese una latitud. Convertí el valor a número decimal y mostrá el doble de esa latitud.

**Ejemplo**:
- Salida esperada: `-51.0`

**Hint**: `input()` siempre devuelve texto, necesitás convertirlo con `float()`.

---

### A20. Ficha de ubicación simple

**Enunciado**: Pedí al usuario que ingrese:
1. Nombre de un lugar
2. Latitud
3. Longitud
Luego mostrá un resumen formateado con los tres datos.

**Ejemplo**:
- Entrada: ``
- Salida esperada:
  ```
  === Ficha de ubicación ===
  Lugar: Glaciar Perito Moreno
  Latitud: -50.5
  Longitud: -73.0
  ```

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Punto medio

**Enunciado**: Dados dos puntos geográficos:
- Punto A: latitud -34.6, longitud -58.4 (Buenos Aires)
- Punto B: latitud -31.4, longitud -64.2 (Córdoba)
Calculá las coordenadas del punto medio entre ambos (promediando latitudes y longitudes por separado).

**Ejemplo**:
- Salida esperada:
  ```
  Punto medio:
  Latitud: -33.0
  Longitud: -61.3
  ```

---

### B2. Grados a grados y minutos

**Enunciado**: La latitud -34.65 grados se puede expresar como grados y minutos decimales. Los grados son la parte entera (-34) y los minutos se calculan multiplicando la parte decimal (0.65) por 60. Convertí la latitud -34.65 y mostrá el resultado.

**Ejemplo**:
- Salida esperada: `-34 grados, 39.0 minutos`

**Hint**: Usá `int()` para obtener la parte entera y el operador `%` o resta para la parte decimal.

---

### B3. Diferencia de husos horarios

**Enunciado**: El huso horario aproximado se puede calcular dividiendo la longitud por 15. Dadas las longitudes de Tokyo (139.7) y Buenos Aires (-58.4), calculá la diferencia aproximada de horas entre ambas ciudades.

**Hint**: Calculá el huso de cada ciudad y luego restá.

---

### B4. Iniciales de un lugar

**Enunciado**: Dado el nombre "Parque Nacional Los Glaciares", extraé y mostrá solo la primera letra de cada palabra (las iniciales).

**Ejemplo**:
- Salida esperada: `P N L G`

**Hint**: Podés acceder a caracteres individuales con índices: `texto[0]`, `texto[1]`, etc. Buscá las posiciones después de cada espacio.

---

### B5. Celsius a Fahrenheit

**Enunciado**: La temperatura en la Base Marambio (Antártida) es de -5°C. Convertila a Fahrenheit usando la fórmula: F = C × 9/5 + 32

**Ejemplo**:
- Salida esperada: `23.0`

---

### B6. Mismo hemisferio

**Enunciado**: Dados dos puntos con sus latitudes:
- `lat_a = -34.6` (Buenos Aires)
- `lat_b = -33.4` (Santiago)
Verificá si ambos están en el mismo hemisferio (ambos positivos o ambos negativos) y mostrá True o False.

**Ejemplo**:
- Salida esperada: `True`

**Hint**: Dos números están en el mismo "lado" si su producto es positivo.

---

### B7. Perímetro de un triángulo

**Enunciado**: Un terreno triangular tiene lados de 150m, 200m y 180m. Calculá y mostrá su perímetro.

**Ejemplo**:
- Salida esperada: `530`

---

### B8. Formatear coordenadas con dirección

**Enunciado**: Dada una latitud de -34.6 y una longitud de -58.4, mostrá las coordenadas con el formato tradicional incluyendo dirección cardinal:
- Latitud negativa = Sur (S), positiva = Norte (N)
- Longitud negativa = Oeste (W), positiva = Este (E)

**Ejemplo**:
- Salida esperada: `34.6°S, 58.4°W`

**Hint**: Usá `abs()` para obtener el valor absoluto y condicionales simples o expresiones para la dirección.

---

### B9. Validar coordenadas completas

**Enunciado**: Pedí al usuario una latitud y una longitud. Verificá que ambas sean válidas:
- Latitud: entre -90 y 90
- Longitud: entre -180 y 180
Mostrá True si ambas son válidas, False en caso contrario.

**Ejemplo**:
- Entrada: `45.5` y `-200`
- Salida esperada: `False` (la longitud está fuera de rango)`

---

### B10. Sello de ubicación

**Enunciado**: Creá un "sello de ubicación" que incluya:
- Una línea de 30 asteriscos
- El nombre del lugar (pedido al usuario)
- Las coordenadas (pedidas al usuario)
- La fecha de hoy (como texto, ingresada por el usuario)
- Otra línea de 30 asteriscos

**Ejemplo**:
- Entrada: `Cataratas del Iguazú`, `-25.7`, `-54.4`, `2026-02-02`
- Salida esperada:
  ```
  ******************************
  Lugar: Cataratas del Iguazú
  Coordenadas: -25.7, -54.4
  Fecha: 2026-02-02
  ******************************
  ```

---

### B11. Link a Google Maps

**Enunciado**: Pedí al usuario que ingrese una latitud y una longitud. Generá e imprimí un link de Google Maps que apunte a esas coordenadas.
El formato del link es: `https://www.google.com/maps?q=LATITUD,LONGITUD`

**Ejemplo**:
- Entrada: `-34.6037`, `-58.3816`
- Salida esperada: `https://www.google.com/maps?q=-34.6037,-58.3816`

**Hint**: Usá f-strings para construir la URL con las variables.

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Distancia euclidiana simplificada

**Enunciado**: Calculá una aproximación de la distancia entre dos puntos usando la fórmula euclidiana simplificada (sin considerar la curvatura terrestre):
distancia = √[(lat2-lat1)² + (lon2-lon1)²]
Puntos:
- Buenos Aires: (-34.6, -58.4)
- Montevideo: (-34.9, -56.2)

**Hint**: Podés calcular la raíz cuadrada elevando a la potencia 0.5: `valor ** 0.5`

---

### C2. Grados/Minutos/Segundos a decimal

**Enunciado**: Las coordenadas a veces se expresan en grados, minutos y segundos (DMS). Por ejemplo: 34° 36' 12" S
La conversión a decimal es: grados + minutos/60 + segundos/3600
Convertí la coordenada 34° 36' 12" Sur a formato decimal (recordá que Sur es negativo).

**Ejemplo**:
- Entrada: `grados=34, minutos=36, segundos=12, dirección="S"`
- Salida esperada: `-34.6033...`

---

### C3. Cuadrante del planeta

**Enunciado**: Determiná en qué cuadrante del planeta está un punto según sus coordenadas:
- NE (Noreste): latitud > 0 y longitud > 0
- NW (Noroeste): latitud > 0 y longitud < 0
- SE (Sureste): latitud < 0 y longitud > 0
- SW (Suroeste): latitud < 0 y longitud < 0
Si la latitud o longitud es exactamente 0, indicá que está en un eje.
Probá con las coordenadas de Sydney: latitud -33.9, longitud 151.2

**Ejemplo**:
- Salida esperada: `SE` (Sureste)`

**Hint**: Usá múltiples comparaciones con `and` y `or`, o investigá sobre expresiones condicionales.

---

### C4. Tiempo de viaje

**Enunciado**: Calculá el tiempo de viaje entre dos ciudades dada la distancia y la velocidad promedio. Mostrá el resultado en formato horas:minutos.
- Distancia: 400 km
- Velocidad: 80 km/h

**Ejemplo**:
- Salida esperada: `4:22` (aproximadamente)`

**Hint**: Las horas son la división entera, los minutos son el resto convertido.

---

### C5. Ficha de ubicación completa

**Enunciado**: Creá una mini-aplicación que:
1. Pida al usuario: nombre del lugar, latitud y longitud
2. Valide que las coordenadas estén en rangos correctos
3. Determine el hemisferio (Norte/Sur) y el meridiano (Este/Oeste)
4. Calcule a qué huso horario aproximado pertenece
5. Muestre un reporte completo y bien formateado

**Ejemplo**:
- Entrada: `Machu Picchu`, `-13.16`, `-72.55`
- Salida esperada:
  ```
  ============================================
  FICHA DE UBICACIÓN
  ============================================
  Lugar: Machu Picchu
  Coordenadas:
  Latitud:  13.16° Sur
  Longitud: 72.55° Oeste
  Ubicación: Hemisferio Sur, Meridiano Oeste
  Huso horario aproximado: UTC-5
  Estado: Coordenadas válidas
  ============================================
  ```

**Hint**: Combiná todo lo aprendido: variables, operadores, strings, conversiones, comparaciones y formateo.

---

*Fin de los ejercicios de la Unidad 1*
