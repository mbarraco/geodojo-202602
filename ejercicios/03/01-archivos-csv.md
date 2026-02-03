# Unidad 3: Archivos y CSV

Ejercicios sobre lectura y escritura de archivos, y manejo del módulo CSV.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Lectura de archivos con open()

---

### A1. Leer archivo completo

**Enunciado**: Creá un archivo `ciudad.txt` con el texto "Buenos Aires" y luego escribí un programa que lo lea completo usando `open()` y `read()`. Mostrá el contenido por pantalla.

**Ejemplo**:
- Contenido del archivo: `Buenos Aires`
- Salida esperada: `Buenos Aires`

**Hint**: Usá `open("archivo.txt", "r")` para abrir en modo lectura y `.read()` para leer todo el contenido.

---

### A2. Leer línea por línea

**Enunciado**: Creá un archivo `ciudades.txt` con tres ciudades (una por línea): Buenos Aires, Córdoba, Rosario. Leé el archivo y mostrá cada línea numerada.

**Ejemplo**:
- Salida esperada:
  ```
  1: Buenos Aires
  2: Córdoba
  3: Rosario
  ```

**Hint**: Usá `readlines()` para obtener una lista de líneas, y `enumerate()` para numerarlas.

---

### A3. Leer con context manager

**Enunciado**: Reescribí el ejercicio anterior usando `with open(...) as f:` en lugar de abrir y cerrar manualmente.

**Ejemplo**:
- Salida esperada: igual que A2

**Hint**: El context manager `with` cierra automáticamente el archivo al salir del bloque.

---

### A4. Contar líneas de un archivo

**Enunciado**: Creá un archivo `provincias.txt` con 5 provincias argentinas (una por línea). Escribí un programa que cuente cuántas líneas tiene el archivo.

**Ejemplo**:
- Salida esperada: `El archivo tiene 5 líneas`

**Hint**: Usá `len(archivo.readlines())` para contar las líneas.

---

### A5. Leer coordenadas desde archivo

**Enunciado**: Creá un archivo `coordenadas.txt` con el contenido `-34.6,-58.4` (latitud y longitud de Buenos Aires). Leé el archivo, separá los valores por la coma, convertí a float y mostrá cada coordenada.

**Ejemplo**:
- Salida esperada:
  ```
  Latitud: -34.6
  Longitud: -58.4
  ```

**Hint**: Usá `.split(",")` para separar por coma y `float()` para convertir.

---

### Bloque 2: Escritura de archivos

---

### A6. Escribir texto simple

**Enunciado**: Escribí un programa que cree un archivo `destino.txt` y escriba el texto "Ushuaia" en él.

**Ejemplo**:
- Contenido del archivo creado: `Ushuaia`

**Hint**: Usá `open("archivo.txt", "w")` para abrir en modo escritura y `.write()` para escribir.

---

### A7. Escribir múltiples líneas

**Enunciado**: Creá una lista con tres ciudades: `["Mendoza", "Salta", "Tucumán"]`. Escribí cada ciudad en una línea separada en un archivo `mis_ciudades.txt`.

**Ejemplo**:
- Contenido del archivo:
  ```
  Mendoza
  Salta
  Tucumán
  ```

**Hint**: Agregá `\n` al final de cada línea, o usá `writelines()` con una lista que ya incluya los saltos de línea.

---

### A8. Agregar al final de un archivo

**Enunciado**: Teniendo el archivo `mis_ciudades.txt` del ejercicio anterior, agregá una nueva ciudad "Neuquén" al final sin borrar las existentes.

**Ejemplo**:
- Contenido final del archivo:
  ```
  Mendoza
  Salta
  Tucumán
  Neuquén
  ```

**Hint**: Usá modo `"a"` (append) en lugar de `"w"` para agregar sin sobrescribir.

---

### A9. Guardar coordenadas

**Enunciado**: Dadas las variables `lat = -32.89` y `lon = -68.83` (Mendoza), escribí un archivo `punto.txt` con el formato `latitud,longitud`.

**Ejemplo**:
- Contenido del archivo: `-32.89,-68.83`

**Hint**: Usá f-string para formatear: `f"{lat},{lon}"`.

---

### A10. Copiar contenido de archivo

