---
name: geodojo-clase
description: Genera archivos YAML de guía de clase. Usar cuando se crea un archivo en data/clases/ o cuando el usuario pide crear una guía de clase para una unidad del curso.
---

# Generación de Guías de Clase (YAML)

Guía para crear archivos YAML de clase (`data/clases/NN/XX-tema.yml`).

## Ubicación de archivos

Los archivos de clase se guardan en `data/clases/NN/XX-nombre.yml` donde:
- `NN` es el número de unidad (00, 01, 02, etc.)
- `XX` es el número de archivo dentro de la unidad

Después de crear/editar el YAML, ejecutar `make markdown` para generar el markdown correspondiente.

## Estructura YAML

```yaml
unit:
  number: 1
  title: "Título de la clase"
  description: "Guía para la clase sobre [descripción breve]."

temario:
  - title: "Tema del bloque 1"
    columns: ["Concepto", "Descripción"]  # o ["Operador", "Operación", "Ejemplo"]
    rows:
      - ["Variable", "Nombre que almacena un valor (`nombre = \"Buenos Aires\"`)"]
      - ["`str`", "Texto, entre comillas (`\"hola\"`, `'mundo'`)"]
  - title: "Tema del bloque 2"
    columns: ["Operador", "Operación", "Ejemplo"]
    rows:
      - ["`+`", "Suma", "`5 + 3` → `8`"]
      - ["`-`", "Resta", "`10 - 4` → `6`"]

ejemplos:
  - id: 1
    title: "Variables básicas"
    enunciado: |
      Crear variables para almacenar el nombre, latitud y longitud de Buenos Aires.
      Mostrar cada una.
    solucion:
      code: |
        nombre = "Buenos Aires"
        latitud = -34.6
        longitud = -58.4
        print(nombre)
        print(latitud)
        print(longitud)
      salida: |
        Buenos Aires
        -34.6
        -58.4
  - id: 2
    title: "Tipos de datos"
    enunciado: "Usando las variables anteriores, mostrar el tipo de cada una con `type()`."
    solucion:
      code: |
        # código...
      salida: |
        <class 'str'>
        <class 'float'>

notas_docente:
  - "Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero"
  - "Cada ejemplo introduce 1-2 conceptos nuevos de forma incremental"
  - "Se recomienda pedir participación: \"¿Qué tipo creen que tiene esta variable?\""
  - "Los ejercicios en `ejercicios/01/01-fundamentos.md` refuerzan estos mismos conceptos"
```

## Relación ejercicios → clase

```
data/ejercicios/NN/XX-tema.yml          data/clases/NN/XX-tema.yml
============================            ==========================

Categoría A (25 ejercicios)        -->  temario (tablas)
  - Bloque 1: Tema X                      - title: Tema X
  - Bloque 2: Tema Y                      - title: Tema Y

Temas de todos los bloques         -->  ejemplos (10 para hacer en vivo)
                                          - Con enunciado y solución

                                        notas_docente
```

## Secciones del archivo

### 1. unit (información de la clase)

```yaml
unit:
  number: 1  # número de la clase/unidad
  title: "Fundamentos de Python"
  description: "Guía para la clase sobre tipos de datos, operadores y funciones básicas."
```

### 2. temario (tablas de conceptos)

Por cada bloque del archivo de ejercicios correspondiente, crear una sección de temario con formato tabla:

```yaml
temario:
  - title: "Variables y tipos de datos"
    columns: ["Concepto", "Descripción"]
    rows:
      - ["Variable", "Nombre que almacena un valor"]
      - ["`str`", "Texto, entre comillas"]
```

Columnas comunes:
- `["Concepto", "Descripción"]`
- `["Operador", "Operación", "Ejemplo"]`
- `["Función", "Descripción", "Ejemplo"]`

### 3. ejemplos (10 para hacer en vivo)

```yaml
ejemplos:
  - id: 1
    title: "Título descriptivo"
    enunciado: "Descripción del problema a resolver en vivo."
    solucion:
      code: |
        # código Python
        print("resultado")
      salida: |
        resultado
```

Los ejemplos deben:
- Cubrir **todos los temas** del temario
- Ser **progresivos** (de menor a mayor complejidad)
- Ser **diferentes** a los ejercicios (no copiar ejercicios)
- Usar **contexto geográfico** consistente
- Ser apropiados para **hacer en vivo** (no muy largos)

**Distribución sugerida**:

| Ejemplos | Temas a cubrir |
|----------|----------------|
| 1-2 | Bloque 1 (más básico) |
| 3-4 | Bloque 2 |
| 5-6 | Bloque 3 |
| 7-8 | Bloque 4 |
| 9-10 | Bloque 5 (más avanzado) |

### 4. notas_docente

```yaml
notas_docente:
  - "Los ejemplos están diseñados para hacerse en vivo"
  - "Cada ejemplo introduce 1-2 conceptos nuevos"
  - "Referencia: ejercicios/01/01-fundamentos.md"
```

## Pipeline de generación

1. Crear/editar archivo YAML en `data/clases/NN/XX-nombre.yml`
2. Ejecutar `make markdown` para generar `clases/NN/XX-nombre.md`
3. Ejecutar `make html` para generar la versión web

O usar `make all` para ejecutar ambos pasos.

## Archivos de referencia

- Ejemplo de clase: `data/clases/01/01-fundamentos.yml`
- Ejemplo de ejercicios: `data/ejercicios/01/01-fundamentos.yml`
- Skill de ejercicios: `.cursor/skills/geodojo-ejercicios/SKILL.md`
