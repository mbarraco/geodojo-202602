# Unidad 3: Pandas para Datos Geográficos

Ejercicios sobre lectura y manipulación de datos con Pandas.

---

## Categoría A - Ejercicios fundamentales

Se recomienda hacerlos todos. Están ordenados por dificultad incremental.

---

### Bloque 1: Cargar datos y exploración básica

---

### A1. Leer CSV con pandas

**Enunciado**: Creá un archivo `ciudades.csv` con columnas nombre, latitud, longitud y población. Leélo con `pd.read_csv()` y mostrá el DataFrame.

**Ejemplo**:
- Contenido del CSV:
  ```
  nombre,latitud,longitud,poblacion
  Buenos Aires,-34.6,-58.4,2890000
  Córdoba,-31.4,-64.2,1430000
  Rosario,-33.0,-60.7,1270000
  ```
- Salida esperada: DataFrame con 3 filas y 4 columnas

**Hint**: `import pandas as pd` y luego `pd.read_csv("archivo.csv")`.

---

### A2. Ver primeras y últimas filas

**Enunciado**: Usando el DataFrame del ejercicio anterior, mostrá las primeras 2 filas con `head()` y las últimas 2 con `tail()`.

**Ejemplo**:
- `df.head(2)` muestra las primeras 2 filas
- `df.tail(2)` muestra las últimas 2 filas

---

### A3. Información del DataFrame

**Enunciado**: Usá `df.shape`, `df.columns` y `df.dtypes` para explorar la estructura del DataFrame.

**Ejemplo**:
- Salida esperada:
  ```
  Forma: (3, 4)
  Columnas: ['nombre', 'latitud', 'longitud', 'poblacion']
  Tipos: nombre: object, latitud: float64, ...
  ```

---

### A4. Estadísticas básicas

**Enunciado**: Usá `df.describe()` para ver estadísticas de las columnas numéricas (latitud, longitud, población).

**Ejemplo**:
- Salida esperada: tabla con count, mean, std, min, max, etc.

---

### A5. Acceder a una columna

**Enunciado**: Extraé la columna "nombre" del DataFrame y mostrá sus valores.

**Ejemplo**:
- Salida esperada:
  ```
  0    Buenos Aires
  1         Córdoba
  2         Rosario
  Name: nombre, dtype: object
  ```

**Hint**: Usá `df["nombre"]` o `df.nombre`.

---

### Bloque 2: Selección con loc e iloc

---

### A6. Seleccionar fila por índice

**Enunciado**: Usá `iloc[0]` para obtener la primera fila del DataFrame como Serie.

**Ejemplo**:
- Salida esperada:
  ```
  nombre        Buenos Aires
  latitud             -34.6
  longitud            -58.4
  poblacion         2890000
  Name: 0, dtype: object
  ```

---

### A7. Seleccionar rango de filas

**Enunciado**: Usá `iloc[0:2]` para obtener las primeras 2 filas como DataFrame.

**Ejemplo**:
- Salida esperada: DataFrame con Buenos Aires y Córdoba

---

### A8. Seleccionar columnas específicas

**Enunciado**: Creá un nuevo DataFrame con solo las columnas "nombre" y "poblacion".

**Ejemplo**:
- Salida esperada: DataFrame con 2 columnas

**Hint**: `df[["nombre", "poblacion"]]` (doble corchete).

---

### A9. Seleccionar con loc por etiqueta

**Enunciado**: Establecé la columna "nombre" como índice con `set_index()`. Luego usá `loc["Córdoba"]` para obtener los datos de Córdoba.

**Ejemplo**:
- Salida esperada: Serie con latitud, longitud y población de Córdoba

---

### A10. Seleccionar celda específica

**Enunciado**: Obtené la población de la primera ciudad usando `iloc[0, 3]` o `loc` con el nombre de columna.

**Ejemplo**:
- Salida esperada: `2890000`

---

### Bloque 3: Filtrado de datos

---

### A11. Filtrar por condición simple

**Enunciado**: Filtrá el DataFrame para mostrar solo las ciudades con población mayor a 1.5 millones.

**Ejemplo**:
- Salida esperada: DataFrame con solo Buenos Aires

**Hint**: `df[df["poblacion"] > 1500000]`.

---

### A12. Filtrar por condición de texto

**Enunciado**: Filtrá para mostrar solo las ciudades cuyo nombre empieza con "B".

**Ejemplo**:
- Salida esperada: DataFrame con Buenos Aires

**Hint**: Usá `df["nombre"].str.startswith("B")`.

---

### A13. Filtrar con múltiples condiciones

**Enunciado**: Filtrá ciudades con latitud menor a -32 Y población mayor a 1 millón.

**Ejemplo**:
- Salida esperada: DataFrame con Buenos Aires y Rosario

**Hint**: Usá `&` para AND y `|` para OR. Cada condición entre paréntesis.

---

### A14. Filtrar con query()

**Enunciado**: Usá el método `query()` para filtrar ciudades con longitud menor a -60.

**Ejemplo**:
- `df.query("longitud < -60")` → ciudades al oeste de -60°

---

### A15. Filtrar con isin()

**Enunciado**: Filtrá para mostrar solo las ciudades que están en la lista `["Buenos Aires", "Rosario"]`.

**Ejemplo**:
- Salida esperada: DataFrame con 2 ciudades

**Hint**: `df[df["nombre"].isin(["Buenos Aires", "Rosario"])]`.

---

### Bloque 4: Agrupación y agregación

---

### A16. Agregar columna de categoría

**Enunciado**: Agregá una columna "region" al DataFrame con valores "Pampeana" para todas las ciudades (por ahora el mismo valor).

**Ejemplo**:
- El DataFrame debe tener una nueva columna "region"