**Enunciado**: Escribí un programa que lea el contenido de `ciudades.txt` y lo copie a un nuevo archivo `ciudades_backup.txt`.

**Ejemplo**:
- Si `ciudades.txt` contiene "Buenos Aires\nCórdoba", `ciudades_backup.txt` debe contener lo mismo.

**Hint**: Leé con `read()` y escribí con `write()`.

---

### Bloque 3: Módulo CSV - Lectura

---

### A11. Leer CSV simple

**Enunciado**: Creá un archivo `ciudades.csv` con el siguiente contenido:
```
nombre,poblacion
Buenos Aires,2890000
Córdoba,1430000
Rosario,1270000
```
Leé el archivo usando `csv.reader()` y mostrá cada fila.

**Ejemplo**:
- Salida esperada:
  ```
  ['nombre', 'poblacion']
  ['Buenos Aires', '2890000']
  ['Córdoba', '1430000']
  ['Rosario', '1270000']
  ```

**Hint**: Importá el módulo `csv` y usá `csv.reader(archivo)`.

---

### A12. Saltar encabezado

**Enunciado**: Usando el archivo `ciudades.csv` del ejercicio anterior, leé y mostrá solo las filas de datos, saltando el encabezado.

**Ejemplo**:
- Salida esperada:
  ```
  Buenos Aires: 2890000 habitantes
  Córdoba: 1430000 habitantes
  Rosario: 1270000 habitantes
  ```

**Hint**: Usá `next(reader)` para saltar la primera fila, o convertí a lista y usá slicing.

---

### A13. CSV con coordenadas

**Enunciado**: Creá un archivo `puntos.csv`:
```
ciudad,latitud,longitud
Buenos Aires,-34.6,-58.4
Córdoba,-31.4,-64.2
Mendoza,-32.9,-68.8
```
Leé el archivo y mostrá cada ciudad con sus coordenadas formateadas.

**Ejemplo**:
- Salida esperada:
  ```
  Buenos Aires está en (-34.6, -58.4)
  Córdoba está en (-31.4, -64.2)
  Mendoza está en (-32.9, -68.8)
  ```

---

### A14. Calcular con datos de CSV

**Enunciado**: Usando `ciudades.csv`, calculá la población total sumando los valores de la columna población.

**Ejemplo**:
- Salida esperada: `Población total: 5590000`

**Hint**: Convertí los valores de población a `int()` antes de sumar.

---

### A15. Buscar en CSV

**Enunciado**: Usando `puntos.csv`, escribí un programa que busque la ciudad "Mendoza" y muestre sus coordenadas.

**Ejemplo**:
- Salida esperada: `Mendoza: latitud -32.9, longitud -68.8`

**Hint**: Recorré las filas y usá un `if` para comparar el nombre.

---

### Bloque 4: DictReader y DictWriter

---

### A16. Leer CSV como diccionarios

**Enunciado**: Usando `puntos.csv`, leé el archivo con `csv.DictReader()` y mostrá cada fila como diccionario.

**Ejemplo**:
- Salida esperada:
  ```
  {'ciudad': 'Buenos Aires', 'latitud': '-34.6', 'longitud': '-58.4'}
  {'ciudad': 'Córdoba', 'latitud': '-31.4', 'longitud': '-64.2'}
  {'ciudad': 'Mendoza', 'latitud': '-32.9', 'longitud': '-68.8'}
  ```

**Hint**: `csv.DictReader()` usa la primera fila como claves.

---

### A17. Acceder por nombre de columna

**Enunciado**: Usando `DictReader`, leé `puntos.csv` y mostrá solo los nombres de las ciudades accediendo por clave.

**Ejemplo**:
- Salida esperada:
  ```
  Buenos Aires
  Córdoba
  Mendoza
  ```

**Hint**: Accedé con `fila["ciudad"]` en lugar de `fila[0]`.

---

### A18. Escribir CSV con DictWriter

**Enunciado**: Creá una lista de diccionarios con datos de provincias:
```python
provincias = [
    {"nombre": "Buenos Aires", "capital": "La Plata"},
    {"nombre": "Córdoba", "capital": "Córdoba"},
    {"nombre": "Santa Fe", "capital": "Santa Fe"}
]
```
Escribí estos datos en un archivo `provincias.csv` usando `DictWriter`.

