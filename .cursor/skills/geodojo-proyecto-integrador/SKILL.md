---
name: geodojo-proyecto-integrador
description: Estructura proyectos integradores que evolucionan entre unidades. Usar cuando se crea un archivo proyecto-integrador.md o cuando el usuario pide crear el proyecto integrador de una unidad.
---

# Proyectos Integradores GeoDojo

Los proyectos integradores son ejercicios extensos que combinan todos los conceptos de una unidad y **evolucionan sobre el proyecto anterior**.

## Principio fundamental

> Cada proyecto integrador es una **evolución** del anterior, agregando complejidad con los conceptos nuevos de la unidad.

| Unidad N | Unidad N+1 |
|----------|------------|
| Programa más simple | Evoluciona el programa anterior |
| Usa conceptos hasta N | Agrega conceptos de N+1 |
| Funciones reutilizables | Reutiliza funciones de N |

## Estructura del archivo

```markdown
# Proyecto Integrador: [Nombre descriptivo]

Un proyecto paso a paso para construir [descripción breve].

---

## Descripción del proyecto

Vamos a construir un programa que:
- [Funcionalidad 1]
- [Funcionalidad 2]
- ...

Este proyecto integra conceptos de la Unidad N: [lista de conceptos].
[Si N > 1]: También reutiliza funciones de la Unidad N-1.

---

## Paso 1: [Título]

**Objetivo**: [Qué se logra en este paso]

**Tareas**:
1. [Tarea específica]
2. [Tarea específica]

**Ejemplo de ejecución**:
\`\`\`
[Input/output esperado]
\`\`\`

**Hint**: [Pista útil]

---

## Paso N: Programa completo

**Objetivo**: Integrar todo en un programa con salida bien formateada.

**Ejemplo de ejecución completa**:
\`\`\`
[Ejecución completa del programa final]
\`\`\`

---

## Conceptos utilizados

| Concepto | Dónde se usa |
|----------|--------------|
| [Concepto] | [Ubicación en el proyecto] |

---

## Desafíos extra

1. [Desafío que extiende el proyecto]
2. [Desafío que requiere investigación]

---

## Conexión con la Unidad anterior

[Solo si N > 1]

Este proyecto es una evolución del Proyecto Integrador de la Unidad N-1:

| Unidad N-1 | Unidad N |
|------------|----------|
| [Característica simple] | [Característica evolucionada] |

Funciones reutilizables:
- `funcion_anterior()` → `funcion_nueva()`

---

*Fin del proyecto integrador - Unidad N*
```

## Patrón de evolución

### Cómo evolucionar el proyecto anterior

1. **Leer** el proyecto integrador de la unidad anterior
2. **Identificar** qué funciones/lógica se pueden reutilizar
3. **Agregar complejidad** usando los conceptos nuevos:

| Conceptos nuevos | Cómo agregan complejidad |
|------------------|--------------------------|
| Listas | De N fijo a N variable de elementos |
| Diccionarios | De variables sueltas a estructuras de datos |
| Condicionales | Agregar validación, casos especiales |
| Bucles | De ejecución única a menú interactivo |
| Archivos | Persistir datos entre ejecuciones |
| Módulos | Organizar código en archivos separados |

### Ejemplo concreto

**Unidad 1**: Calculadora de 2 puntos
```
- 2 puntos hardcodeados por input
- Programa lineal (se ejecuta una vez)
- Sin validación
- Variables simples
```

**Unidad 2**: Planificador de N puntos
```
- N puntos dinámicos (lista)
- Menú interactivo (while + if/elif)
- Validación de coordenadas (if)
- Lista de diccionarios
- Reutiliza: distancia_euclidiana(), formatear_coordenada()
```

## Hilo conductor temático

Todos los proyectos mantienen un **tema geográfico coherente**:
- Coordenadas, ciudades, rutas
- Cálculos de distancia
- Links de Google Maps
- Contexto argentino/sudamericano

Esto permite que la evolución sea natural: el usuario ya conoce el dominio.

## Cantidad de pasos

| Unidad | Pasos recomendados |
|--------|-------------------|
| 1 | 7-8 pasos (programa más simple) |
| 2+ | 9-12 pasos (programa más complejo) |

Cada paso debe:
- Tener un objetivo claro
- Ser verificable (mostrar output esperado)
- Construir sobre el paso anterior

## Sección "Conexión con Unidad anterior"

**Obligatoria** para unidades 2 en adelante. Debe incluir:

1. Tabla comparativa de características
2. Lista de funciones reutilizables
3. Explicación de cómo evoluciona el proyecto

## Sección "Desafíos extra"

5-7 desafíos que:
- Extienden el proyecto sin requerir conceptos de unidades futuras
- Algunos requieren investigación independiente
- Preparan conceptualmente para la siguiente unidad

## Archivos de referencia

- Proyecto U1: `ejercicios/01/03-proyecto-integrador.md`
- Proyecto U2: `ejercicios/02/02-proyecto-integrador.md`

## Proceso para crear un proyecto integrador

1. **Leer** el proyecto integrador de la unidad anterior
2. **Identificar** funciones reutilizables
3. **Diseñar** la evolución usando los conceptos nuevos
4. **Escribir** los pasos de forma incremental
5. **Agregar** la sección de conexión con la unidad anterior
6. **Crear** desafíos extra
