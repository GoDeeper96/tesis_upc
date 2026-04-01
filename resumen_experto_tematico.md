# Resumen Ejecutivo — Experto Temático

## ¿Qué es?

**Experto Temático** es un sistema de inteligencia artificial que automatiza la creación de materiales instruccionales (IPES) para asignaturas universitarias. En lugar de que un experto humano dedique 40–80 horas por curso, el sistema genera el contenido completo en minutos a partir de tres documentos de entrada.

## ¿Qué problema resuelve?

Las instituciones universitarias con grandes portafolios de cursos no pueden escalar la producción de materiales educativos de calidad con equipos humanos convencionales. El proceso manual es lento, costoso e inconsistente.

## ¿Cómo funciona?

1. El usuario sube tres archivos: **Sílabo** (Excel), **Kick-Off** (Word/PDF) y **Bibliografía** (Excel).
2. El sistema los parsea automáticamente y construye el contexto del curso.
3. Un conjunto de **agentes de IA especializados** (usando GPT-4.1-mini y Gemini 2.0-flash-lite) genera:
   - El **esquema curricular** del curso: Temas → Subtemas → Apartados por semana.
   - Los **IPES completos** semana a semana: Introducción + Presentaciones con recursos + Ejercicios.
4. Un validador determinístico (**TimeRevisor**) verifica que se cumplan todas las restricciones pedagógicas de tiempo y recursos.

## Restricciones pedagógicas que garantiza

- Cada recurso seleccionado se alinea con el **verbo de Bloom** y la **densidad de contenido** del tema.
- El tiempo total de presentaciones nunca supera el **presupuesto de la sesión**.
- Máximo 2 videos explicativos por semana.
- Reducción automática de carga en semanas de examen (máx. 2 recursos) y de tarea (70% del presupuesto).

## Tecnología

| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js + React + TypeScript + Zustand |
| Backend | FastAPI + LangGraph + Python |
| IA | GPT-4.1-mini (estructura) + Gemini 2.0-flash-lite (contenido) |
| Validación | TimeRevisor (código puro, sin LLM) |

## Resultado

Un conjunto completo de IPES listos para revisión humana, a un costo estimado de **$0.05–0.10 USD por curso** frente a **$50–200 USD** en tiempo de experto humano.
