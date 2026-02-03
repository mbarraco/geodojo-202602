---
name: geodojo-ejercicios
description: Estructura archivos YAML de ejercicios para cursos de Python con categorías A, B, C y contexto geográfico. Usar cuando se crean o editan archivos en el directorio data/ejercicios/ o cuando el usuario pide crear ejercicios para una unidad del curso.
---

# Estructura de Ejercicios GeoDojo (YAML)

Guía para crear archivos YAML de ejercicios consistentes para el curso de Python.

## Ubicación de archivos

Los archivos de ejercicios se guardan en `data/ejercicios/NN/XX-nombre.yml` donde:
- `NN` es el número de unidad (01, 02, etc.)
- `XX` es el número de archivo dentro de la unidad

Después de crear/editar el YAML, ejecutar `make markdown` para generar el markdown correspondiente.

## Estructura YAML

```yaml
unit:
  number: 1
  title: "Título de la unidad"
  description: "Descripción breve del tema."

categories:
  - id: A
    title: "Ejercicios fundamentales"
    description: "Se recomienda hacerlos todos. Están ordenados por dificultad incremental."
    blocks:
      - name: "Tema del bloque 1"
        exercises:
          - id: A1
            title: "Título del ejercicio"
            enunciado: "Descripción clara del problema con contexto geográfico."
            ejemplo:
              entrada: "valor_ejemplo"  # opcional
              salida: "resultado_ejemplo"
            hint: "Pista para orientar la resolución."  # opcional
          - id: A2
            # ... más ejercicios
      - name: "Tema del bloque 2"
        exercises:
          # ... ejercicios A6-A10
      # ... bloques 3, 4, 5

  - id: B
    title: "Ejercicios de práctica extra"
    description: "Recomendables para quienes quieran practicar más."
    exercises:  # Sin bloques, ejercicios directos
      - id: B1
        title: "Título"
        enunciado: "..."
        ejemplo:
          salida: "..."

  - id: C
    title: "Desafíos"
    description: "Ejercicios opcionales que requieren mayor dificultad o investigación."
    exercises:
      - id: C1
        # ...
```

## Categorías

| Categoría | Cantidad | Propósito | Dificultad |
|-----------|----------|-----------|------------|
| A | 25 | Fundamentales, necesarios para entender el tema | Incremental (de menor a mayor) |
| B | 10 | Práctica extra, recomendables | Moderada |
| C | 5 | Desafíos opcionales, requieren investigación | Alta |

## Organización de Categoría A

Dividir los 25 ejercicios en 5 bloques de 5 ejercicios cada uno.

## Formato de cada ejercicio

```yaml
- id: A1
  title: "Título descriptivo"
  enunciado: |
    Descripción clara del problema con contexto geográfico.
    Puede ser multilínea usando |
  ejemplo:
    entrada: "valor_ejemplo"  # opcional, solo si hay input del usuario
    salida: |
      resultado_ejemplo
      puede ser multilínea
  hint: "Pista para orientar la resolución."  # opcional
```

### Reglas del formato

1. **id**: Código del ejercicio (A1, A2, B1, C1, etc.)
2. **title**: Corto y descriptivo (3-5 palabras)
3. **enunciado**: Claro, con contexto geográfico cuando sea posible
4. **ejemplo**: Siempre incluir salida esperada, entrada solo si hay input
5. **hint**: Opcional, solo si el ejercicio lo requiere

## Contexto geográfico

Usar ejemplos relacionados con geografía:

- Coordenadas (latitud, longitud)
- Ciudades y países (preferencia por Argentina y Sudamérica)
- Distancias y áreas
- Altitudes y elevaciones
- Puntos cardinales
- Husos horarios

## Progresión de dificultad

En la Categoría A, cada bloque debe ser más difícil que el anterior:

| Bloque | Nivel | Descripción |
|--------|-------|-------------|
| 1 | Básico | Concepto más simple, sin combinar |
| 2 | Básico+ | Variaciones del concepto |
| 3 | Intermedio | Combinar con conceptos previos |
| 4 | Intermedio+ | Agregar complejidad |
| 5 | Avanzado | Combinar múltiples técnicas |

## Ejemplo de archivo completo

Ver `data/ejercicios/01/01-fundamentos.yml` como referencia de estructura y estilo.

## Pipeline de generación

1. Crear/editar archivo YAML en `data/ejercicios/NN/XX-nombre.yml`
2. Ejecutar `make markdown` para generar `ejercicios/NN/XX-nombre.md`
3. Ejecutar `make html` para generar la versión web

O usar `make all` para ejecutar ambos pasos.

## Nota sobre proyectos integradores

Esta skill es para archivos de ejercicios con categorías A/B/C.

Los **proyectos integradores** (`*-proyecto-integrador.yml`) tienen estructura diferente y su propia skill: `.cursor/skills/geodojo-proyecto-integrador/SKILL.md`