**Ejemplo**:
- Contenido del archivo:
  ```
  nombre,capital
  Buenos Aires,La Plata
  Córdoba,Córdoba
  Santa Fe,Santa Fe
  ```

**Hint**: Usá `writeheader()` para escribir los encabezados y `writerows()` para los datos.

---

### A19. Agregar fila a CSV existente

**Enunciado**: Agregá una nueva provincia al archivo `provincias.csv`: Mendoza con capital Mendoza.

**Ejemplo**:
- Nueva línea agregada: `Mendoza,Mendoza`

**Hint**: Abrí en modo `"a"` y usá `writerow()` para una sola fila. No escribas el encabezado de nuevo.

---

### A20. Filtrar y guardar

**Enunciado**: Leé `puntos.csv` y guardá en un nuevo archivo `puntos_sur.csv` solo las ciudades con latitud menor a -32 (más al sur).

**Ejemplo**:
- Contenido de `puntos_sur.csv`:
  ```
  ciudad,latitud,longitud
  Buenos Aires,-34.6,-58.4
  Mendoza,-32.9,-68.8
  ```

---

### Bloque 5: Combinando lectura y escritura

---

### A21. Transformar datos de CSV

**Enunciado**: Leé `puntos.csv` y creá un nuevo archivo `puntos_absolutos.csv` donde las latitudes y longitudes sean valores absolutos (sin signo negativo).

**Ejemplo**:
- Contenido de `puntos_absolutos.csv`:
  ```
  ciudad,latitud,longitud
  Buenos Aires,34.6,58.4
  Córdoba,31.4,64.2
  Mendoza,32.9,68.8
  ```

---

### A22. Agregar columna calculada

**Enunciado**: Leé `ciudades.csv` y creá `ciudades_categoria.csv` agregando una columna "categoria" que sea "grande" si la población > 1500000, o "mediana" en caso contrario.

**Ejemplo**:
- Contenido de `ciudades_categoria.csv`:
  ```
  nombre,poblacion,categoria
  Buenos Aires,2890000,grande
  Córdoba,1430000,mediana
  Rosario,1270000,mediana
  ```

---

### A23. Combinar dos archivos CSV

**Enunciado**: Tenés `ciudades.csv` (nombre, población) y `puntos.csv` (ciudad, latitud, longitud). Creá `ciudades_completas.csv` que combine ambos archivos, incluyendo nombre, población, latitud y longitud.

**Ejemplo**:
- Contenido de `ciudades_completas.csv`:
  ```
  nombre,poblacion,latitud,longitud
  Buenos Aires,2890000,-34.6,-58.4
  Córdoba,1430000,-31.4,-64.2
  ```

**Hint**: Leé ambos archivos a diccionarios y combiná por nombre de ciudad.

---

### A24. Generar reporte desde CSV

**Enunciado**: Leé `puntos.csv` y generá un archivo `reporte.txt` (no CSV) con un resumen legible:
```
=== REPORTE DE CIUDADES ===
Total de ciudades: 3
Ciudad más al norte: Córdoba (-31.4)
Ciudad más al sur: Buenos Aires (-34.6)
```

---

### A25. Exportar a formato Google Maps

**Enunciado**: Leé `puntos.csv` y generá un archivo `links.txt` con un link de Google Maps por cada ciudad.

**Ejemplo**:
- Contenido de `links.txt`:
  ```
  Buenos Aires: https://www.google.com/maps?q=-34.6,-58.4
  Córdoba: https://www.google.com/maps?q=-31.4,-64.2
  Mendoza: https://www.google.com/maps?q=-32.9,-68.8
  ```

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Contar palabras en archivo

**Enunciado**: Creá un archivo `descripcion.txt` con una descripción de una ciudad (varias oraciones). Contá cuántas palabras tiene el archivo.

**Ejemplo**:
- Si el archivo contiene "Buenos Aires es la capital de Argentina."
- Salida esperada: `El archivo tiene 7 palabras`

---

### B2. Validar existencia de archivo

**Enunciado**: Escribí un programa que intente leer un archivo `datos.csv`. Si el archivo no existe, mostrá un mensaje de error amigable en lugar de que el programa falle.

