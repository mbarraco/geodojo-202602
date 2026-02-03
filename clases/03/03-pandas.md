# Clase 3: Pandas para Datos Geográficos

Guía para la clase sobre lectura y manipulación de datos con Pandas.

---

## 1. Temario

### 1.1 Cargar datos y exploración básica

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `pd.read_csv(path)` | Lee archivo CSV | `df = pd.read_csv("datos.csv")` |
| `df.head(n)` | Primeras n filas | `df.head(5)` |
| `df.tail(n)` | Últimas n filas | `df.tail(3)` |
| `df.shape` | Dimensiones (filas, cols) | `(100, 5)` |
| `df.columns` | Nombres de columnas | `['nombre', 'lat', 'lon']` |
| `df.dtypes` | Tipos de datos | `nombre: object, lat: float64` |
| `df.describe()` | Estadísticas básicas | Media, std, min, max, etc. |

### 1.2 Selección con loc e iloc

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `df["col"]` | Selecciona columna | `df["nombre"]` |
| `df[["c1", "c2"]]` | Múltiples columnas | `df[["nombre", "lat"]]` |
| `df.iloc[i]` | Fila por posición | `df.iloc[0]` → primera fila |
| `df.iloc[i:j]` | Rango de filas | `df.iloc[0:5]` |
| `df.iloc[i, j]` | Celda específica | `df.iloc[0, 2]` |
| `df.loc[label]` | Fila por etiqueta | `df.loc["Buenos Aires"]` |
| `df.loc[label, col]` | Celda por etiqueta | `df.loc["BA", "lat"]` |

### 1.3 Filtrado de datos

| Operación | Sintaxis | Ejemplo |
|-----------|----------|---------|
| Condición simple | `df[df["col"] > x]` | `df[df["poblacion"] > 1000000]` |
| Múltiples condiciones | `df[(cond1) & (cond2)]` | `df[(df["lat"] < -30) & (df["lon"] < -60)]` |
| OR lógico | `df[(cond1) \| (cond2)]` | `df[(df["region"] == "N") \| (df["region"] == "S")]` |
| Método query | `df.query("expr")` | `df.query("poblacion > 1000000")` |
| Está en lista | `df[df["col"].isin(lista)]` | `df[df["nombre"].isin(["BA", "CB"])]` |
| String contiene | `df[df["col"].str.contains("x")]` | `df[df["nombre"].str.contains("Aires")]` |

### 1.4 Agrupación y agregación

| Operación | Sintaxis | Resultado |
|-----------|----------|-----------|
| Agrupar | `df.groupby("col")` | Objeto GroupBy |
| Contar | `grouped.size()` | Serie con conteos |
| Sumar | `grouped["col"].sum()` | Serie con sumas |
| Promedio | `grouped["col"].mean()` | Serie con promedios |
| Múltiples | `grouped.agg(["sum", "mean"])` | DataFrame |
| Agg personalizado | `grouped.agg({"col1": "sum", "col2": "mean"})` | DataFrame |

### 1.5 Guardar y combinar DataFrames

| Operación | Sintaxis | Uso |
|-----------|----------|-----|
| Guardar CSV | `df.to_csv(path, index=False)` | Exportar datos |
| Ordenar | `df.sort_values("col")` | Ordenar por columna |
| Concatenar | `pd.concat([df1, df2])` | Unir filas |
| Merge | `pd.merge(df1, df2, on="col")` | JOIN por columna |
| Nueva columna | `df["nueva"] = valor` | Agregar columna |
| Columna calculada | `df["c"] = df["a"] + df["b"]` | Operaciones |

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo, cubriendo todos los temas.

---

### 2.1 Enunciados (para mostrar en clase)

---

#### Ejemplo 1: Leer CSV con pandas
Leer un archivo CSV de ciudades argentinas y mostrar el DataFrame.

---

#### Ejemplo 2: Explorar el DataFrame
Ver las primeras filas, la forma, las columnas y las estadísticas básicas.

---

#### Ejemplo 3: Seleccionar columnas
Crear un nuevo DataFrame con solo nombre y población.

---

#### Ejemplo 4: Acceder a filas con iloc
Obtener la primera ciudad, las primeras 3, y una celda específica.

---

#### Ejemplo 5: Filtrar por condición
Mostrar solo ciudades con más de 1 millón de habitantes.

---

#### Ejemplo 6: Filtrar con múltiples condiciones
Ciudades del hemisferio sur (lat < 0) con longitud oeste de -60.

---

#### Ejemplo 7: Agregar columna calculada
Crear una columna "hemisferio" basada en la latitud.

---

#### Ejemplo 8: Agrupar y agregar
Contar ciudades por región y calcular población total por región.

---

#### Ejemplo 9: Ordenar y guardar
Ordenar por población descendente y guardar en nuevo CSV.