**Hint**: `df["region"] = "Pampeana"`.

---

### A17. Agrupar y contar

**Enunciado**: Creá un DataFrame con varias ciudades y regiones (Pampeana, Cuyo, Norte). Usá `groupby("region").size()` para contar ciudades por región.

**Ejemplo**:
- Salida esperada:
  ```
  region
  Cuyo       2
  Norte      1
  Pampeana   3
  dtype: int64
  ```

---

### A18. Agrupar y sumar

**Enunciado**: Agrupá por región y calculá la población total de cada región con `sum()`.

**Ejemplo**:
- Salida esperada: Serie con población total por región

---

### A19. Múltiples agregaciones

**Enunciado**: Agrupá por región y calculá tanto la suma como el promedio de población usando `agg()`.

**Ejemplo**:
- Salida esperada: DataFrame con columnas sum y mean por región

**Hint**: `df.groupby("region")["poblacion"].agg(["sum", "mean"])`.

---

### A20. Estadísticas por grupo

**Enunciado**: Para cada región, encontrá la ciudad con mayor población usando `idxmax()` o filtrado.

**Ejemplo**:
- Salida esperada: nombre de la ciudad más poblada de cada región

---

### Bloque 5: Guardar y combinar DataFrames

---

### A21. Guardar a CSV

**Enunciado**: Guardá el DataFrame en un nuevo archivo `ciudades_procesado.csv` sin incluir el índice.

**Ejemplo**:
- El archivo se crea correctamente

**Hint**: `df.to_csv("archivo.csv", index=False)`.

---

### A22. Ordenar DataFrame

**Enunciado**: Ordená el DataFrame por población de mayor a menor y guardalo.

**Ejemplo**:
- La primera fila debe ser la ciudad más poblada

**Hint**: `df.sort_values("poblacion", ascending=False)`.

---

### A23. Combinar con concat

**Enunciado**: Creá dos DataFrames pequeños (ciudades del norte y del sur) y combinalos en uno solo con `pd.concat()`.

**Ejemplo**:
- Salida esperada: DataFrame con todas las ciudades de ambos DataFrames

---

### A24. Combinar con merge

**Enunciado**: Tenés un DataFrame con ciudades y población, y otro con ciudades y área. Combinalos por nombre de ciudad usando `merge()`.

**Ejemplo**:
- Salida esperada: DataFrame con nombre, población y área

**Hint**: `pd.merge(df1, df2, on="nombre")`.

---

### A25. Crear columna calculada

**Enunciado**: Agregá una columna "densidad" calculada como población / área (asumiendo que tenés la columna área).

**Ejemplo**:
- Si Buenos Aires tiene 2890000 habitantes y 203 km², la densidad es ~14236

**Hint**: `df["densidad"] = df["poblacion"] / df["area"]`.

---

## Categoría B - Ejercicios de práctica extra

Recomendables para quienes quieran practicar más.

---

### B1. Leer CSV con opciones

**Enunciado**: Leé un CSV especificando el separador (`;`), encoding (`latin-1`) y columnas a usar.

**Hint**: Parámetros `sep`, `encoding`, `usecols` de `read_csv()`.

---

### B2. Manejar valores nulos

**Enunciado**: Creá un DataFrame con algunos valores nulos. Usá `fillna()` para reemplazarlos y `dropna()` para eliminar filas con nulos.

---

### B3. Renombrar columnas

**Enunciado**: Renombrá las columnas del DataFrame de inglés a español usando `rename()`.

---

### B4. Aplicar función a columna

**Enunciado**: Usá `apply()` para crear una columna "hemisferio" que sea "Sur" si latitud < 0, "Norte" si no.

---

### B5. Pivotear datos

**Enunciado**: Creá una tabla pivote que muestre la población promedio por región y año.

---

### B6. Fechas en pandas

**Enunciado**: Leé un CSV con una columna de fecha. Convertila a datetime y extraé el año y mes.

---

### B7. Exportar a Excel

**Enunciado**: Guardá el DataFrame en formato Excel usando `to_excel()`.

**Hint**: Necesitás instalar `openpyxl`.

---

### B8. Leer múltiples CSVs

**Enunciado**: Leé todos los archivos CSV de un directorio y combinalos en un solo DataFrame.

---

### B9. Valores únicos y conteos

**Enunciado**: Usá `unique()` y `value_counts()` para analizar los valores de la columna región.

---

### B10. Crear DataFrame desde diccionario

**Enunciado**: Creá un DataFrame a partir de un diccionario de listas o una lista de diccionarios.

---

## Categoría C - Desafíos

Ejercicios opcionales que requieren mayor dificultad o investigación.

---

### C1. Leer datos de URL

**Enunciado**: Usá `pd.read_csv()` para leer un CSV directamente desde una URL de internet.

---

### C2. Análisis de correlación

**Enunciado**: Calculá la matriz de correlación entre latitud, longitud y población. Interpretá los resultados.

**Hint**: `df.corr()`.

---

### C3. Datos geoespaciales

**Enunciado**: Instalá `geopandas` y creá un GeoDataFrame a partir de coordenadas. Visualizá los puntos en un mapa simple.

---

### C4. Optimizar memoria

**Enunciado**: Analizá el uso de memoria del DataFrame con `df.memory_usage()`. Convertí columnas a tipos más eficientes (category, int32, etc.).

---

### C5. Pipeline de transformación

**Enunciado**: Creá un pipeline que lea un CSV, limpie datos, agregue columnas calculadas, filtre, agrupe y exporte a un nuevo CSV. Todo en una secuencia encadenada usando el estilo de pandas con `.pipe()` o encadenamiento de métodos.

---

*Fin de los ejercicios de la Unidad 3 - Pandas*
