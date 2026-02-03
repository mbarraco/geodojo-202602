# Clase 3: Archivos y CSV

Guía para la clase sobre lectura y escritura de archivos, y manejo del módulo CSV.

---

## 1. Temario

### 1.1 Lectura de archivos con open()

| Función/Método | Descripción | Ejemplo |
|----------------|-------------|---------|
| `open(path, "r")` | Abre archivo en modo lectura | `f = open("datos.txt", "r")` |
| `.read()` | Lee todo el contenido como string | `contenido = f.read()` |
| `.readline()` | Lee una línea | `linea = f.readline()` |
| `.readlines()` | Lee todas las líneas como lista | `lineas = f.readlines()` |
| `.close()` | Cierra el archivo | `f.close()` |
| `with open(...) as f:` | Context manager (cierre automático) | Ver ejemplos |

### 1.2 Escritura de archivos

| Modo | Descripción | Uso |
|------|-------------|-----|
| `"w"` | Escritura (sobrescribe) | `open("nuevo.txt", "w")` |
| `"a"` | Append (agrega al final) | `open("log.txt", "a")` |
| `"r+"` | Lectura y escritura | `open("datos.txt", "r+")` |

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `.write(str)` | Escribe un string | `f.write("Hola")` |
| `.writelines(list)` | Escribe lista de strings | `f.writelines(["a\n", "b\n"])` |

### 1.3 Módulo CSV - Lectura

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `csv.reader(f)` | Lee CSV como listas | `reader = csv.reader(archivo)` |
| `next(reader)` | Obtiene siguiente fila (salta encabezado) | `encabezado = next(reader)` |
| `list(reader)` | Convierte a lista de filas | `datos = list(reader)` |

### 1.4 DictReader y DictWriter

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `csv.DictReader(f)` | Lee CSV como diccionarios | `reader = csv.DictReader(archivo)` |
| `csv.DictWriter(f, fieldnames)` | Escribe diccionarios a CSV | `writer = csv.DictWriter(f, ["col1", "col2"])` |
| `.writeheader()` | Escribe fila de encabezados | `writer.writeheader()` |
| `.writerow(dict)` | Escribe un diccionario | `writer.writerow({"col1": "val1"})` |
| `.writerows(list)` | Escribe lista de diccionarios | `writer.writerows(datos)` |

### 1.5 Patrones comunes

| Patrón | Código |
|--------|--------|
| Leer archivo completo | `with open("f.txt") as f: texto = f.read()` |
| Leer líneas | `with open("f.txt") as f: lineas = f.readlines()` |
| Escribir texto | `with open("f.txt", "w") as f: f.write("texto")` |
| Leer CSV a lista | `with open("f.csv") as f: datos = list(csv.reader(f))` |
| Leer CSV a dicts | `with open("f.csv") as f: datos = list(csv.DictReader(f))` |

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Leer archivo de texto
Crear un archivo `ciudad.txt` con el nombre de una ciudad y leerlo con Python.

---

#### Ejemplo 2: Context manager
Reescribir el ejemplo anterior usando `with open(...) as f:`.

---

#### Ejemplo 3: Leer múltiples líneas
Crear un archivo con 3 ciudades (una por línea) y mostrarlas numeradas.

---

#### Ejemplo 4: Escribir archivo
Crear un archivo `destinos.txt` escribiendo una lista de ciudades.

---

#### Ejemplo 5: Modo append
Agregar una nueva ciudad al archivo sin borrar las existentes.

---

#### Ejemplo 6: Leer CSV con csv.reader
Crear un CSV de ciudades con población y leerlo mostrando cada fila.

---

#### Ejemplo 7: Procesar datos del CSV
Leer el CSV de ciudades y calcular la población total.

---

#### Ejemplo 8: Usar DictReader
Leer el mismo CSV pero accediendo a los datos por nombre de columna.

---

#### Ejemplo 9: Escribir CSV con DictWriter
Crear una lista de diccionarios con datos de puntos geográficos y guardarla como CSV.

---

#### Ejemplo 10: Transformar CSV
Leer un CSV de coordenadas, agregar una columna calculada, y guardar en un nuevo archivo.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Leer archivo de texto

**Enunciado**: Crear un archivo `ciudad.txt` con el nombre de una ciudad y leerlo con Python.

```python
# Primero creamos el archivo manualmente o con Python:
with open("ciudad.txt", "w") as f:
    f.write("Buenos Aires")

# Luego lo leemos:
archivo = open("ciudad.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
```

**Salida**:
```
Buenos Aires
```

---

#### Ejemplo 2: Context manager

**Enunciado**: Reescribir el ejemplo anterior usando `with open(...) as f:`.

```python
with open("ciudad.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# El archivo se cierra automáticamente al salir del bloque with
```

**Salida**:
```
Buenos Aires
```

---

#### Ejemplo 3: Leer múltiples líneas

**Enunciado**: Crear un archivo con 3 ciudades (una por línea) y mostrarlas numeradas.

```python
# Crear archivo
with open("ciudades.txt", "w") as f:
    f.write("Buenos Aires\n")
    f.write("Córdoba\n")
    f.write("Rosario\n")

# Leer y mostrar numerado
with open("ciudades.txt", "r") as f:
    lineas = f.readlines()
    for i, linea in enumerate(lineas, 1):
        print(f"{i}: {linea.strip()}")
```