---

#### Ejemplo 10: Combinar DataFrames
Hacer merge de datos de ciudades con datos de clima.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

---

#### Ejemplo 1: Leer CSV con pandas

**Enunciado**: Leer un archivo CSV de ciudades argentinas y mostrar el DataFrame.

```python
import pandas as pd

# Crear CSV de ejemplo
datos = """nombre,latitud,longitud,poblacion,region
Buenos Aires,-34.6,-58.4,2890000,Pampeana
Córdoba,-31.4,-64.2,1430000,Pampeana
Rosario,-33.0,-60.7,1270000,Pampeana
Mendoza,-32.9,-68.8,115000,Cuyo
Salta,-24.8,-65.4,620000,Norte"""

with open("ciudades.csv", "w") as f:
    f.write(datos)

# Leer con pandas
df = pd.read_csv("ciudades.csv")
print(df)
```

**Salida**:
```
         nombre  latitud  longitud  poblacion    region
0  Buenos Aires    -34.6     -58.4    2890000  Pampeana
1       Córdoba    -31.4     -64.2    1430000  Pampeana
2       Rosario    -33.0     -60.7    1270000  Pampeana
3       Mendoza    -32.9     -68.8     115000      Cuyo
4         Salta    -24.8     -65.4     620000     Norte
```

---

#### Ejemplo 2: Explorar el DataFrame

**Enunciado**: Ver las primeras filas, la forma, las columnas y las estadísticas.

```python
print("Primeras 3 filas:")
print(df.head(3))

print(f"\nForma: {df.shape}")
print(f"Columnas: {list(df.columns)}")

print("\nEstadísticas:")
print(df.describe())
```

**Salida**:
```
Primeras 3 filas:
         nombre  latitud  longitud  poblacion    region
0  Buenos Aires    -34.6     -58.4    2890000  Pampeana
1       Córdoba    -31.4     -64.2    1430000  Pampeana
2       Rosario    -33.0     -60.7    1270000  Pampeana

Forma: (5, 5)
Columnas: ['nombre', 'latitud', 'longitud', 'poblacion', 'region']

Estadísticas:
         latitud   longitud      poblacion
count   5.000000   5.000000   5.000000e+00
mean  -31.340000 -63.500000   1.265000e+06
...
```

---

#### Ejemplo 3: Seleccionar columnas

**Enunciado**: Crear un nuevo DataFrame con solo nombre y población.

```python
# Una columna (Serie)
nombres = df["nombre"]
print("Columna nombre:")
print(nombres)

# Múltiples columnas (DataFrame)
df_reducido = df[["nombre", "poblacion"]]
print("\nNombre y población:")
print(df_reducido)
```

**Salida**:
```
Columna nombre:
0    Buenos Aires
1         Córdoba
2         Rosario
3         Mendoza
4           Salta
Name: nombre, dtype: object

Nombre y población:
         nombre  poblacion
0  Buenos Aires    2890000
1       Córdoba    1430000
2       Rosario    1270000
3       Mendoza     115000
4         Salta     620000
```

---

#### Ejemplo 4: Acceder a filas con iloc

**Enunciado**: Obtener la primera ciudad, las primeras 3, y una celda específica.

```python
# Primera fila (Serie)
print("Primera ciudad:")
print(df.iloc[0])

# Primeras 3 filas (DataFrame)
print("\nPrimeras 3 ciudades:")
print(df.iloc[0:3])

# Celda específica: fila 0, columna 3 (población)
poblacion_ba = df.iloc[0, 3]
print(f"\nPoblación de Buenos Aires: {poblacion_ba}")
```

**Salida**:
```
Primera ciudad:
nombre       Buenos Aires
latitud             -34.6
longitud            -58.4
poblacion         2890000
region           Pampeana
Name: 0, dtype: object

Primeras 3 ciudades:
         nombre  latitud  longitud  poblacion    region
0  Buenos Aires    -34.6     -58.4    2890000  Pampeana
1       Córdoba    -31.4     -64.2    1430000  Pampeana
2       Rosario    -33.0     -60.7    1270000  Pampeana

Población de Buenos Aires: 2890000
```

---

#### Ejemplo 5: Filtrar por condición

**Enunciado**: Mostrar solo ciudades con más de 1 millón de habitantes.

```python
# Crear máscara booleana
mascara = df["poblacion"] > 1000000
print("Máscara:")
print(mascara)

# Aplicar filtro
grandes = df[df["poblacion"] > 1000000]
print("\nCiudades con más de 1M habitantes:")
print(grandes)
```

