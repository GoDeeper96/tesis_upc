# STATUS — Tesis UPC: Experto Temático

> Documento de referencia permanente. Actualizar con cada cambio relevante.

---

## Información General

| Campo | Valor |
|-------|-------|
| **Título tentativo** | Sistema de Generación Automatizada de Materiales Instruccionales mediante Inteligencia Artificial |
| **Institución** | Universidad Peruana de Ciencias Aplicadas (UPC) |
| **Tema principal** | Experto Temático — IA aplicada al Diseño Instruccional |
| **Profesor** | Daniel Burga — daniel.burga@upc.pe |
| **Repositorio** | https://github.com/GoDeeper96/tesis_upc.git |
| **Código fuente de referencia** | `D:\Proyectos actuales\UTP_Experto_Tematico\experto_tem_v1` |

---

## Estado Actual del Proyecto

| Fase | Estado | Notas |
|------|--------|-------|
| Definición del tema | ✅ Completado | Experto Temático confirmado como tema |
| Documento inicial (`initial.md`) | ✅ Completado | Base argumental, marco teórico, arquitectura |
| Resumen ejecutivo | ✅ Completado | `resumen_experto_tematico.md` |
| Registro de sesiones | ✅ Iniciado | `sesiones.md` — pendiente de llenar |
| Marco teórico | ⏳ En progreso | Preliminar en `initial.md` |
| Desarrollo formal de tesis | ⏳ Pendiente | |
| Evaluación del sistema | ⏳ Pendiente | |

---

## Archivos Clave del Repo

| Archivo | Descripción |
|---------|-------------|
| `initial.md` | Documento base: problema, hipótesis, marco teórico, arquitectura, contribuciones |
| `resumen_experto_tematico.md` | Resumen ejecutivo del sistema |
| `sesiones.md` | Historial de sesiones de clase |
| `status.md` | Este archivo |
| `cronograma.png` | Cronograma del curso |

---

## Sistema: Experto Temático v1

### Entradas
1. **Sílabo** `.xlsx` — estructura del curso (unidades, semanas, temas, logros)
2. **Kick-Off** `.docx / .pdf` — acta de reunión con acuerdos del curso
3. **Bibliografía** `.xlsx` — referencias base y complementarias

### Salidas
- **EsquemaCurso:** Temas → Subtemas → Apartados con logros de aprendizaje
- **IPES por semana:** Introducción + Presentaciones (recursos) + Ejercicios

### Stack Tecnológico
| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js + React 18 + TypeScript + Zustand + Fluent UI |
| Backend | FastAPI + LangGraph + Python |
| Modelo estructural | GPT-4.1-mini (esquemas, parseo, clasificación) |
| Modelo de contenido | Gemini 2.0-flash-lite (IPES, validación de calidad) |
| Validación crítica | TimeRevisor (código puro — sin LLM) |

### Agentes del Sistema
| Agente | Rol |
|--------|-----|
| KickOffAgent | Parsea el acta de kick-off a modelo estructurado |
| SyllabusActivityClassifier | Clasifica semanas: EXAMEN / TAREA / NO_CALIFICADA |
| CourseSchemaAgent | Genera contexto del curso y delega esquemas por unidad |
| UniteSchemaSubAgent | Genera esquema semanal y actividades por unidad |
| IpesAgent | Genera Introducción + Presentaciones + Ejercicios por semana |
| CheckIpesAgent | Valida y revisa IPES generados (hasta 2 reintentos) |
| OneStepIpesAgent | Generación unificada (11 nodos LangGraph) |

---

## Marco Teórico — Pilares Principales

- **Taxonomía de Bloom** — verbos de aprendizaje → selección de tipo de recurso
- **Alineación Constructiva** (Biggs, 1996) — coherencia logros ↔ recursos ↔ evaluaciones
- **Teoría de la Carga Cognitiva** (Sweller, 1988) — restricciones de tiempo y cantidad de recursos
- **Modelo ADDIE** — marco de referencia del Diseño Instruccional
- **LLMs en Educación (AIED)** — justificación tecnológica
- **Sistemas Multi-Agente / LangGraph** — arquitectura de solución

---

## Pendientes Importantes

- [ ] Completar primera sesión en `sesiones.md`
- [ ] Definir estructura formal del documento de tesis
- [ ] Establecer métricas de evaluación del sistema
- [ ] Recopilar datos de validación experta (cuántos cursos procesados, tiempo vs. manual)
- [ ] Revisar y ampliar referencias bibliográficas

---

## Notas y Decisiones Clave

- El código fuente real vive en `UTP_Experto_Tematico/experto_tem_v1` — **no modificar**, solo referencia.
- El repo `tesis_upc` es exclusivo para documentación de tesis.
- La validación de restricciones de tiempo es **siempre código, nunca LLM** — decisión arquitectónica central.
- Hay dos modos: **Two-Step** (con revisión intermedia) y **One-Step** (generación unificada).
- La versión 2 del sistema (CU1: QA Masivo, CU2: Actualización Masiva) está documentada en `initial.md` como trabajo futuro.