**Salida**:
```
1: Buenos Aires
2: Córdoba
3: Rosario
```

---

#### Ejemplo 4: Escribir archivo

**Enunciado**: Crear un archivo `destinos.txt` escribiendo una lista de ciudades.

```python
ciudades = ["Ushuaia", "Bariloche", "Mendoza"]

with open("destinos.txt", "w") as f:
    for ciudad in ciudades:
        f.write(ciudad + "\n")

print("Archivo creado!")
```

**Salida**:
```
Archivo creado!
```

---

#### Ejemplo 5: Modo append

**Enunciado**: Agregar una nueva ciudad al archivo sin borrar las existentes.

```python
# Agregar al final (no sobrescribe)
with open("destinos.txt", "a") as f:
    f.write("Salta\n")

# Verificar contenido
with open("destinos.txt", "r") as f:
    print(f.read())
```

**Salida**:
```
Ushuaia
Bariloche
Mendoza
Salta
```

---

#### Ejemplo 6: Leer CSV con csv.reader

**Enunciado**: Crear un CSV de ciudades con población y leerlo mostrando cada fila.

```python
import csv

# Crear CSV
with open("ciudades.csv", "w") as f:
    f.write("nombre,poblacion\n")
    f.write("Buenos Aires,2890000\n")
    f.write("Córdoba,1430000\n")
    f.write("Rosario,1270000\n")

# Leer CSV
with open("ciudades.csv", "r") as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)
```

**Salida**:
```
['nombre', 'poblacion']
['Buenos Aires', '2890000']
['Córdoba', '1430000']
['Rosario', '1270000']
```

---

#### Ejemplo 7: Procesar datos del CSV

**Enunciado**: Leer el CSV de ciudades y calcular la población total.

```python
import csv

with open("ciudades.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Saltar encabezado
    
    total = 0
    for fila in reader:
        nombre = fila[0]
        poblacion = int(fila[1])
        total += poblacion
        print(f"{nombre}: {poblacion:,} habitantes")
    
    print(f"\nTotal: {total:,} habitantes")
```

**Salida**:
```
Buenos Aires: 2,890,000 habitantes
Córdoba: 1,430,000 habitantes
Rosario: 1,270,000 habitantes

Total: 5,590,000 habitantes
```

---

#### Ejemplo 8: Usar DictReader

**Enunciado**: Leer el mismo CSV pero accediendo a los datos por nombre de columna.

```python
import csv

with open("ciudades.csv", "r") as f:
    reader = csv.DictReader(f)
    
    for fila in reader:
        nombre = fila["nombre"]
        poblacion = fila["poblacion"]
        print(f"{nombre} tiene {poblacion} habitantes")
```

**Salida**:
```
Buenos Aires tiene 2890000 habitantes
Córdoba tiene 1430000 habitantes
Rosario tiene 1270000 habitantes
```

---

#### Ejemplo 9: Escribir CSV con DictWriter

**Enunciado**: Crear una lista de diccionarios con datos de puntos geográficos y guardarla como CSV.

```python
import csv

puntos = [
    {"ciudad": "Buenos Aires", "lat": -34.6, "lon": -58.4},
    {"ciudad": "Córdoba", "lat": -31.4, "lon": -64.2},
    {"ciudad": "Mendoza", "lat": -32.9, "lon": -68.8}
]

with open("puntos.csv", "w", newline="") as f:
    campos = ["ciudad", "lat", "lon"]
    writer = csv.DictWriter(f, fieldnames=campos)
    
    writer.writeheader()
    writer.writerows(puntos)

print("CSV creado!")
```

**Salida**:
```
CSV creado!
```

---

#### Ejemplo 10: Transformar CSV

**Enunciado**: Leer un CSV de coordenadas, agregar una columna calculada, y guardar en un nuevo archivo.

```python
import csv

# Leer datos originales
with open("puntos.csv", "r") as f:
    reader = csv.DictReader(f)
    puntos = list(reader)

# Agregar columna: hemisferio
for punto in puntos:
    lat = float(punto["lat"])
    punto["hemisferio"] = "Sur" if lat < 0 else "Norte"

# Guardar con nueva columna
with open("puntos_hemisferio.csv", "w", newline="") as f:
    campos = ["ciudad", "lat", "lon", "hemisferio"]
    writer = csv.DictWriter(f, fieldnames=campos)
    
    writer.writeheader()
    writer.writerows(puntos)

# Mostrar resultado
with open("puntos_hemisferio.csv", "r") as f:
    print(f.read())
```

**Salida**:
```
ciudad,lat,lon,hemisferio
Buenos Aires,-34.6,-58.4,Sur
Córdoba,-31.4,-64.2,Sur
Mendoza,-32.9,-68.8,Sur
```

---

## Notas para el docente

- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Cada ejemplo introduce 1-2 conceptos nuevos de forma incremental
- Se recomienda crear los archivos en vivo para que los alumnos vean el proceso completo
- Enfatizar el uso de `with` como buena práctica (cierre automático de archivos)
- Los ejercicios en `ejercicios/03/01-archivos-csv.md` refuerzan estos conceptos
- Contexto geográfico: ciudades argentinas, coordenadas, población
- Tener cuidado con el parámetro `newline=""` en Windows al escribir CSV