**Ejemplo**:
- Si el archivo no existe: `Error: El archivo datos.csv no fue encontrado`

**Hint**: Usá `try/except FileNotFoundError`.

---

### B3. CSV con delimitador personalizado

**Enunciado**: Creá un archivo `datos.tsv` separado por tabulaciones (no comas) con datos de ciudades. Leélo usando el parámetro `delimiter` de csv.reader.

**Ejemplo**:
- Contenido: `Buenos Aires	-34.6	-58.4`

---

### B4. Estadísticas de coordenadas

**Enunciado**: Leé `puntos.csv` y calculá: latitud promedio, longitud promedio, y el punto más al este (mayor longitud).

**Ejemplo**:
- Salida esperada:
  ```
  Latitud promedio: -32.97
  Longitud promedio: -63.8
  Punto más al este: Buenos Aires
  ```

---

### B5. Ordenar CSV por columna

**Enunciado**: Leé `ciudades.csv` y creá `ciudades_ordenadas.csv` con las ciudades ordenadas de mayor a menor población.

---

### B6. Backup con timestamp

**Enunciado**: Escribí un programa que copie `puntos.csv` a un archivo de backup con la fecha actual en el nombre, por ejemplo `puntos_backup_2026-02-03.csv`.

**Hint**: Usá el módulo `datetime` para obtener la fecha.

---

### B7. Validar formato de CSV

**Enunciado**: Escribí un programa que verifique si un archivo CSV tiene exactamente 3 columnas en cada fila. Si alguna fila tiene más o menos, mostrá un mensaje de error indicando el número de fila.

---

### B8. Convertir CSV a formato vertical

**Enunciado**: Leé `puntos.csv` y generá un archivo `puntos_vertical.txt` con formato:
```
--- Buenos Aires ---
Latitud: -34.6
Longitud: -58.4

--- Córdoba ---
Latitud: -31.4
Longitud: -64.2
```

---

### B9. Unir múltiples archivos CSV

**Enunciado**: Tenés `ciudades_norte.csv` y `ciudades_sur.csv` con el mismo formato. Creá un programa que los una en `todas_ciudades.csv`.

---

### B10. Leer CSV desde string

**Enunciado**: Dado un string multilínea que representa un CSV:
```python
datos = """ciudad,lat,lon
Buenos Aires,-34.6,-58.4
Córdoba,-31.4,-64.2"""
```
Parseá el string como si fuera un archivo CSV usando `io.StringIO`.

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Detector de encoding

**Enunciado**: Algunos archivos CSV pueden tener diferentes encodings (UTF-8, Latin-1, etc.). Escribí un programa que intente abrir un archivo con UTF-8 primero, y si falla, pruebe con Latin-1.

---

### C2. CSV con campos multilínea

**Enunciado**: Los campos CSV pueden contener saltos de línea si están entre comillas. Creá un archivo donde una celda contenga texto con saltos de línea y leélo correctamente.

**Ejemplo**:
```csv
ciudad,descripcion
"Buenos Aires","Capital de Argentina.
Ciudad más poblada."
```

---

### C3. Comparar dos versiones de CSV

**Enunciado**: Tenés `ciudades_v1.csv` y `ciudades_v2.csv`. Escribí un programa que muestre qué ciudades fueron agregadas, eliminadas o modificadas entre ambas versiones.

---

### C4. Generar CSV desde API simulada

**Enunciado**: Creá una función `obtener_ciudades()` que simule una respuesta de API retornando una lista de diccionarios. Luego guardá esos datos en un archivo CSV.

```python
def obtener_ciudades():
    return [
        {"nombre": "Buenos Aires", "pais": "Argentina"},
        {"nombre": "Santiago", "pais": "Chile"}
    ]
```

---

### C5. Sistema de log en archivo

**Enunciado**: Creá un sistema simple de logging que agregue mensajes con timestamp a un archivo `log.txt`. Cada vez que se ejecute el programa, debe agregar una nueva línea sin borrar las anteriores.

**Ejemplo** de contenido después de varias ejecuciones:
```
2026-02-03 10:30:15 - Programa iniciado
2026-02-03 10:30:16 - Datos procesados
2026-02-03 10:45:22 - Programa iniciado
```

---

*Fin de los ejercicios de la Unidad 3 - Archivos y CSV*
