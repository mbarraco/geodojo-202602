---
name: geodojo-ejercicios
description: Estructura archivos de ejercicios para cursos de Python con categorías A, B, C y contexto geográfico. Usar cuando se crean o editan archivos en el directorio ejercicios/ o cuando el usuario pide crear ejercicios para una unidad del curso.
---

# Estructura de Ejercicios GeoDojo

Guía para crear archivos de ejercicios consistentes para el curso de Python.

## Estructura del archivo

Cada unidad tiene un archivo `ejercicios/NN-nombre.md` con este formato:

```markdown
# Unidad N: Título

Descripción breve del tema.

---

## Categoría A - Ejercicios fundamentales

[Ejercicios A1-A25]

---

## Categoría B - Ejercicios de práctica extra

[Ejercicios B1-B10]

---

## Categoría C - Desafíos

[Ejercicios C1-C5]
```

## Categorías

| Categoría | Cantidad | Propósito | Dificultad |
|-----------|----------|-----------|------------|
| A | 25 | Fundamentales, necesarios para entender el tema | Incremental (de menor a mayor) |
| B | 10 | Práctica extra, recomendables | Moderada |
| C | 5 | Desafíos opcionales, requieren investigación | Alta |

## Organización de Categoría A

Dividir los 25 ejercicios en 5 bloques de 5 ejercicios cada uno:

```markdown
### Bloque 1: [Tema básico]

---

### A1. Título del ejercicio
...

### A2. Título del ejercicio
...
```

## Formato de cada ejercicio

```markdown
### A1. Título descriptivo

**Enunciado**: Descripción clara del problema con contexto geográfico.

**Ejemplo**:
- Entrada: `valor_ejemplo`
- Salida esperada: `resultado_ejemplo`

**Hint** (opcional): Pista para orientar la resolución.

---
```

### Reglas del formato

1. **Título**: Corto y descriptivo (3-5 palabras)
2. **Enunciado**: Claro, con contexto geográfico cuando sea posible
3. **Ejemplo**: Siempre incluir entrada/salida esperada
4. **Hint**: Opcional, solo si el ejercicio lo requiere
5. **Separador**: Usar `---` entre ejercicios

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

Ver `ejercicios/01/01-fundamentos.md` como referencia de estructura y estilo.

## Nota sobre proyectos integradores

Esta skill es para archivos de ejercicios con categorías A/B/C.

Los **proyectos integradores** (`*-proyecto-integrador.md`) tienen estructura diferente y su propia skill: `.cursor/skills/geodojo-proyecto-integrador/SKILL.md`
