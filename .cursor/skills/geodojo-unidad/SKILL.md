---
name: geodojo-unidad
description: Orquesta la creación de contenido para unidades del curso GeoDojo. Usar cuando se quiera crear una nueva unidad completa, o cuando el usuario pida implementar una unidad del programa.
---

# Creación de Unidades GeoDojo

Guía para estructurar y crear unidades del curso. Esta skill orquesta el proceso y delega la implementación a las skills específicas.

## Fuente de verdad

El programa del curso está en `README.md`. Consultarlo siempre para:
- Ver qué unidades existen
- Entender el tema de cada unidad
- Identificar qué unidades están pendientes

## Estructura de una unidad

Cada unidad `NN` tiene archivos YAML en `data/`:

```
data/ejercicios/NN/
├── 01-grupo-conceptual-1.yml
├── 02-grupo-conceptual-2.yml    # opcional, si el tema lo requiere
└── 0X-proyecto-integrador.yml   # siempre al final

data/clases/NN/
├── 01-grupo-conceptual-1.yml
└── 02-grupo-conceptual-2.yml    # corresponde a cada archivo de ejercicios (excepto proyecto)
```

Los archivos markdown y HTML se **generan automáticamente** con `make all`.

## Proceso para crear una unidad

### Paso 1: Analizar el tema

1. Leer el tema de la unidad en `README.md`
2. Dividir en **grupos conceptuales** (1-3 archivos)
3. Cada grupo debe ser enseñable en una sesión de clase

**Criterios para dividir:**
- ¿Puede enseñarse de forma independiente?
- ¿Tiene suficiente contenido para 25 ejercicios (categoría A)?
- ¿Es un prerequisito para otro grupo?

**Ejemplo**: "Tipos de datos, operadores, funciones básicas" se dividió en:
- `01-fundamentos.yml` (tipos, variables, operadores)
- `02-funciones.yml` (funciones built-in)

### Paso 2: Crear estructura de directorios

```bash
mkdir -p data/ejercicios/NN data/clases/NN
```

### Paso 3: Crear archivos de ejercicios

Para cada grupo conceptual, crear el archivo YAML de ejercicios.

**Delegar a**: `.cursor/skills/geodojo-ejercicios/SKILL.md`

Orden:
1. `data/ejercicios/NN/01-grupo-1.yml`
2. `data/ejercicios/NN/02-grupo-2.yml` (si aplica)

**Nota**: El proyecto integrador se crea en el Paso 5, con su propia skill.

### Paso 4: Crear archivos de clase

Por cada archivo de ejercicios (excepto proyecto integrador), crear la guía de clase correspondiente.

**Delegar a**: `.cursor/skills/geodojo-clase/SKILL.md`

La clase se genera **a partir** del archivo de ejercicios correspondiente.

### Paso 5: Proyecto integrador

El último archivo de ejercicios de cada unidad es un proyecto especial.

**Delegar a**: `.cursor/skills/geodojo-proyecto-integrador/SKILL.md`

Características:
- Combina todos los conceptos de la unidad
- **Evoluciona sobre el proyecto de la unidad anterior** (excepto U1)
- No tiene archivo de clase asociado
- Estructura de pasos incrementales, no categorías A/B/C

### Paso 6: Generar archivos

Después de crear todos los YAML, ejecutar:

```bash
make all
```

Esto genera:
- Markdown en `ejercicios/` y `clases/`
- HTML en `web/`

## Convenciones de nombres

| Componente | Formato | Ejemplo |
|------------|---------|---------|
| Directorio unidad | `NN/` (dos dígitos) | `01/`, `02/` |
| Archivo tema | `NN-nombre-descriptivo.yml` | `01-fundamentos.yml` |
| Proyecto integrador | `0X-proyecto-integrador.yml` | `03-proyecto-integrador.yml` |

## Verificar estado actual

Para saber qué está implementado:

```bash
ls data/ejercicios/
ls data/clases/
```

Comparar con el programa en `README.md`.

## Skills relacionadas

| Skill | Cuándo usar |
|-------|-------------|
| `geodojo-ejercicios` | Al crear archivos de ejercicios (NO proyecto integrador) |
| `geodojo-clase` | Al crear cada archivo en `data/clases/NN/` |
| `geodojo-proyecto-integrador` | Al crear el proyecto integrador de la unidad |

## Pipeline de generación

```
data/*.yml  →  make markdown  →  ejercicios/*.md, clases/*.md
            →  make html      →  web/*.html
            →  make all       →  ambos
```

## Checklist para unidad completa

- [ ] Tema analizado y dividido en grupos conceptuales
- [ ] Directorios `data/ejercicios/NN/` y `data/clases/NN/` creados
- [ ] Archivo YAML de ejercicios para cada grupo conceptual
- [ ] Archivo YAML de clase para cada grupo conceptual
- [ ] Proyecto integrador YAML creado
- [ ] `make all` ejecutado para generar markdown y HTML