**Salida**:
```
Máscara:
0     True
1     True
2     True
3    False
4    False
Name: poblacion, dtype: bool

Ciudades con más de 1M habitantes:
         nombre  latitud  longitud  poblacion    region
0  Buenos Aires    -34.6     -58.4    2890000  Pampeana
1       Córdoba    -31.4     -64.2    1430000  Pampeana
2       Rosario    -33.0     -60.7    1270000  Pampeana
```

---

#### Ejemplo 6: Filtrar con múltiples condiciones

**Enunciado**: Ciudades del hemisferio sur (lat < 0) con longitud oeste de -60.

```python
# Ambas condiciones deben cumplirse
filtro = df[(df["latitud"] < 0) & (df["longitud"] < -60)]

print("Ciudades al sur y oeste de -60:")
print(filtro[["nombre", "latitud", "longitud"]])
```

**Salida**:
```
Ciudades al sur y oeste de -60:
    nombre  latitud  longitud
1  Córdoba    -31.4     -64.2
2  Rosario    -33.0     -60.7
3  Mendoza    -32.9     -68.8
4    Salta    -24.8     -65.4
```

---

#### Ejemplo 7: Agregar columna calculada

**Enunciado**: Crear una columna "hemisferio" basada en la latitud.

```python
# Usando apply con función lambda
df["hemisferio"] = df["latitud"].apply(
    lambda x: "Sur" if x < 0 else "Norte"
)

print(df[["nombre", "latitud", "hemisferio"]])
```

**Salida**:
```
         nombre  latitud hemisferio
0  Buenos Aires    -34.6        Sur
1       Córdoba    -31.4        Sur
2       Rosario    -33.0        Sur
3       Mendoza    -32.9        Sur
4         Salta    -24.8        Sur
```

---

#### Ejemplo 8: Agrupar y agregar

**Enunciado**: Contar ciudades por región y calcular población total.

```python
# Contar por región
conteo = df.groupby("region").size()
print("Ciudades por región:")
print(conteo)

# Población total por región
poblacion_region = df.groupby("region")["poblacion"].sum()
print("\nPoblación por región:")
print(poblacion_region)

# Múltiples estadísticas
stats = df.groupby("region")["poblacion"].agg(["count", "sum", "mean"])
print("\nEstadísticas por región:")
print(stats)
```

**Salida**:
```
Ciudades por región:
region
Cuyo        1
Norte       1
Pampeana    3
dtype: int64

Población por región:
region
Cuyo         115000
Norte        620000
Pampeana    5590000
Name: poblacion, dtype: int64

Estadísticas por región:
          count      sum          mean
region                                
Cuyo          1   115000  115000.000000
Norte         1   620000  620000.000000
Pampeana      3  5590000 1863333.333333
```

---

#### Ejemplo 9: Ordenar y guardar

**Enunciado**: Ordenar por población descendente y guardar en nuevo CSV.

```python
# Ordenar de mayor a menor población
df_ordenado = df.sort_values("poblacion", ascending=False)
print("Ordenado por población:")
print(df_ordenado[["nombre", "poblacion"]])

# Guardar a CSV (sin índice)
df_ordenado.to_csv("ciudades_ordenadas.csv", index=False)
print("\nArchivo guardado!")
```

**Salida**:
```
Ordenado por población:
         nombre  poblacion
0  Buenos Aires    2890000
1       Córdoba    1430000
2       Rosario    1270000
4         Salta     620000
3       Mendoza     115000

Archivo guardado!
```

---

#### Ejemplo 10: Combinar DataFrames

**Enunciado**: Hacer merge de datos de ciudades con datos de clima.

```python
# Crear DataFrame de clima
clima = pd.DataFrame({
    "ciudad": ["Buenos Aires", "Córdoba", "Mendoza"],
    "temp_media": [18.5, 17.2, 16.8],
    "precipitacion": [1200, 800, 200]
})

# Merge por nombre de ciudad
df_completo = pd.merge(
    df, 
    clima, 
    left_on="nombre", 
    right_on="ciudad"
)

print("Datos combinados:")
print(df_completo[["nombre", "poblacion", "temp_media", "precipitacion"]])
```

**Salida**:
```
Datos combinados:
         nombre  poblacion  temp_media  precipitacion
0  Buenos Aires    2890000        18.5           1200
1       Córdoba    1430000        17.2            800
2       Mendoza     115000        16.8            200
```

---

## Notas para el docente

- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Crear el CSV inicial es importante para que todos trabajen con los mismos datos
- Enfatizar la diferencia entre `iloc` (posición) y `loc` (etiqueta)
- El filtrado con múltiples condiciones requiere paréntesis y operadores `&` / `|`
- `groupby` es muy poderoso - dedicarle tiempo suficiente
- Los ejercicios en `ejercicios/03/03-pandas.md` refuerzan estos conceptos
- Contexto geográfico: ciudades argentinas, coordenadas, regiones, población
