---
name: geodojo-clase
description: Genera archivos de guía de clase a partir de archivos de ejercicios. Usar cuando se crea un archivo en clases/ o cuando el usuario pide crear una guía de clase para una unidad del curso.
---

# Generación de Guías de Clase

Guía para crear archivos de clase (`clases/NN/XX-tema.md`) a partir de archivos de ejercicios (`ejercicios/NN/XX-tema.md`).

## Relación ejercicios → clase

```
ejercicios/NN/XX-tema.md              clases/NN/XX-tema.md
========================              ====================

Categoría A (25 ejercicios)     -->   1. Temario (tablas)
  - Bloque 1: Tema X                     - 1.1 Tema X
  - Bloque 2: Tema Y                     - 1.2 Tema Y
  - Bloque 3: Tema Z                     - 1.3 Tema Z
  - ...                                  - ...

Temas de todos los bloques      -->   2. Ejemplos para la clase
                                         - 2.1 Solo enunciados
                                         - 2.2 Con soluciones

                                      Notas para el docente
```

## Estructura del archivo de clase

```markdown
# Clase N: Título

Guía para la clase sobre [descripción breve].

---

## 1. Temario

### 1.1 Tema del bloque 1
| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| ... | ... | ... |

### 1.2 Tema del bloque 2
...

---

## 2. Ejemplos para la clase

10 ejemplos progresivos para hacer en vivo.

### 2.1 Enunciados (para mostrar en clase)

#### Ejemplo 1: Título
Descripción del problema.

---

### 2.2 Enunciados + Soluciones (referencia del docente)

#### Ejemplo 1: Título

**Enunciado**: Descripción.

\`\`\`python
# código solución
\`\`\`

**Salida**:
\`\`\`
resultado
\`\`\`

---

## Notas para el docente

- Consejos pedagógicos
- Referencia al archivo de ejercicios
```

## Proceso de transformación

### Paso 1: Identificar bloques

Leer el archivo de ejercicios y extraer los nombres de los **bloques de la Categoría A**:

```
### Bloque 1: Variables y print
### Bloque 2: Operadores aritméticos
### Bloque 3: Strings y formateo
...
```

### Paso 2: Crear temario en tablas

Por cada bloque, crear una sección de temario con formato tabla:

| Columnas recomendadas | Uso |
|----------------------|-----|
| Concepto / Operador / Función | Nombre del elemento |
| Descripción | Qué hace o para qué sirve |
| Ejemplo | Código y resultado: `` `código` → `resultado` `` |

**Ejemplo de tabla**:

```markdown
### 1.2 Operadores aritméticos

| Operador | Operación | Ejemplo |
|----------|-----------|---------|
| `+` | Suma | `5 + 3` → `8` |
| `-` | Resta | `10 - 4` → `6` |
| `*` | Multiplicación | `6 * 7` → `42` |
```

### Paso 3: Diseñar 10 ejemplos

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

### Paso 4: Escribir ejemplos en dos versiones

**Versión 2.1 - Solo enunciados** (para proyectar):
```markdown
#### Ejemplo 3: Operaciones aritméticas
Calcular el promedio de tres temperaturas: 25.5, 28.3 y 22.1 grados.
```

**Versión 2.2 - Con solución** (referencia docente):
```markdown
#### Ejemplo 3: Operaciones aritméticas

**Enunciado**: Calcular el promedio de tres temperaturas: 25.5, 28.3 y 22.1 grados.

\`\`\`python
temp1 = 25.5
temp2 = 28.3
temp3 = 22.1

promedio = (temp1 + temp2 + temp3) / 3
print(f"Promedio: {round(promedio, 1)}°C")
\`\`\`

**Salida**:
\`\`\`
Promedio: 25.3°C
\`\`\`
```

### Paso 5: Agregar notas para el docente

Incluir al final:
- Que los ejemplos son para hacer en vivo
- Progresión de conceptos
- Sugerencias de participación
- Referencia al archivo de ejercicios correspondiente
- Contexto temático usado

**Ejemplo**:
```markdown
## Notas para el docente

- Los ejemplos están diseñados para hacerse en vivo, escribiendo el código desde cero
- Cada ejemplo introduce 1-2 conceptos nuevos de forma incremental
- Se recomienda pedir participación: "¿Qué tipo creen que tiene esta variable?"
- Los ejercicios en `ejercicios/01/01-fundamentos.md` refuerzan estos mismos conceptos
- Contexto geográfico consistente: coordenadas, ciudades, distancias
```

## Archivos de referencia

- Ejemplo de clase: `clases/01/01-fundamentos.md`
- Ejemplo de ejercicios: `ejercicios/01/01-fundamentos.md`
- Skill de ejercicios: `.cursor/skills/geodojo-ejercicios/SKILL.md`
