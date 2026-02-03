---
name: geodojo-proyecto-integrador
description: Estructura proyectos integradores YAML que evolucionan entre unidades. Usar cuando se crea un archivo proyecto-integrador.yml o cuando el usuario pide crear el proyecto integrador de una unidad.
---

# Proyectos Integradores GeoDojo (YAML)

Los proyectos integradores son ejercicios extensos que combinan todos los conceptos de una unidad y **evolucionan sobre el proyecto anterior**.

## Ubicación de archivos

Los archivos se guardan en `data/ejercicios/NN/XX-proyecto-integrador.yml` donde:
- `NN` es el número de unidad
- `XX` es el número de archivo (generalmente el último de la unidad)

Después de crear/editar el YAML, ejecutar `make all` para generar markdown y HTML.

## Principio fundamental

> Cada proyecto integrador es una **evolución** del anterior, agregando complejidad con los conceptos nuevos de la unidad.

| Unidad N | Unidad N+1 |
|----------|------------|
| Programa más simple | Evoluciona el programa anterior |
| Usa conceptos hasta N | Agrega conceptos de N+1 |
| Funciones reutilizables | Reutiliza funciones de N |

## Estructura YAML

```yaml
unit:
  number: 1
  title: "Proyecto Integrador: Nombre Descriptivo"
  description: "Un proyecto paso a paso para construir..."

proyecto:
  descripcion: |
    Vamos a construir un programa que:
    - Funcionalidad 1
    - Funcionalidad 2
    - Funcionalidad 3
    
    Este proyecto integra conceptos de la Unidad N: variables, tipos, operadores, etc.
  
  nota: "Este proyecto NO usa estructuras de control..."  # opcional

pasos:
  - numero: 1
    titulo: "Pedir el primer punto"
    objetivo: "Pedir al usuario los datos de un punto geográfico y mostrarlos."
    ejemplo_ejecucion: |
      === Punto 1 ===
      Nombre del lugar: Buenos Aires
      Latitud: -34.6
      Longitud: -58.4
      
      Punto 1: Buenos Aires
      Coordenadas: (-34.6, -58.4)
    hint: "Usá `input()` para pedir texto y `float()` para convertir."
  
  - numero: 2
    titulo: "Pedir el segundo punto"
    objetivo: "Agregar el ingreso del segundo punto."
    ejemplo_ejecucion: |
      ...
    hint: "Repetí la estructura con variables diferentes."

conceptos_utilizados:
  - concepto: "Variables y tipos"
    donde: "Almacenar nombres, latitudes, longitudes"
  - concepto: "f-strings"
    donde: "Formatear el reporte final"
  - concepto: "Funciones con return"
    donde: "distancia_euclidiana(), punto_medio()"

desafios_extra:
  - "Agregar validación básica de coordenadas"
  - "Calcular rumbo entre los dos puntos"
  - "Agregar un tercer punto y calcular el centroide"

# Solo para unidades 2 en adelante:
conexion_unidad_anterior:
  descripcion: "Este proyecto es una evolución del Proyecto de la Unidad N-1"
  comparativa:
    - aspecto: "Cantidad de puntos"
      antes: "2 puntos fijos"
      despues: "N puntos dinámicos"
    - aspecto: "Ejecución"
      antes: "Lineal (una vez)"
      despues: "Menú interactivo (while)"
  funciones_reutilizables:
    - "distancia_euclidiana() → se reutiliza sin cambios"
    - "punto_medio() → se adapta para N puntos"
```

## Secciones del archivo

### 1. unit (información básica)

```yaml
unit:
  number: 1
  title: "Proyecto Integrador: Calculadora de Coordenadas"
  description: "Un proyecto paso a paso para construir una calculadora geográfica."
```

### 2. proyecto (descripción general)

```yaml
proyecto:
  descripcion: |
    Vamos a construir un programa que:
    - Pide al usuario dos puntos geográficos
    - Calcula la distancia entre ellos
    - Genera links de Google Maps
    
    Este proyecto integra conceptos de la Unidad 1: variables, tipos, operadores, strings, f-strings, input/output y funciones.
  nota: "Este proyecto NO usa estructuras de control (if/else, for, while)."
```

### 3. pasos (desarrollo incremental)

```yaml
pasos:
  - numero: 1
    titulo: "Título del paso"
    objetivo: "Qué se logra en este paso"
    ejemplo_ejecucion: |
      Input/output esperado
    hint: "Pista útil"  # opcional
```

Cada paso debe:
- Tener un objetivo claro
- Mostrar ejemplo de ejecución verificable
- Construir sobre el paso anterior

### 4. conceptos_utilizados (tabla resumen)

```yaml
conceptos_utilizados:
  - concepto: "Concepto de Python"
    donde: "Dónde se usa en el proyecto"
```

### 5. desafios_extra

```yaml
desafios_extra:
  - "Desafío que extiende el proyecto"
  - "Desafío que requiere investigación"
```

5-7 desafíos que:
- Extienden el proyecto sin requerir conceptos de unidades futuras
- Algunos requieren investigación independiente
- Preparan conceptualmente para la siguiente unidad

### 6. conexion_unidad_anterior (solo si N > 1)

```yaml
conexion_unidad_anterior:
  descripcion: "Este proyecto evoluciona el de la Unidad anterior"
  comparativa:
    - aspecto: "Característica"
      antes: "Versión simple"
      despues: "Versión evolucionada"
  funciones_reutilizables:
    - "funcion() → cómo se reutiliza"
```

## Patrón de evolución

### Cómo evolucionar el proyecto anterior

1. **Leer** el proyecto integrador de la unidad anterior
2. **Identificar** qué funciones/lógica se pueden reutilizar
3. **Agregar complejidad** usando los conceptos nuevos

| Conceptos nuevos | Cómo agregan complejidad |
|------------------|--------------------------|
| Listas | De N fijo a N variable de elementos |
| Diccionarios | De variables sueltas a estructuras de datos |
| Condicionales | Agregar validación, casos especiales |
| Bucles | De ejecución única a menú interactivo |
| Archivos | Persistir datos entre ejecuciones |
| Módulos | Organizar código en archivos separados |

## Cantidad de pasos

| Unidad | Pasos recomendados |
|--------|-------------------|
| 1 | 7-8 pasos (programa más simple) |
| 2+ | 9-12 pasos (programa más complejo) |

## Hilo conductor temático

Todos los proyectos mantienen un **tema geográfico coherente**:
- Coordenadas, ciudades, rutas
- Cálculos de distancia
- Links de Google Maps
- Contexto argentino/sudamericano

## Pipeline de generación

1. Crear/editar archivo YAML en `data/ejercicios/NN/XX-proyecto-integrador.yml`
2. Ejecutar `make all` para generar markdown y HTML

## Archivos de referencia

- Proyecto U1: `data/ejercicios/01/03-proyecto-integrador.yml`
- Proyecto U2: `data/ejercicios/02/02-proyecto-integrador.yml`

## Proceso para crear un proyecto integrador

1. **Leer** el proyecto integrador de la unidad anterior (si existe)
2. **Identificar** funciones reutilizables
3. **Diseñar** la evolución usando los conceptos nuevos
4. **Escribir** los pasos de forma incremental en YAML
5. **Agregar** la sección de conexión con la unidad anterior (si N > 1)
6. **Crear** desafíos extra
7. **Ejecutar** `make all` para generar los archivos
