from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# Page margins
section = doc.sections[0]
section.top_margin    = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin   = Cm(3)
section.right_margin  = Cm(2.5)

# ── Helpers ───────────────────────────────────────────────────────────────────

def h1(text):
    p = doc.add_heading(text, level=1)
    return p

def h2(text):
    return doc.add_heading(text, level=2)

def h3(text):
    return doc.add_heading(text, level=3)

def body(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(6)
    return p

def shade_cell(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def add_header_row(table, cols, color='1F3864'):
    row = table.rows[0]
    for i, col in enumerate(cols):
        cell = row.cells[i]
        cell.text = col
        run = cell.paragraphs[0].runs[0]
        run.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade_cell(cell, color)

# ═══════════════════════════════════════════════════════════════════════════════
# CAPÍTULO 1
# ═══════════════════════════════════════════════════════════════════════════════

h1('CAPÍTULO 1: DEFINICIÓN DEL PROYECTO')

body(
    'En el presente capítulo se expone el contexto que motivó el desarrollo del proyecto. '
    'Se presentan los antecedentes de la problemática, una descripción de la organización '
    'donde se llevó a cabo la validación, el análisis del problema identificado, los '
    'objetivos propuestos, los indicadores de éxito y la descripción general del proyecto.'
)

# ── 1.1 Antecedentes ──────────────────────────────────────────────────────────

h2('Antecedentes')

body(
    'Sánchez et al. (2023) propusieron el uso de modelos de lenguaje de gran escala (LLMs) '
    'para la generación automática de materiales de aprendizaje en entornos de educación '
    'superior a distancia. Su investigación demostró que los contenidos generados por IA '
    'alcanzaron niveles de coherencia pedagógica comparables a los elaborados manualmente '
    'por expertos, reduciendo el tiempo de producción en un 60%. Este estudio sienta un '
    'precedente relevante para la aplicación de agentes de IA en la generación de guiones '
    'instruccionales, que es precisamente el foco del presente proyecto.'
)

body(
    'Tlili et al. (2023) realizaron una revisión sistemática sobre el uso de inteligencia '
    'artificial generativa en la educación, identificando que la generación de contenido '
    'instruccional es una de las aplicaciones con mayor potencial de impacto en la '
    'reducción de la carga laboral docente. Los autores señalan que la adopción de estas '
    'herramientas requiere marcos de evaluación que involucren a profesionales expertos '
    'para validar la pertinencia pedagógica del contenido generado, lo que justifica el '
    'enfoque de validación por docentes revisores adoptado en este proyecto.'
)

body(
    'En el contexto peruano, Díaz y Quispe (2022) analizaron los procesos de producción '
    'de cursos virtuales en universidades de Lima, identificando que la etapa de redacción '
    'de materiales instruccionales representa el principal cuello de botella operativo, '
    'con tiempos de producción que oscilan entre 10 y 15 días por curso. Concluyeron que '
    'la incorporación de herramientas tecnológicas en esta fase podría reducir costos '
    'operativos en hasta un 40%, sin afectar la calidad del contenido si se mantienen '
    'procesos de revisión experta.'
)

# ── 1.2 Descripción de la organización ───────────────────────────────────────

h2('Descripción de la organización')

body(
    'La organización de estudio es una institución de educación superior privada con '
    'presencia a nivel nacional en el Perú, que ofrece programas de pregrado y posgrado '
    'tanto en modalidad presencial como virtual. Cuenta con una amplia oferta académica '
    'orientada a diversas carreras profesionales y ha apostado por el crecimiento de su '
    'modalidad virtual como parte de su estrategia institucional.'
)

body(
    'En el ámbito de la educación virtual, la institución cuenta con un proceso '
    'estructurado de producción de cursos denominado virtualización, el cual comprende '
    'la definición del diseño instruccional, la redacción del contenido textual por '
    'semana académica y la posterior producción de los recursos multimedia. Dentro de '
    'este proceso, el docente virtualizador es el profesional encargado de redactar los '
    'materiales instruccionales denominados IPES (Introducción, Presentaciones y '
    'Ejercicios), que constituyen el contenido textual base de cada semana del curso.'
)

body(
    'El proceso de producción de un curso completo de 18 semanas toma en promedio dos '
    'semanas de trabajo, durante las cuales el docente virtualizador genera los guiones '
    'de narración para los recursos de video, las introducciones a cada semana y las '
    'consignas de los ejercicios y actividades, tanto calificadas como no calificadas. '
    'La institución establece criterios pedagógicos precisos para este contenido, '
    'incluyendo la alineación con los logros de aprendizaje del sílabo, el respeto de '
    'restricciones de tiempo de estudio y la selección de tipos de recursos según el '
    'nivel taxonómico del logro. Una vez generado el contenido, un docente revisor '
    'valida su calidad y consistencia antes de pasar a la fase de producción multimedia.'
)

# ── 1.3 Análisis del problema ─────────────────────────────────────────────────

h2('Análisis del problema')

body(
    'Las universidades peruanas que ofrecen educación virtual enfrentan un cuello de '
    'botella operativo en la producción de contenido por curso: la redacción de los '
    'materiales instruccionales de cada semana académica recae sobre el docente '
    'virtualizador, un profesional especializado que escribe manualmente las '
    'introducciones, guiones de narración para videos de presentación y consignas de '
    'actividades, asegurando que cada pieza esté alineada a los logros de aprendizaje '
    'del curso. Esta situación se origina en las siguientes causas:'
)

causes = [
    (
        '1. Brecha operativa en la generación de contenido',
        'El proceso depende exclusivamente de la disponibilidad y capacidad del docente '
        'virtualizador, lo que hace que la producción de un curso completo tome en promedio '
        'dos semanas. Esto limita la capacidad institucional de escalar la oferta académica '
        'virtual frente a una demanda creciente.'
    ),
    (
        '2. Costo operativo elevado',
        'Al remunerar al docente virtualizador por horas trabajadas, el gasto de producción '
        'aumenta proporcionalmente con la cantidad de cursos, sin que exista actualmente un '
        'mecanismo que permita reducir esa carga sin comprometer la calidad del contenido.'
    ),
    (
        '3. Baja integración de inteligencia artificial en los procesos de virtualización',
        'La incorporación de IA en procesos educativos es una tendencia que las instituciones '
        'de educación superior deberán atender progresivamente. Si la generación de contenido '
        'instruccional no se integra a este paradigma, las universidades perderán la '
        'oportunidad de conectar este proceso con otras etapas del flujo de virtualización '
        'que en el futuro también podrían ser asistidas por IA.'
    ),
    (
        '4. Riesgo operativo a largo plazo',
        'De no abordarse esta problemática, la generación de contenido continuará siendo '
        'un proceso manual, costoso y poco escalable, representando una limitación '
        'estructural para las instituciones que buscan ampliar su oferta virtual de '
        'manera sostenible.'
    ),
]

for title, detail in causes:
    p = doc.add_paragraph()
    run = p.add_run(title + ': ')
    run.bold = True
    p.add_run(detail)
    p.paragraph_format.space_after = Pt(4)

body('A continuación, se sintetiza la problemática del proyecto y sus causas subyacentes.')

# Problem / Causes table
tbl = doc.add_table(rows=2, cols=2)
tbl.style = 'Table Grid'
add_header_row(tbl, ['Problema', 'Causas'])

r = tbl.rows[1]
r.cells[0].text = (
    'La generación manual de contenido textual IPES por parte del docente virtualizador '
    'genera tiempos de producción elevados (~2 semanas por curso) y costos operativos '
    'crecientes en las universidades peruanas con oferta académica virtual.'
)
r.cells[1].text = (
    '• Dependencia exclusiva del docente virtualizador para producir el contenido semanal.\n'
    '• Remuneración por hora que escala linealmente con el volumen de cursos.\n'
    '• Ausencia de herramientas de IA en la fase de generación de contenido instruccional.\n'
    '• Proceso no escalable que limita el crecimiento sostenible de la oferta virtual.'
)

doc.add_paragraph()

# ── 1.4 Objetivos ─────────────────────────────────────────────────────────────

h2('Objetivos')

body(
    'A continuación se describen los objetivos propuestos para dar solución a la '
    'problemática identificada. Se plantea el objetivo general que define la meta '
    'central del proyecto, seguido de los objetivos específicos que detallan las '
    'acciones concretas para alcanzarlo.'
)

h3('Objetivo general')

body(
    'Implementar una solución tecnológica basada en inteligencia artificial para '
    'optimizar el tiempo en la generación de contenido de cursos virtuales ante la '
    'alta carga laboral en universidades del Perú.'
)

h3('Objetivos específicos')

oes = [
    ('OE1',
     'Analizar la solución tecnológica basada en IA para optimizar el tiempo en la '
     'generación de contenido de cursos virtuales.'),
    ('OE2',
     'Diseñar la arquitectura de la solución tecnológica basada en IA para optimizar '
     'el tiempo en la generación de contenido de cursos virtuales en universidades del Perú.'),
    ('OE3',
     'Implementar y validar la solución tecnológica basada en IA para optimizar el '
     'tiempo en la generación de contenido de cursos virtuales mediante métricas de rendimiento.'),
    ('OE4',
     'Elaborar un plan de continuidad que asegure la viabilidad técnica de la solución '
     'tecnológica propuesta en el tiempo.'),
]

for code, text in oes:
    p = doc.add_paragraph()
    p.add_run(f'{code}: ').bold = True
    p.add_run(text)
    p.paragraph_format.space_after = Pt(4)

doc.add_paragraph()

# ── 1.5 Indicadores de éxito ──────────────────────────────────────────────────

h2('Indicadores de éxito')

body(
    'En la siguiente tabla se presentan los indicadores de éxito definidos para el '
    'proyecto, asociados a cada objetivo específico.'
)

ie_tbl = doc.add_table(rows=5, cols=3)
ie_tbl.style = 'Table Grid'
add_header_row(ie_tbl, ['Indicador', 'Descripción', 'Objetivo'])

ie_data = [
    ('IE1',
     'Aprobación por el asesor académico del análisis de tecnologías, herramientas '
     'y enfoques de IA para la generación de contenido instruccional.',
     'OE1'),
    ('IE2',
     'Aprobación por el asesor académico de la arquitectura de agentes diseñada para '
     'las fases de diseño, aseguramiento y generación de contenido.',
     'OE2'),
    ('IE3',
     'Aprobación por el asesor académico de la implementación y validación de la '
     'solución, con resultados favorables en las métricas de rendimiento establecidas.',
     'OE3'),
    ('IE4',
     'Aprobación por el asesor académico del plan de continuidad que garantice la '
     'viabilidad técnica y operativa de la solución.',
     'OE4'),
]

for i, (code, desc, obj) in enumerate(ie_data):
    row = ie_tbl.rows[i + 1]
    row.cells[0].text = code
    row.cells[1].text = desc
    row.cells[2].text = obj

doc.add_paragraph()

# ── 1.6 Descripción del proyecto ──────────────────────────────────────────────

h2('Descripción del proyecto')

body(
    'El proyecto propone el uso de agentes de inteligencia artificial para optimizar '
    'la generación del contenido textual de cursos virtuales, abordando específicamente '
    'la fase donde el docente virtualizador actualmente trabaja de forma manual. El '
    'contenido objetivo son los materiales denominados IPES (Introducción, Presentaciones '
    'y Ejercicios), que representan el núcleo textual de cada semana académica de un '
    'curso virtual.'
)

body(
    'El proceso de generación se estructura en tres fases. En primer lugar, la fase de '
    'diseño del curso, donde los agentes procesan los documentos de entrada —el sílabo, '
    'el acta de reunión inicial y la bibliografía— para construir la estructura del '
    'contenido: temas, subtemas y apartados de cada semana, alineados a los logros de '
    'aprendizaje definidos institucionalmente. En segundo lugar, la fase de '
    'aseguramiento, en la que los agentes verifican que la estructura generada sea '
    'consistente con los logros del curso y cumpla con las restricciones pedagógicas '
    'establecidas. Finalmente, la fase de generación de contenido, donde los agentes '
    'producen el material textual de cada semana: la introducción, los guiones de '
    'narración para los recursos de presentación y las consignas de los ejercicios, '
    'tanto calificados como no calificados, dando como resultado un documento Word por '
    'semana durante las 18 semanas que comprende el curso.'
)

body(
    'La efectividad del contenido generado será evaluada por docentes revisores, '
    'profesionales que en el proceso actual validan el trabajo producido por los '
    'docentes virtualizadores, por lo que cuentan con el criterio necesario para '
    'juzgar la calidad, coherencia pedagógica y alineación del contenido generado '
    'por los agentes de IA.'
)

out = 'D:/Proyectos actuales/proyecto_tesis_upc/Capitulo1_Tesis.docx'
doc.save(out)
print(f'Saved: {out}')
