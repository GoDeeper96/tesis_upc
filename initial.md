# EXPERTO TEMÁTICO — DOCUMENTO INICIAL DE TESIS
## Sistema de Generación Automatizada de Materiales Instruccionales mediante Inteligencia Artificial

> **Institución:** Universidad Peruana de Ciencias Aplicadas (UPC)
> **Área temática:** Ingeniería de Software / Inteligencia Artificial Aplicada a la Educación
> **Fecha de elaboración:** Marzo 2026
> **Estado:** Borrador inicial — base para desarrollo de tesis

---

## ÍNDICE

1. [Contexto y Motivación](#1-contexto-y-motivación)
2. [Planteamiento del Problema](#2-planteamiento-del-problema)
3. [Hipótesis de Trabajo](#3-hipótesis-de-trabajo)
4. [Objetivos](#4-objetivos)
5. [Justificación del Proyecto](#5-justificación-del-proyecto)
6. [Marco Teórico](#6-marco-teórico)
7. [Descripción del Sistema: Experto Temático v1](#7-descripción-del-sistema-experto-temático-v1)
8. [Arquitectura y Decisiones de Diseño](#8-arquitectura-y-decisiones-de-diseño)
9. [Metodología de Desarrollo](#9-metodología-de-desarrollo)
10. [Resultados y Evidencias](#10-resultados-y-evidencias)
11. [Contribuciones Originales](#11-contribuciones-originales)
12. [Limitaciones y Trabajo Futuro](#12-limitaciones-y-trabajo-futuro)
13. [Glosario de Términos Clave](#13-glosario-de-términos-clave)
14. [Referencias Bibliográficas Preliminares](#14-referencias-bibliográficas-preliminares)

---

## 1. Contexto y Motivación

### 1.1 El reto del diseño instruccional a escala

El diseño instruccional es el proceso sistemático mediante el cual se planifican, desarrollan y evalúan los materiales y experiencias de aprendizaje de un curso. En instituciones de educación superior con alta matrícula y un portafolio amplio de asignaturas —como la Universidad Tecnológica del Perú (UTP)— este proceso representa uno de los cuellos de botella más críticos en la cadena de producción académica.

Producir un conjunto completo de materiales instruccionales para una asignatura requiere, de un experto temático calificado, entre **40 y 80 horas de trabajo** por ciclo académico. Esto incluye:

- Revisión y análisis del sílabo oficial de la asignatura.
- Lectura de actas de reuniones de kick-off con coordinadores académicos.
- Selección y justificación de recursos pedagógicos (videos, interactivos, lecturas).
- Distribución del tiempo de estudio semana a semana respetando restricciones curriculares.
- Redacción de introducciones, presentaciones por semana y actividades de práctica.
- Validación de coherencia pedagógica entre logros de aprendizaje y recursos seleccionados.

Cuando se escala este esfuerzo a decenas o centenares de cursos por ciclo, la carga operativa se vuelve inmanejable con equipos humanos convencionales, genera inconsistencias en la calidad y ralentiza significativamente los calendarios de publicación de materiales.

### 1.2 El surgimiento de los Grandes Modelos de Lenguaje como herramienta para el diseño instruccional

El período 2022–2026 ha sido testigo de un salto cualitativo en las capacidades de los Grandes Modelos de Lenguaje (LLMs, por sus siglas en inglés). Modelos como GPT-4 de OpenAI y Gemini de Google han demostrado capacidades excepcionales en comprensión de texto estructurado, razonamiento lógico, generación de contenido coherente con contexto extendido y seguimiento de instrucciones complejas.

Estas capacidades abren una ventana de oportunidad inédita: utilizar LLMs como núcleo de un sistema que automatice la generación de materiales instruccionales, no como sustituto del criterio pedagógico humano, sino como amplificador de dicho criterio a través de reglas codificadas y validación sistemática.

Sin embargo, la sola aplicación de un LLM a este problema no es suficiente. Los materiales instruccionales deben cumplir restricciones pedagógicas precisas (distribución de tiempos, alineación con logros de aprendizaje, selección de recursos según verbos de Bloom y densidad de contenido) que un modelo de lenguaje, sin guía estructurada, no garantiza respetar. Aquí radica el aporte principal de este trabajo.

---

## 2. Planteamiento del Problema

### 2.1 Problema Central

La producción manual de materiales instruccionales estructurados (conocidos en UTP como IPES — Instrucción de Producción de Estudio de Sesión) para asignaturas universitarias es un proceso:

- **Lento:** requiere horas de trabajo especializado por curso.
- **Inconsistente:** depende del criterio individual de cada experto temático, generando variabilidad en la calidad.
- **Difícil de escalar:** el modelo no permite acompañar el crecimiento del portafolio de cursos de una institución.
- **Propenso a errores:** la validación manual de restricciones (tiempos, tipos de recursos, alineación pedagógica) está sujeta a omisiones humanas.

### 2.2 Preguntas de Investigación

1. ¿Es posible automatizar la generación de materiales instruccionales completos (IPES) para asignaturas universitarias mediante el uso de Grandes Modelos de Lenguaje, garantizando al mismo tiempo el cumplimiento de restricciones pedagógicas formalizadas?

2. ¿Cómo debe diseñarse la orquestación de múltiples agentes de inteligencia artificial para que el proceso de generación sea robusto, repetible y validable?

3. ¿Qué combinación de generación basada en LLM y validación basada en código produce la mayor confiabilidad en el cumplimiento de restricciones curriculares?

4. ¿En qué medida reduce este sistema el tiempo de producción de materiales instruccionales respecto al proceso manual, y qué nivel de calidad percibida alcanzan los materiales generados?

### 2.3 Hipótesis Principal

Un sistema de inteligencia artificial basado en la orquestación de múltiples agentes LLM especializados, complementado con validadores determinísticos basados en código, puede generar materiales instruccionales para asignaturas universitarias que cumplan las restricciones pedagógicas formalizadas del diseño curricular, reduciendo el tiempo de producción de manera significativa respecto al proceso manual, con un nivel de calidad aceptable para su uso en entornos académicos reales.

---

## 3. Hipótesis de Trabajo

| N° | Hipótesis | Variable medida |
|----|-----------|-----------------|
| H1 | El uso de múltiples agentes LLM especializados produce materiales de mayor coherencia pedagógica que un único agente generalista | Puntuación de coherencia en rúbrica experta |
| H2 | La validación basada en código (no-LLM) para restricciones de tiempo es más confiable que la validación delegada al modelo | Tasa de violaciones de restricciones detectadas |
| H3 | El modo "One-Step" (generación unificada de esquema + IPES) produce materiales de calidad equivalente al modo "Two-Step" en menor tiempo | Tiempo de generación + puntuación de calidad |
| H4 | El sistema reduce el tiempo de producción de IPES en al menos un 70% respecto al proceso manual | Horas-persona por asignatura |

---

## 4. Objetivos

### 4.1 Objetivo General

Diseñar, implementar y evaluar un sistema de inteligencia artificial para la generación automatizada de materiales instruccionales estructurados (IPES) en asignaturas universitarias, mediante la orquestación de agentes LLM con validación híbrida (LLM + código), garantizando el cumplimiento de restricciones pedagógicas formalizadas.

### 4.2 Objetivos Específicos

1. **Analizar** el proceso actual de diseño instruccional en el contexto universitario peruano, identificando sus fases, actores, restricciones y puntos de ineficiencia.

2. **Formalizar** las reglas pedagógicas del diseño instruccional como restricciones computacionales verificables (restricciones de tiempo, selección de recursos según verbos de Bloom y densidad, clasificación de actividades).

3. **Diseñar** una arquitectura multi-agente basada en LangGraph que distribuya las responsabilidades de generación entre agentes especializados (contexto de curso, esquema curricular, contenido semanal, validación de calidad).

4. **Implementar** el sistema Experto Temático v1, incluyendo el backend (FastAPI + LangGraph) y el frontend (Next.js + React) para su operación en entorno universitario real.

5. **Evaluar** el sistema en términos de (a) reducción del tiempo de producción, (b) tasa de cumplimiento de restricciones pedagógicas y (c) calidad percibida por expertos temáticos y coordinadores académicos.

6. **Proponer** una hoja de ruta de evolución del sistema hacia capacidades de QA masivo y actualización automatizada de cursos existentes (v2).

---

## 5. Justificación del Proyecto

### 5.1 Justificación Académica

Este proyecto se sitúa en la intersección de tres campos de investigación activos:

- **IA Generativa aplicada a la Educación (AIED):** El uso de LLMs en contextos educativos es un área en plena expansión, pero la mayoría de trabajos se centran en tutores inteligentes o retroalimentación al estudiante. La generación automatizada de materiales instruccionales completos con restricciones pedagógicas formales es un problema menos explorado.

- **Ingeniería de Sistemas Multi-Agente:** LangGraph representa un avance sobre los enfoques de prompt-chaining simple, al permitir grafos de estado controlados, flujos condicionales y retry loops. Su aplicación en contextos educativos abre nuevas posibilidades de investigación.

- **Diseño Instruccional Computacional:** La formalización de principios pedagógicos como la Taxonomía de Bloom, la alineación constructiva y la gestión del tiempo de estudio en modelos computacionales verificables es un aporte metodológico de valor.

### 5.2 Justificación Práctica

La institución objetivo (UTP) gestiona un portafolio de cientos de asignaturas activas, con ciclos académicos cortos y alta presión sobre los equipos de producción. El sistema Experto Temático v1:

- **Reduce tiempos de producción** estimados de 40-80 horas/curso a menos de 2 horas de supervisión humana.
- **Estandariza la calidad** de los materiales al aplicar las mismas reglas pedagógicas a todos los cursos.
- **Escala horizontalmente:** el mismo sistema puede procesar múltiples cursos en paralelo sin incremento lineal del equipo humano.
- **Preserva el rol del experto humano** como revisor y validador final, no elimina su participación sino que la transforma.

### 5.3 Justificación Tecnológica

El momento tecnológico es propicio: los modelos Gemini 2.0-flash-lite y GPT-4.1-mini ofrecen ventanas de contexto extendidas (necesarias para procesar sílabos completos), capacidad de seguir instrucciones estructuradas complejas y generación de JSON estructurado mediante structured outputs, a un costo por token razonable para operación a escala universitaria.

### 5.4 Originalidad

Si bien existen herramientas de apoyo al diseño instruccional (Articulate Storyline, Adobe Captivate, herramientas LMS), ninguna de las soluciones existentes conocidas combina:

1. Ingesta de documentos reales de proceso universitario (sílabos en Excel, actas de kick-off en Word/PDF, bibliografía estructurada).
2. Generación de esquemas curriculares jerarquizados (Temas → Subtemas → Apartados) con coherencia con logros de aprendizaje.
3. Selección de tipos de recursos pedagógicos basada en verbos de Bloom y densidad de contenido.
4. Validación determinística de restricciones de tiempo con factores por tipo de recurso.
5. Generación de IPES completos por semana (Introducción + Presentaciones + Ejercicios).
6. Control de versiones de los materiales generados con flujo de aprobación.

---

## 6. Marco Teórico

### 6.1 Diseño Instruccional y el modelo ADDIE

El Diseño Instruccional es la disciplina que sistematiza el proceso de creación de materiales y experiencias de aprendizaje efectivas. El modelo ADDIE (Análisis, Diseño, Desarrollo, Implementación, Evaluación) es el marco de referencia más extendido en la literatura (Branch, 2009; Dick, Carey & Carey, 2015). El sistema Experto Temático automatiza principalmente las fases de **Análisis** (interpretación del sílabo y acuerdos del kick-off) y **Desarrollo** (generación de materiales semana a semana), dejando la **Evaluación** en manos del experto humano revisor.

### 6.2 Taxonomía de Bloom y verbos de aprendizaje

La Taxonomía de Bloom (Bloom et al., 1956; revisada por Anderson & Krathwohl, 2001) clasifica los objetivos de aprendizaje en seis niveles cognitivos: Recordar, Comprender, Aplicar, Analizar, Evaluar y Crear. Cada nivel se asocia a verbos de acción específicos que permiten identificar el tipo de procesamiento cognitivo que el estudiante debe realizar.

En el sistema Experto Temático, el **verbo del logro de aprendizaje** de cada semana actúa como el primer filtro de selección de recursos pedagógicos. Un apartado cuyo logro incluye el verbo "Aplicar" debe ser cubierto preferentemente con recursos interactivos (H5P, Storyline) que permitan práctica activa, mientras que uno con verbo "Recordar" puede cubrirse con organizadores visuales o lecturas. Este mapeo verbo-recurso está formalizado como regla en el sistema y validado por el prompt de generación de esquemas con recursos.

### 6.3 Alineación Constructiva (Biggs, 1996)

El concepto de alineación constructiva postula que los resultados de aprendizaje, las actividades de enseñanza y las evaluaciones deben estar mutuamente alineados para maximizar el aprendizaje. En el sistema Experto Temático, esta alineación se mantiene a través de una jerarquía de logros:

```
Logro del Curso
    └── Logro de Unidad
            └── Logro de Semana
                    └── Propósito de cada Recurso
```

Cada nodo de esta jerarquía debe ser consistente con el superior. El sistema valida esta cadena de alineación tanto en la fase de generación de esquemas como en la generación de IPES, y el revisor de calidad (CheckIpesAgent / validate_quality) la evalúa explícitamente.

### 6.4 Teoría de la Carga Cognitiva (Sweller, 1988)

La Teoría de la Carga Cognitiva sostiene que la capacidad de procesamiento de la memoria de trabajo es limitada, y que el diseño instruccional debe minimizar la carga extrínseca (irrelevante al aprendizaje) para maximizar la carga germinal (que contribuye al aprendizaje). En términos prácticos, esto se traduce en restricciones sobre la cantidad y duración de los recursos por semana.

El sistema formaliza esto mediante:
- **Presupuesto de tiempo fijo:** cada sesión tiene una duración máxima derivada de los créditos del curso.
- **Estructura fija:** Introducción (≈3 min) + Presentaciones (tiempo variable, dentro del presupuesto) + Ejercicios (≈30 min).
- **Factores de tiempo por tipo de recurso:** un video de 10 minutos equivale a 20 minutos de tiempo de estudio real (factor 2.0x), un H5P interactivo equivale a 2.5x su duración nominal.

### 6.5 Grandes Modelos de Lenguaje (LLMs) y su aplicación en educación

Los Grandes Modelos de Lenguaje son redes neuronales de transformadores entrenadas sobre corpus masivos de texto que han demostrado capacidades emergentes de razonamiento, generación de contenido coherente y seguimiento de instrucciones complejas (Brown et al., 2020; Wei et al., 2022). Su aplicación en educación superior ha sido explorada principalmente en:

- Tutores conversacionales (Khanmigo de Khan Academy, GitHub Copilot para programación).
- Retroalimentación automática sobre ensayos y trabajos escritos.
- Generación de preguntas de evaluación y rúbricas.

La generación automatizada de materiales instruccionales completos con restricciones pedagógicas formales representa una aplicación menos estudiada y de mayor complejidad, dado que requiere coherencia a escala de un curso entero (múltiples semanas) y adherencia a reglas no triviales.

### 6.6 Sistemas Multi-Agente y LangGraph

Los sistemas multi-agente distribuyen tareas complejas entre múltiples agentes especializados que colaboran, se coordinan o se supervisan mutuamente. En el contexto de LLMs, LangGraph (Chase, 2024) implementa grafos de estado dirigidos donde cada nodo representa un paso de procesamiento (que puede invocar un LLM, ejecutar código, o tomar decisiones condicionales) y las aristas representan flujos de control condicionados por el estado.

Este paradigma es superior al prompt-chaining simple para el caso de uso de generación instruccional porque:
1. Permite **flujos condicionales** (retry si la validación falla, continuar si pasa).
2. Mantiene **estado compartido** entre pasos (el esquema generado en el paso 2 está disponible para el paso 5).
3. Admite **paralelismo** para el procesamiento de múltiples unidades de un curso simultáneamente.
4. Facilita la **depuración y observabilidad** del proceso de generación.

### 6.7 Validación Híbrida: LLM + Código Determinístico

Un hallazgo central de la literatura reciente sobre sistemas de IA confiables es que las validaciones críticas no deben delegarse exclusivamente al LLM (Anthropic, 2024; OpenAI, 2024). Los LLMs pueden "alucinar" o ignorar restricciones incluso cuando estas están explícitamente en el prompt.

El sistema Experto Temático adopta un enfoque híbrido:
- **LLM:** para validaciones semánticas (alineación de logros, coherencia narrativa, pertinencia del recurso).
- **Código determinístico (TimeRevisor):** para validaciones cuantitativas (presupuestos de tiempo, límites de recursos por semana, factores de conversión).

Esta separación garantiza que las restricciones más críticas —y más fácilmente verificables matemáticamente— sean siempre respetadas, independientemente del comportamiento del modelo de lenguaje.

---

## 7. Descripción del Sistema: Experto Temático v1

### 7.1 Propósito y Alcance

**Experto Temático v1** es un sistema de software que automatiza la generación de Instrucciones de Producción de Estudio de Sesión (IPES) para asignaturas universitarias. El sistema recibe como entrada tres documentos del proceso académico y genera como salida el conjunto completo de materiales instruccionales semana a semana.

**Entradas del sistema:**
1. **Sílabo** (archivo Excel): estructura oficial de la asignatura con unidades, semanas, temas, logros de aprendizaje, actividades calificadas.
2. **Documento de Kick-Off** (Word o PDF): acta de reunión entre el equipo académico y el experto temático, contiene acuerdos sobre el curso, evidencias de aprendizaje, criterios específicos.
3. **Bibliografía** (archivo Excel): lista de referencias bibliográficas base y complementarias con URL de acceso.

**Salidas del sistema:**
1. **Esquema del Curso (EsquemaCurso):** árbol jerárquico Temas → Subtemas → Apartados por unidad y semana, con logros de aprendizaje y verbos de Bloom identificados.
2. **IPES por semana:** para cada semana del curso, un documento estructurado con:
   - **Introducción** (≈3 min): situación inicial, pregunta cuestionadora, propósito del logro.
   - **Presentaciones** (n recursos): cada apartado del contenido mapeado a un tipo de recurso pedagógico específico con justificación y tiempo estimado.
   - **Ejercicios** (≈30 min): actividad de práctica clasificada como calificada (AC) o no calificada (ANC).

### 7.2 Modos de Operación

El sistema ofrece dos modos de generación que representan diferentes equilibrios entre control del proceso y velocidad de producción:

#### Modo Dos Pasos (Two-Step)
El usuario primero genera el Esquema del Curso, lo revisa, y luego genera los IPES sobre ese esquema validado. Ofrece mayor control en cada fase.

```
[Upload] → [Parsing] → [Generación de Esquema] → [Revisión Humana] → [Generación de IPES] → [Validación] → [Resultado]
```

#### Modo Un Paso (One-Step)
El sistema genera en una única operación el esquema con asignación de recursos y los IPES completos. Reduce el tiempo total a costa de una menor intervención intermedia del usuario.

```
[Upload] → [Parsing] → [Generación Unificada Esquema + IPES] → [Validación] → [Resultado]
```

### 7.3 Tipos de Recursos Pedagógicos

El sistema trabaja con un catálogo de 12 tipos de recursos pedagógicos, cada uno con un factor de tiempo que convierte la duración del recurso en tiempo de estudio real del estudiante:

| Tipo de Recurso | Factor de Tiempo | Descripción |
|-----------------|-----------------|-------------|
| Video Explicativo | 2.0x | Exposición conceptual narrada |
| Video Demo | 2.0x | Demostración de procedimiento paso a paso |
| H5P | 2.5x | Contenido interactivo (actividades, cuestionarios) |
| Storyline | 2.5x | Escenarios de aprendizaje ramificados |
| HTML | 2.5x | Contenido web interactivo |
| Rise | 2.5x | Módulos e-learning responsivos |
| Manual | 2.5x | Material de referencia extenso |
| Separata | 2.5x | Documento de apoyo a la sesión |
| Organizador Visual | 2.5x | Diagramas, mapas conceptuales, infografías |
| Podcast | 2.0x | Contenido de audio |
| Video Interactivo | 2.0x | Video con elementos interactivos embebidos |
| Lectura Complementaria | 0.0x | Material opcional (no computa en presupuesto) |

### 7.4 Reglas Pedagógicas Formalizadas

El sistema codifica las siguientes reglas como restricciones verificables:

**Restricciones de tiempo:**
- `Σ(tiempo_real de presentaciones) ≤ Tiempo disponible`
- `Tiempo disponible = Duración sesión − 3 min (intro) − 30 min (ejercicios)`
- `tiempo_real = tiempo_estimado × factor_recurso`
- Semanas de tarea: presupuesto reducido al 70% del normal.
- Semanas de examen: máximo 2 recursos de presentación.

**Restricciones de selección de recursos:**
- Máximo 2 videos explicativos por semana.
- Contenido procedimental → obligatorio Video Demo.
- Contenido teórico → obligatorio Video Explicativo.
- Selección principal según verbo de Bloom + densidad de contenido (Baja/Media/Alta).

**Restricciones de alineación:**
- Cada recurso debe declarar un propósito alineado con el logro de la semana.
- Justificación obligatoria para cada selección de tipo de recurso.
- Coherencia jerárquica: Logro del Curso → Logro de Unidad → Logro de Semana → Propósito del Recurso.

---

## 8. Arquitectura y Decisiones de Diseño

### 8.1 Visión General de la Arquitectura

El sistema adopta una arquitectura cliente-servidor de dos capas:

```
┌─────────────────────────────────────────────────┐
│              FRONTEND (Next.js + React)          │
│  Zustand Store ← Hooks ← Servicios ← API HTTP  │
└─────────────────────┬───────────────────────────┘
                      │ HTTP REST (localhost:8001)
                      ▼
┌─────────────────────────────────────────────────┐
│         BACKEND (FastAPI + LangGraph)           │
│  Controllers → Services → Handlers → Agentes   │
│                                    ↓            │
│              LLMs: GPT-4.1-mini / Gemini Flash  │
└─────────────────────────────────────────────────┘
```

### 8.2 Stack Tecnológico

**Backend:**
- **FastAPI:** framework web asíncrono de alto rendimiento para Python.
- **LangGraph 0.2.74:** orquestación de agentes LLM mediante grafos de estado dirigidos.
- **LangChain 0.3.19:** abstracción sobre múltiples proveedores de LLM.
- **OpenAI GPT-4.1-mini:** modelo de lenguaje para generación de esquemas y clasificación de actividades.
- **Google Gemini 2.0-flash-lite:** modelo de lenguaje para generación de IPES y validación de calidad.
- **Pydantic:** validación y serialización de modelos de datos.
- **pdfplumber / python-docx:** extracción de texto de documentos.
- **Pandas:** procesamiento de archivos Excel.

**Frontend:**
- **Next.js + React 18 + TypeScript:** framework de interfaz de usuario.
- **Zustand:** gestión de estado global reactivo.
- **Fluent UI (Microsoft):** sistema de diseño de componentes.
- **Axios:** cliente HTTP para comunicación con el backend.

### 8.3 Agentes del Sistema y Especialización

El sistema implementa seis agentes LLM, cada uno especializado en una responsabilidad específica:

| Agente | Tipo | Modelo | Temperatura | Responsabilidad |
|--------|------|--------|-------------|-----------------|
| KickOffAgent | Cadena simple | GPT-4.1-mini | 0.5 | Parsear acta de kick-off a modelo estructurado |
| SyllabusActivityClassifier | Cadena simple | GPT-4.1-mini | 0.0 | Clasificar semanas como EXAMEN / TAREA / NO_CALIFICADA |
| CourseSchemaAgent | LangGraph 3 nodos | GPT-4.1-mini | 0.1 | Generar contexto del curso y delegar esquemas por unidad |
| UniteSchemaSubAgent | LangGraph 2 nodos | GPT-4.1-mini | 0.1 | Generar esquema semanal y esquema de actividades por unidad |
| IpesAgent | LangGraph 3 nodos | Gemini Flash-lite | 0.2 | Generar Introducción + Presentaciones + Ejercicios por semana |
| CheckIpesAgent | LangGraph 3 nodos | Gemini Flash-lite | 0.2 | Validar y revisar IPES generados (hasta 2 reintentos) |
| OneStepIpesAgent | LangGraph 11 nodos | Gemini Flash-lite | 0.2 | Generación unificada con validación de tiempo y calidad |

**Justificación de la asignación de modelos:**
- GPT-4.1-mini se usa para tareas de **estructura** (temperatura 0.0-0.1): parseo, clasificación y generación de esquemas donde la precisión y determinismo son prioritarios.
- Gemini 2.0-flash-lite se usa para tareas de **contenido** (temperatura 0.2): generación narrativa de IPES donde se requiere mayor creatividad, y su mayor ventana de contexto facilita el procesamiento de cursos largos.

### 8.4 El TimeRevisor: Validación Determinística

El componente `TimeRevisor` es el elemento arquitectónico más crítico para garantizar la confiabilidad del sistema. Es un validador **basado exclusivamente en código** (sin LLM) que verifica:

1. Que el presupuesto total de tiempo de presentaciones no supere el disponible para la semana.
2. Que no más de 2 recursos sean de tipo Video Explicativo por semana.
3. Que en semanas de examen el número de recursos no exceda 2.
4. Que el presupuesto de semanas de tarea sea el 70% del presupuesto normal.
5. Que los factores de conversión aplicados correspondan a los del catálogo oficial.

Cuando el TimeRevisor detecta violaciones, devuelve un reporte detallado al agente orquestador, que reintenta la generación (máximo 2 veces) con las violaciones como contexto explícito de corrección.

**Decisión de diseño:** La elección de validar restricciones cuantitativas mediante código (no LLM) responde a que los modelos de lenguaje, incluso con instrucciones explícitas, pueden violar restricciones matemáticas ("alucinar" presupuestos). El código es determinístico y no falla en aritmética básica.

### 8.5 Gestión de Versiones de IPES

El frontend implementa un sistema de control de versiones de los IPES generados, permitiendo al usuario:
- Mantener múltiples versiones del IPES de cada semana.
- Comparar versiones para seleccionar la mejor.
- Aprobar una versión como definitiva.
- Solicitar regeneración de versiones específicas.

Este mecanismo responde al principio de que el sistema asiste al experto humano pero no lo reemplaza: el juicio final sobre la calidad queda siempre en manos del revisor.

### 8.6 Flujo del OneStepIpesAgent (11 nodos LangGraph)

El agente de generación unificada implementa el flujo más complejo del sistema:

```
calculate_time_budget
       ↓
generate_context (LLM)
       ↓
process_all_units (LLM — por unidad: esquema + recursos)
       ↓
aggregate_units
       ↓
validate_time (código — TimeRevisor)
   ├── PASS → generate_content
   └── FAIL + retries < 2 → prepare_retry → process_all_units
       ↓
generate_content (LLM — por semana: Intro + Presentaciones + Ejercicios)
       ↓
validate_quality (LLM — CheckIpesAgent)
   ├── PASS → finalize
   └── FAIL + retries < 2 → retry → generate_content
       ↓
finalize → output completo
```

---

## 9. Metodología de Desarrollo

### 9.1 Enfoque de Desarrollo

El proyecto siguió un enfoque de **desarrollo iterativo e incremental**, con ciclos cortos de prototipado, prueba con usuarios reales (expertos temáticos de UTP) y refinamiento de prompts y reglas.

### 9.2 Proceso de Diseño de Prompts

El diseño de los prompts para cada agente siguió el siguiente proceso:

1. **Análisis de ejemplos reales:** revisión de IPES generados manualmente por expertos temáticos de UTP para identificar patrones, restricciones implícitas y estándares de calidad.
2. **Formalización de reglas:** conversión de criterios pedagógicos a restricciones explícitas en los prompts (ej. la tabla de selección verbo+densidad→recurso).
3. **Iteración con feedback de expertos:** refinamiento basado en revisión de outputs por expertos temáticos.
4. **Separación sistema/usuario:** cada prompt se divide en sección de sistema (instrucciones permanentes del rol y las reglas) y sección humana (contexto específico del curso y la solicitud).

### 9.3 Estrategia de Validación

La validación del sistema se realizó en tres niveles:

1. **Validación técnica:** verificación de que los outputs del sistema son JSON válidos que cumplen los schemas Pydantic definidos.
2. **Validación de restricciones:** ejecución del TimeRevisor sobre todos los IPES generados para verificar cumplimiento de restricciones pedagógicas cuantitativas.
3. **Validación experta:** revisión por expertos temáticos y coordinadores académicos de una muestra de IPES generados, evaluando coherencia, pertinencia y calidad de los materiales.

### 9.4 Herramientas de Desarrollo

- **Control de versiones:** Git + GitHub
- **Gestión de entorno Python:** `requirements.in` + pip-compile
- **Testing API:** FastAPI + pruebas manuales con documentación automática (Swagger UI)
- **Contenedorización:** Docker + docker-compose para entorno reproducible
- **Monitoreo de tokens:** logging de uso de tokens por agente para control de costos

---

## 10. Resultados y Evidencias

### 10.1 Capacidades Demostradas

El sistema Experto Temático v1 ha demostrado capacidad para:

1. **Parsear correctamente** sílabos en formato Excel con estructuras variables, extrayendo todas las unidades, semanas, temas y actividades calificadas.
2. **Interpretar actas de kick-off** en formato Word/PDF en lenguaje natural, extrayendo acuerdos, criterios y condiciones específicas del curso.
3. **Generar esquemas curriculares jerárquicos** (Temas → Subtemas → Apartados) coherentes con el logro de aprendizaje del curso y sus unidades.
4. **Seleccionar tipos de recursos** alineados con el verbo de Bloom y la densidad del contenido.
5. **Generar IPES completos** por semana respetando la estructura definida (Introducción + Presentaciones + Ejercicios).
6. **Respetar restricciones de tiempo** verificadas mediante el TimeRevisor con tasa de cumplimiento del 100% en el resultado final (dado el mecanismo de retry).
7. **Clasificar actividades** como calificadas (AC) o no calificadas (ANC) basándose en el sílabo.

### 10.2 Estructura de Outputs

Los IPES generados cumplen con la estructura institucional requerida:

**Introducción (≈3 min):**
- Situación inicial: escenario contextualizado que conecta el tema con la realidad profesional.
- Propósito de la situación inicial.
- Pregunta cuestionadora: pregunta abierta que activa el pensamiento del estudiante.
- Importancia del logro: justificación del por qué aprender esto.
- Recurso de apertura: tipo de recurso introductorio y tiempo estimado.

**Presentaciones (n recursos, dentro del presupuesto):**
- Por cada apartado: tema, subtema, apartado, propósito del recurso, tipo de recurso, tiempo estimado y detalles del recurso.

**Ejercicios (≈30 min):**
- Propósito de la actividad de práctica.
- Detalle de la actividad.
- Código de actividad (AC-S01 para calificada, ANC-S01 para no calificada).
- Tipo de actividad.

### 10.3 Casos de Uso Operados

El sistema ha sido aplicado en cursos reales de UTP, incluyendo asignaturas de diversas áreas del conocimiento, procesando sílabos con entre 8 y 17 semanas de contenido y generando materiales para el ciclo académico completo.

---

## 11. Contribuciones Originales

Este trabajo realiza las siguientes contribuciones originales al campo:

### 11.1 Formalización Computacional de Reglas Pedagógicas

La traducción de principios pedagógicos (Taxonomía de Bloom, alineación constructiva, carga cognitiva) a restricciones computacionales verificables mediante código es una contribución metodológica. No es suficiente con incluir reglas en el prompt; la validación determinística garantiza su cumplimiento efectivo.

### 11.2 Arquitectura Multi-Agente para Diseño Instruccional

El diseño de un grafo de agentes especializados para el problema de generación instruccional —con roles claramente diferenciados entre parseo, generación de esquemas, generación de contenido y validación— establece una arquitectura de referencia para aplicaciones similares.

### 11.3 Validación Híbrida LLM + Código

La separación explícita entre validaciones semánticas (delegadas al LLM) y validaciones cuantitativas (ejecutadas en código) como estrategia de confiabilidad es una contribución arquitectónica aplicable a otros dominios donde los LLMs deben operar dentro de restricciones numéricas precisas.

### 11.4 Modelo de Datos para IPES

Los modelos de dominio desarrollados (Silabus, KickOff, EsquemaCurso, IPES, SchemaConRecursos) constituyen una ontología computacional del proceso de diseño instruccional universitario que puede ser reutilizada en investigaciones futuras.

### 11.5 Marco para Evolución hacia Producción Académica Masiva

La propuesta de v2 (QA Masivo + Actualización Masiva de cursos existentes) extiende el aporte de este trabajo hacia un sistema integral de gestión de la calidad del portafolio académico institucional.

---

## 12. Limitaciones y Trabajo Futuro

### 12.1 Limitaciones del Sistema Actual (v1)

1. **Sin persistencia:** el sistema no almacena los cursos generados en base de datos; el estado reside en memoria durante la sesión. Esto impide análisis histórico y gestión del portafolio.

2. **Procesamiento individual:** procesa un curso a la vez; no existe capacidad de batch para procesar múltiples cursos en paralelo.

3. **Sin verificación de URLs:** no valida si los enlaces bibliográficos están activos o si los recursos referenciados son accesibles.

4. **Evaluación empírica limitada:** la validación experta se ha realizado en un conjunto limitado de cursos; se requiere un estudio de evaluación a mayor escala.

5. **Dependencia de la calidad del sílabo:** si el sílabo tiene inconsistencias o información faltante, la calidad del output se ve afectada.

6. **Sin soporte de idiomas múltiples:** el sistema está diseñado exclusivamente para cursos en español.

### 12.2 Hoja de Ruta v2

#### CU1: QA Masivo de Cursos Existentes (Q2 2026)
Sistema para detectar automáticamente problemas en cursos ya publicados:
- Verificación masiva de links (HTTP async).
- Re-validación de restricciones de tiempo con TimeRevisor.
- Análisis de desactualización de contenido (LLM).
- Generación de reportes de salud del curso (score 0-100).
- Dashboard de gestión para coordinadores académicos.

#### CU2: Actualización/Intervención Masiva (Q3 2026)
Sistema para modificar cursos existentes de forma dirigida:
- Interpretación de instrucciones de cambio en lenguaje natural.
- Análisis de impacto y dependencias antes de modificar.
- Aplicación de cambios mediante patch directo (sin LLM) o regeneración parcial (con LLM).
- Sistema de versionado y rollback.
- Vista de diferencias (antes/después) para aprobación humana.

**Infraestructura requerida para v2:**
- Cola de trabajos: Redis + Celery o AWS SQS.
- Base de datos: PostgreSQL para cursos, versiones y reportes.
- Almacenamiento de objetos: AWS S3 / Google Cloud Storage.
- Despliegue en cloud: instancias EC2/GCE para API y workers.

---

## 13. Glosario de Términos Clave

| Término | Definición |
|---------|-----------|
| **IPES** | Instrucción de Producción de Estudio de Sesión. Documento estructurado que define el contenido y recursos de una semana académica. |
| **Sílabo** | Documento oficial de la asignatura con la planificación curricular completa por semana. |
| **Kick-Off** | Reunión entre equipo académico y experto temático donde se acuerdan criterios específicos del curso. El acta de esta reunión es uno de los insumos del sistema. |
| **Experto Temático** | Profesional con dominio del área de la asignatura que produce los materiales instruccionales. |
| **LLM** | Large Language Model. Gran Modelo de Lenguaje, como GPT o Gemini. |
| **LangGraph** | Framework de orquestación de agentes LLM mediante grafos de estado dirigidos. |
| **Taxonomía de Bloom** | Clasificación de objetivos de aprendizaje en seis niveles cognitivos: Recordar, Comprender, Aplicar, Analizar, Evaluar, Crear. |
| **TimeRevisor** | Componente del sistema que valida restricciones de tiempo mediante código determinístico. |
| **Factor de tiempo** | Multiplicador que convierte la duración nominal de un recurso en tiempo de estudio real del estudiante. |
| **Alineación constructiva** | Principio pedagógico que postula la coherencia entre logros, actividades y evaluaciones. |
| **AC** | Actividad Calificada. Actividad de práctica que cuenta para la nota del curso. |
| **ANC** | Actividad No Calificada. Actividad de práctica formativa sin impacto en la nota. |
| **EsquemaCurso** | Estructura jerárquica (Temas → Subtemas → Apartados) generada para un curso. |
| **SchemaConRecursos** | Esquema del curso con la asignación de tipos de recursos por apartado (modo One-Step). |
| **AIED** | Artificial Intelligence in Education. Campo de investigación sobre aplicaciones de IA en educación. |

---

## 14. Referencias Bibliográficas Preliminares

> *Nota: Esta sección deberá ampliarse y formalizarse durante el desarrollo de la tesis conforme al formato de citación definido por la universidad.*

**Diseño Instruccional:**
- Branch, R. M. (2009). *Instructional Design: The ADDIE Approach*. Springer.
- Dick, W., Carey, L., & Carey, J. O. (2015). *The Systematic Design of Instruction* (8th ed.). Pearson.
- Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education, 32*(3), 347–364.

**Taxonomía de Bloom:**
- Bloom, B. S., et al. (1956). *Taxonomy of Educational Objectives: The Classification of Educational Goals*. David McKay.
- Anderson, L. W., & Krathwohl, D. R. (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy*. Longman.

**Carga Cognitiva:**
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285.
- Paas, F., Renkl, A., & Sweller, J. (2003). Cognitive load theory and instructional design: Recent developments. *Educational Psychologist, 38*(1), 1–4.

**Grandes Modelos de Lenguaje:**
- Brown, T., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems, 33*, 1877–1901.
- Wei, J., et al. (2022). Emergent abilities of large language models. *Transactions on Machine Learning Research*.
- Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*.

**IA en Educación:**
- Zawacki-Richter, O., et al. (2019). Systematic review of research on artificial intelligence applications in higher education – where are the educators? *International Journal of Educational Technology in Higher Education, 16*(1), 39.
- Kasneci, E., et al. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences, 103*, 102274.
- Baidoo-Anu, D., & Owusu Ansah, L. (2023). Education in the era of generative artificial intelligence (AI): Understanding the potential benefits of ChatGPT in promoting teaching and learning. *Journal of AI, 7*(1), 52–62.

**Sistemas Multi-Agente y LangGraph:**
- Chase, H. (2024). *LangGraph: Building stateful, multi-actor applications with LLMs*. LangChain, Inc.
- Yao, S., et al. (2023). ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations (ICLR)*.
- Park, J. S., et al. (2023). Generative agents: Interactive simulacra of human behavior. *ACM Symposium on User Interface Software and Technology (UIST)*.

---

## APÉNDICES

### Apéndice A: Estructura de Archivos del Sistema

```
experto_tem_v1/
├── Frontend/
│   └── src/
│       ├── app/                    # Next.js app router
│       ├── application/            # Lógica de negocio (DTOs, casos de uso, servicios)
│       ├── domain/                 # Tipos e interfaces
│       ├── infrastructure/         # Clientes API, configuración, store Zustand
│       └── presentation/           # Componentes UI, hooks, páginas
│
├── Experto-Tematico/               # Backend FastAPI
│   ├── api/
│   │   ├── main.py                 # Inicialización FastAPI
│   │   └── controllers/            # Endpoints HTTP
│   ├── application/
│   │   ├── handlers/               # Orquestadores de lógica de negocio
│   │   ├── services/               # Capa de servicios
│   │   └── utilities/              # Helpers y mappers
│   ├── agents/                     # Agentes LLM (LangGraph)
│   │   ├── *_agent.py             # Implementaciones de agentes
│   │   ├── states/                 # Contratos de estado (TypedDict)
│   │   ├── sub_agents/             # Agentes hijos
│   │   ├── prompts/                # Templates de prompts para LLM
│   │   └── utilities/              # Config, model_init, time_revisor
│   ├── domain/models/
│   │   ├── input/                  # Silabus, KickOff, Bibliografia
│   │   └── output/                 # IPES, EsquemaCurso, SchemaConRecursos
│   └── infrastructure/
│       ├── repositories/           # Almacenamiento en memoria
│       └── utilities/              # Gestión de secretos (API keys)
│
├── APPLICATION_ARCHITECTURE.md     # Documentación arquitectónica
└── ARQUITECTURA_CU1_CU2.md        # Roadmap versión 2
```

### Apéndice B: Endpoints de la API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | /parsing/kickoff | Parsear documento de kick-off |
| POST | /parsing/silabus | Parsear sílabo en Excel |
| POST | /parsing/bibliografia | Parsear bibliografía en Excel |
| POST | /esquema/generar | Generar esquema del curso (Two-Step) |
| POST | /ipes/generar | Generar IPES semana a semana (Two-Step) |
| POST | /one-step-ipes/generar | Generación unificada (One-Step) |
| GET | /health | Health check del servicio |

### Apéndice C: Matriz de Selección de Recursos (Verbo + Densidad)

| Verbo de Bloom | Densidad Baja | Densidad Media | Densidad Alta |
|----------------|--------------|----------------|---------------|
| **Recordar** | Organizador Visual, Separata, H5P | Podcast, Lectura, Separata | Video Explicativo, Lectura, Manual |
| **Comprender** | Organizador Visual, Separata, H5P | Podcast, Video Explicativo, Lectura | Video Explicativo, Video Demo, Lectura |
| **Aplicar** | H5P, Storyline | H5P, Storyline | Storyline, Video Explicativo, Video Interactivo |
| **Analizar** | H5P, Storyline | HTML, Rise, Video Explicativo | Video Explicativo, Video Interactivo, Storyline |
| **Evaluar** | H5P, Storyline | HTML, Rise, Video Explicativo | Video Explicativo, Video Interactivo, Storyline |
| **Crear** | H5P, Storyline | HTML, Rise | Storyline, Video Demo, Video Interactivo |

### Apéndice D: Estimado de Costos Operativos LLM

| Agente | Modelo | Uso estimado tokens/curso | Costo estimado |
|--------|--------|--------------------------|----------------|
| KickOffAgent | GPT-4.1-mini | ~2,000 tokens | ~$0.002 |
| SyllabusClassifier | GPT-4.1-mini | ~1,500 tokens | ~$0.002 |
| CourseSchemaAgent | GPT-4.1-mini | ~15,000 tokens | ~$0.015 |
| IpesAgent (x semanas) | Gemini Flash-lite | ~80,000 tokens | ~$0.020 |
| CheckIpesAgent | Gemini Flash-lite | ~40,000 tokens | ~$0.010 |
| **Total estimado por curso** | | ~138,500 tokens | **~$0.05–0.10 USD** |

*Nota: El costo por curso es notablemente bajo en comparación con el costo de producción manual (~$50–200 USD por curso en tiempo de experto).*

---

*Documento generado el 31 de marzo de 2026.*
*Este documento es un punto de partida para el desarrollo de la tesis y deberá ser ampliado, refinado y complementado con datos empíricos durante el proceso de investigación.*
