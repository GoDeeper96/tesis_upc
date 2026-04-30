from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

section = doc.sections[0]
section.top_margin    = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin   = Cm(3)
section.right_margin  = Cm(2.5)

# ── Helpers ───────────────────────────────────────────────────────────────────

def h1(text):
    return doc.add_heading(text, level=1)

def h2(text):
    return doc.add_heading(text, level=2)

def h3(text):
    return doc.add_heading(text, level=3)

def body(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(6)
    return p

def bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    if bold_prefix:
        r = p.add_run(bold_prefix + ': ')
        r.bold = True
    p.add_run(text)
    p.paragraph_format.space_after = Pt(3)
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

def spacer():
    doc.add_paragraph()

# ═══════════════════════════════════════════════════════════════════════════════
# CAPITULO 2 - MARCO TEORICO
# ═══════════════════════════════════════════════════════════════════════════════

h1('CAPITULO 2: MARCO TEORICO')

body(
    'El presente capitulo expone los conceptos y fundamentos necesarios para comprender '
    'el problema abordado, la solucion disenada y los criterios con los que se evaluo. '
    'Se organiza en cuatro bloques: el contexto del proceso de produccion instruccional, '
    'los fundamentos pedagogicos que rigen las reglas del sistema, los fundamentos '
    'tecnicos sobre los que se construyo la solucion y la metodologia de desarrollo empleada.'
)

# ═══════════════════════════════════════════════════════════════════════════════
# 2.1  PROCESO DE PRODUCCION INSTRUCCIONAL
# ═══════════════════════════════════════════════════════════════════════════════

h2('2.1  El Proceso de Produccion Instruccional')

body(
    'En esta seccion se describen los elementos que componen el proceso de produccion '
    'de cursos virtuales en una institucion de educacion superior: los roles del equipo, '
    'los documentos de entrada que definen el curso, los artefactos que se producen y '
    'el catalogo de tipos de recursos educativos.'
)

# ── 2.1.1 Roles ───────────────────────────────────────────────────────────────

h3('2.1.1  Roles del equipo de produccion')

body(
    'Se explicara cada uno de los perfiles que intervienen en el proceso de '
    'virtualizacion de cursos, su responsabilidad especifica dentro del flujo de '
    'produccion y la relacion entre ellos. Los roles a desarrollar son:'
)

roles = [
    ('DDA (Direccion de Diseno Academico)',
     'Rol con vision macro del proceso de produccion. '
     'Puede intervenir y tomar decisiones sobre cualquier curso en cualquier momento. '
     'No necesariamente es experto en el contenido de cada asignatura.'),
    ('LxD (Learning Designer / Disenador Instruccional)',
     'Profesional que disena la estructura instruccional del curso. '
     'Conoce como debe estructurarse un curso pero no es el experto en la materia. '
     'Es quien genera el IPES.'),
    ('Docente Virtualizador / Experto Tematico',
     'Experto en el contenido de la asignatura y responsable de crear '
     'los materiales instruccionales. Es el rol que el sistema replica mediante IA.'),
    ('Docente Revisor',
     'Experto que revisa y valida los materiales generados -ya sea por humanos o por IA- '
     'antes de que pasen a produccion. Es el validador final de calidad.'),
    ('Area de Evaluacion',
     'Equipo especializado en la construccion de instrumentos de evaluacion (consignas, '
     'rubricas, listas de cotejo). Verifica que las actividades calificadas esten bien '
     'construidas pedagogicamente.'),
]

for title, desc in roles:
    bullet(desc, title)

spacer()

# ── 2.1.2 Inputs ──────────────────────────────────────────────────────────────

h3('2.1.2  Documentos de entrada: Silabus y Kickoff')

body(
    'Se describiran los dos documentos que el sistema recibe como entrada y que '
    'concentran toda la informacion necesaria para producir el contenido de un curso:'
)

inputs = [
    ('Silabus',
     'Documento oficial del curso (formato Excel) que contiene la estructura academica: '
     'unidades, semanas, temas, logros de aprendizaje y actividades calificadas. '
     'Es la fuente de verdad estructural del curso.'),
    ('Kickoff / Acta de Reunion de Inicio',
     'Documento que recoge los acuerdos tomados entre el equipo academico y el experto '
     'antes de iniciar la produccion. Incluye: perfil del estudiante, enfoque de diseno '
     '(teorico / practico / mixto), temas complejos, formula de evaluacion y criterios '
     'especificos del curso. Contiene informacion que el silabus no recoge y que '
     'condiciona decisiones de diseno.'),
]

for title, desc in inputs:
    bullet(desc, title)

spacer()

# ── 2.1.3 Outputs ─────────────────────────────────────────────────────────────

h3('2.1.3  Artefactos producidos: IPES, Material Base y Consignas')

body(
    'Se explicaran los tres artefactos principales que produce el proceso de '
    'virtualizacion, con enfasis en la relacion secuencial entre ellos:'
)

outputs = [
    ('IPES (Introduccion, Presentaciones y Ejercicios)',
     'Primer output del sistema. Documento de planificacion instruccional por semana '
     'que define: la situacion inicial y pregunta cuestionadora de la introduccion, '
     'los recursos de presentacion con su tipo, proposito y tiempo estimado, '
     'y el ejercicio de la semana (calificado o no calificado). '
     'El IPES no es el contenido final; es la hoja de ruta que indica que producir.'),
    ('Material Base / Base Content',
     'Ultimo output del proceso. Usando el IPES como entrada, se genera el contenido '
     'real que consumiran los estudiantes: guiones de narracion para videos, texto de '
     'separatas y manuales, pantallas para H5P y Storyline, instrucciones y resoluciones '
     'de ejercicios. Es el artefacto final de la cadena de produccion.'),
    ('Consignas',
     'Instrumentos de evaluacion formales: rubricas, listas de cotejo y escalas de '
     'valoracion. Definen como se evaluara el desempeno del estudiante en las '
     'actividades calificadas. Son revisados por el Area de Evaluacion.'),
]

for title, desc in outputs:
    bullet(desc, title)

spacer()

# ── 2.1.4 Catalogo de recursos ────────────────────────────────────────────────

h3('2.1.4  Catalogo de recursos educativos y factores de tiempo')

body(
    'Se presentara el conjunto de tipos de recursos educativos que el sistema maneja '
    'y el concepto de factor de tiempo, que convierte la duracion nominal de un recurso '
    'en el tiempo real de estudio que representa para el estudiante. '
    'Se senalara que la clasificacion de recursos es institucional: cada universidad '
    'puede definir su propio catalogo; el sistema utiliza el de la institucion donde '
    'se valido el proyecto.'
)

body('Los tipos de recursos del catalogo y sus factores son los siguientes:')

res_tbl = doc.add_table(rows=14, cols=3)
res_tbl.style = 'Table Grid'
add_header_row(res_tbl, ['Tipo de Recurso', 'Categoria', 'Factor de Tiempo'])

res_data = [
    ('H5P',                    'Contenido interactivo', '2.5x'),
    ('HTML',                   'Contenido interactivo', '2.5x'),
    ('Rise',                   'Contenido interactivo', '2.5x'),
    ('Storyline',              'Contenido interactivo', '2.5x'),
    ('Video Explicativo',      'Audiovisual',           '2.0x'),
    ('Video Demo',             'Audiovisual',           '2.0x'),
    ('Video Interactivo',      'Audiovisual',           '2.0x'),
    ('Podcast',                'Audiovisual',           '2.0x'),
    ('Separata',               'Lectura',               '2.5x'),
    ('Manual',                 'Lectura',               '2.5x'),
    ('Lectura',                'Lectura',               '2.5x'),
    ('Organizador Visual',     'Visual / grafico',      '2.5x'),
    ('Lectura Complementaria', 'Lectura opcional',      '0x (no computa)'),
]

for i, (tipo, cat, factor) in enumerate(res_data):
    row = res_tbl.rows[i + 1]
    row.cells[0].text = tipo
    row.cells[1].text = cat
    row.cells[2].text = factor

spacer()

body(
    'Se explicara que el factor de tiempo no es arbitrario: refleja el tiempo de '
    'procesamiento cognitivo adicional que requiere cada tipo de recurso respecto '
    'a su duracion nominal. Por ejemplo, un Video Explicativo de 10 minutos implica '
    '20 minutos de tiempo de estudio real (factor 2.0x), ya que el estudiante necesita '
    'procesar y asimilar el contenido, no solo reproducirlo.'
)

spacer()

# ═══════════════════════════════════════════════════════════════════════════════
# 2.2  FUNDAMENTOS PEDAGOGICOS
# ═══════════════════════════════════════════════════════════════════════════════

h2('2.2  Fundamentos Pedagogicos')

body(
    'En esta seccion se presentan los marcos teoricos del aprendizaje que sustentan '
    'las reglas pedagogicas codificadas en el sistema. Cada concepto se explica en '
    'relacion directa con las decisiones de diseno instruccional que el sistema automatiza.'
)

# ── 2.2.1 Taxonomia de Bloom ──────────────────────────────────────────────────

h3('2.2.1  Taxonomia de Bloom')

body(
    'Se explicara la Taxonomia de Bloom (revision de Anderson & Krathwohl, 2001) como '
    'el marco de clasificacion de objetivos de aprendizaje que el sistema utiliza para '
    'tomar decisiones sobre que tipo de recurso asignar a cada apartado del curso. '
    'Los puntos a cubrir son:'
)

bloom_points = [
    'Los seis niveles cognitivos y sus verbos asociados '
    '(Recordar, Comprender, Aplicar, Analizar, Evaluar, Crear).',
    'Como el verbo del logro de aprendizaje semanal determina el tipo de recurso '
    'a utilizar (tabla verbo x densidad -> tipo de recurso).',
    'La jerarquia de logros: Logro del Curso -> Logro de Unidad -> '
    'Logro de Semana -> Proposito del Recurso, y por que cada nivel '
    'debe ser consistente con el superior.',
    'La distincion entre contenido procedimental (requiere Video Demo), '
    'teorico (requiere Video Explicativo) y basico (flexible), '
    'y como el verbo del logro permite identificar cada tipo.',
]

for pt in bloom_points:
    bullet(pt)

spacer()

# ── 2.2.2 AHA Moment ─────────────────────────────────────────────────────────

h3('2.2.2  Conflicto cognitivo y la Situacion Inicial (AHA Moment)')

body(
    'Se explicara el concepto de conflicto cognitivo como mecanismo de activacion '
    'del aprendizaje, y como se operacionaliza en la seccion de Introduccion del IPES. '
    'Los puntos a cubrir son:'
)

aha_points = [
    'Que es el conflicto cognitivo: presentar al estudiante un problema o situacion '
    'que no puede resolver con su conocimiento actual, generando la motivacion '
    'intrinseca para aprender.',
    'La Situacion Inicial como el recurso instruccional que genera ese conflicto: '
    'caso, estadistica, reto o testimonio relacionado con el tema de la semana.',
    'La Pregunta Cuestionadora como cierre del conflicto cognitivo: '
    'la pregunta abierta que el estudiante no puede responder aun pero respondera '
    'al terminar los recursos de presentacion.',
    'Por que la introduccion siempre usa un recurso HTML y tiene duracion fija '
    '(72 segundos): es un elemento de apertura, no de contenido.',
]

for pt in aha_points:
    bullet(pt)

spacer()

# ═══════════════════════════════════════════════════════════════════════════════
# 2.3  FUNDAMENTOS TECNICOS
# ═══════════════════════════════════════════════════════════════════════════════

h2('2.3  Fundamentos Tecnicos')

body(
    'En esta seccion se presentan los conceptos de inteligencia artificial e ingenieria '
    'de software sobre los que se construyo el sistema. Se explica cada concepto en '
    'funcion de su rol dentro de la arquitectura de la solucion.'
)

# ── 2.3.1 Prompt Engineering ──────────────────────────────────────────────────

h3('2.3.1  Prompt Engineering')

body(
    'Se explicara que es el diseno de prompts y por que es la principal interfaz '
    'de programacion con los modelos de lenguaje. Los puntos a cubrir son:'
)

pe_points = [
    'Que es un prompt: la instruccion en lenguaje natural que guia el comportamiento '
    'de un modelo de lenguaje para una tarea especifica.',
    'La separacion entre system prompt (instrucciones permanentes de rol y reglas) '
    'y user prompt (contexto variable de cada ejecucion).',
    'El patron de hard rules vs. soft guidelines dentro de un prompt: '
    'reglas no negociables que el agente debe respetar siempre, '
    'versus lineamientos donde puede aplicar criterio propio.',
    'El proceso iterativo de refinamiento de prompts con validacion por expertos '
    'como parte del desarrollo del sistema.',
    'La diferencia entre prompt chaining simple (secuencia lineal de prompts) '
    'y la orquestacion estructurada mediante grafos de estado.',
]

for pt in pe_points:
    bullet(pt)

spacer()

# ── 2.3.2 Structured Outputs ──────────────────────────────────────────────────

h3('2.3.2  Structured Outputs (Salidas Estructuradas)')

body(
    'Se explicara por que los modelos de lenguaje deben producir datos estructurados '
    '(JSON) en lugar de texto libre para que la solucion funcione como pipeline. '
    'Los puntos a cubrir son:'
)

so_points = [
    'El problema del texto libre: un LLM que responde en lenguaje natural no puede '
    'integrarse directamente en un sistema de software; su output debe ser parseable.',
    'JSON mode / structured output como mecanismo de enforcement: '
    'el modelo es forzado a producir un JSON que cumple un esquema predefinido.',
    'Pydantic como contrato de datos: cada agente define su modelo de entrada y salida '
    'mediante clases Pydantic, garantizando que los tipos y campos sean correctos.',
    'La cadena de datos entre agentes: el output estructurado de un agente '
    '(por ejemplo, el IPES) se convierte en el input del siguiente '
    '(por ejemplo, el generador de Material Base).',
]

for pt in so_points:
    bullet(pt)

spacer()

# ── 2.3.3 Multi-Agent Systems ─────────────────────────────────────────────────

h3('2.3.3  Sistemas Multi-Agente')

body(
    'Se explicara el concepto de sistema multi-agente aplicado a modelos de lenguaje '
    'y por que es superior a un unico agente generalista para este problema. '
    'Los puntos a cubrir son:'
)

ma_points = [
    'Que es un agente de IA: una instancia de un modelo de lenguaje con un rol, '
    'instrucciones y responsabilidad especifica.',
    'Por que especializar: un agente con una sola responsabilidad bien definida '
    'produce resultados mas precisos y confiables que uno que intenta hacer todo.',
    'La distribucion de responsabilidades en el sistema: '
    'parseo de documentos, generacion de esquema curricular, '
    'generacion de contenido por semana, validacion de calidad.',
    'Coordinacion entre agentes: como el estado se comparte y acumula '
    'a medida que cada agente completa su tarea.',
]

for pt in ma_points:
    bullet(pt)

spacer()

# ── 2.3.4 Nodes ───────────────────────────────────────────────────────────────

h3('2.3.4  Nodos y Grafos de Estado')

body(
    'Se explicara el concepto de nodo dentro de un grafo de estado dirigido '
    'y como esta abstraccion permite controlar flujos complejos de generacion. '
    'Los puntos a cubrir son:'
)

nodes_points = [
    'Un nodo como unidad de procesamiento: puede invocar un LLM, ejecutar codigo '
    'o tomar una decision condicional.',
    'Estado compartido: el grafo mantiene un estado global que todos los nodos '
    'pueden leer y escribir; asi la informacion generada en pasos anteriores '
    'esta disponible para los siguientes.',
    'Aristas condicionales: el flujo entre nodos no es siempre lineal; '
    'puede bifurcarse segun el resultado de un nodo '
    '(ej.: validacion pasa -> continuar, validacion falla -> reintentar).',
    'El ciclo retry: cuando un nodo de validacion detecta un problema, '
    'el grafo regresa al nodo de generacion con el feedback del error como contexto, '
    'permitiendo correccion automatica hasta un maximo de intentos.',
]

for pt in nodes_points:
    bullet(pt)

spacer()

# ── 2.3.5 LangChain / LangGraph ───────────────────────────────────────────────

h3('2.3.5  Agent Framework: LangChain y LangGraph')

body(
    'Se explicara el rol de LangChain y LangGraph como las herramientas de '
    'orquestacion sobre las que se implemento la solucion. '
    'Los puntos a cubrir son:'
)

lg_points = [
    'LangChain: capa de abstraccion sobre multiples proveedores de modelos de lenguaje '
    '(OpenAI, Google Gemini, etc.) que estandariza la forma de invocarlos, '
    'manejar prompts y procesar outputs.',
    'LangGraph: extension de LangChain que implementa la orquestacion de agentes '
    'mediante grafos de estado dirigidos, habilitando flujos condicionales, '
    'ciclos de retry y estado compartido entre nodos.',
    'Por que LangGraph sobre prompt chaining simple: el chaining no permite '
    'flujos condicionales, retry automatico ni estado persistente entre pasos.',
    'La relacion con los agentes del sistema: cada agente es un subgrafo de LangGraph '
    'con sus propios nodos y estado interno.',
]

for pt in lg_points:
    bullet(pt)

spacer()

# ── 2.3.6 Python ──────────────────────────────────────────────────────────────

h3('2.3.6  Python como ecosistema de desarrollo de IA')

body(
    'Se explicara brevemente por que Python es el lenguaje estandar para el desarrollo '
    'de sistemas de IA y cuales son las bibliotecas clave que hacen posible el sistema. '
    'Los puntos a cubrir son:'
)

py_points = [
    'Python como lengua franca de la IA: concentra el ecosistema mas amplio de '
    'bibliotecas para modelos de lenguaje, procesamiento de datos y APIs.',
    'FastAPI: framework web asincrono que expone los agentes como endpoints HTTP, '
    'permitiendo la comunicacion con el frontend.',
    'Pydantic: validacion de modelos de datos y enforcement de structured outputs.',
    'Bibliotecas de procesamiento documental: pdfplumber (PDFs), python-docx (Word), '
    'pandas (Excel) para parsear los documentos de entrada del sistema.',
]

for pt in py_points:
    bullet(pt)

spacer()

# ── 2.3.7 Instrumento de evaluacion de calidad ────────────────────────────────

h3('2.3.7  Instrumento de evaluacion de calidad del contenido generado')

body(
    'Se explicara el instrumento construido para que los Docentes Revisores evaluen '
    'la calidad del contenido generado por el sistema. A diferencia de las metricas '
    'tecnicas (cumplimiento de esquema, restricciones de tiempo), este instrumento '
    'mide la calidad pedagogica percibida por expertos. '
    'Se describiran los insumos que debe proporcionar el evaluador y los seis '
    'criterios de la rubrica.'
)

body('Insumos requeridos para la evaluacion:')

insumos = [
    'Nombre y ciclo del curso',
    'Logro del curso',
    'Logro de la unidad',
    'Logro de la semana a la que corresponde el material evaluado',
    'Tema y subtema del material',
]

for ins in insumos:
    bullet(ins)

spacer()
body('Rubrica de evaluacion de calidad de contenido:')

rub_tbl = doc.add_table(rows=7, cols=4)
rub_tbl.style = 'Table Grid'
add_header_row(rub_tbl, ['Criterio', 'Estandar Esperado (5 pts)', 'En proceso (3 pts)', 'Inicial (1 pt)'])

rubric_data = [
    (
        'Alineacion del contenido',
        'El contenido tiene una conexion clara con el logro de la unidad y cubre el tema con un alcance completo, sin dejar vacios de informacion.',
        'El contenido esta relacionado con el logro de la unidad pero incluye material solo tangencialmente relacionado o que divaga.',
        'El contenido no esta relacionado con sus logros y/o tiene material con un alcance insuficiente.',
    ),
    (
        'Exactitud del contenido',
        'El contenido del material es completamente factualmente correcto y tiene suficientes matices para el tema.',
        'El contenido del material tiene errores factuales superficiales como terminologia equivocada, simplificaciones o imprecisiones, pero encaja con el tema.',
        'El contenido del material tiene errores factuales profundos o no encaja con el tema.',
    ),
    (
        'Rigor academico',
        'El contenido del material es profundo, creible y cita / se basa en fuentes confiables.',
        'El contenido es superficial o hace afirmaciones cuestionables / poco creibles.',
        'El contenido no tiene sustento o hace afirmaciones sin soporte.',
    ),
    (
        'Propiedad para el nivel del alumno',
        'El vocabulario, el nivel de dificultad y complejidad del material son los adecuados para el nivel del alumno.',
        'El vocabulario, nivel de dificultad y complejidad son ligeramente muy avanzados o muy simples para el nivel del alumno.',
        'El vocabulario, nivel de dificultad y complejidad no tienen conexion con el nivel del alumno.',
    ),
    (
        'Calidad de ejemplos',
        'El contenido tiene ejemplos relevantes y concretos que suplementan los conceptos explicados.',
        'El contenido tiene ejemplos genericos o solo parcialmente relevantes a los conceptos explicados.',
        'El contenido tiene ejemplos confusos, pobres o no existentes.',
    ),
    (
        'Probabilidad de que el alumno complete el material',
        'El contenido puede generar interes intrinsecamente y haria que los alumnos lo revisen voluntariamente.',
        'El contenido se presta a que los alumnos lo lean si es requerido pero no es motivador.',
        'El contenido se presta a que los alumnos lo revisen superficialmente o lo salten aunque sea requerido.',
    ),
]

for i, (criterio, estandar, en_proceso, inicial) in enumerate(rubric_data):
    row = rub_tbl.rows[i + 1]
    row.cells[0].text = criterio
    row.cells[1].text = estandar
    row.cells[2].text = en_proceso
    row.cells[3].text = inicial

spacer()

body(
    'Se explicara cada criterio en relacion con el tipo de contenido que el sistema '
    'genera, y por que estos seis aspectos son los relevantes para juzgar la calidad '
    'de un material instruccional generado por IA en el contexto universitario.'
)

spacer()

# ═══════════════════════════════════════════════════════════════════════════════
# 2.4  METODOLOGIA DE DESARROLLO
# ═══════════════════════════════════════════════════════════════════════════════

h2('2.4  Metodologia de Desarrollo')

body(
    'En esta seccion se describe el marco metodologico que guio el desarrollo '
    'del sistema a lo largo del proyecto.'
)

h3('2.4.1  SCRUM en equipos multidisciplinarios')

body(
    'Se explicara el framework SCRUM y su aplicacion en un equipo compuesto por '
    'perfiles de distintas disciplinas (ingenieria de software, diseno instruccional, '
    'expertos tematicos). Los puntos a cubrir son:'
)

scrum_points = [
    'Que es SCRUM: framework agil de desarrollo iterativo e incremental basado '
    'en sprints de duracion fija, revisiones constantes y adaptacion continua.',
    'Por que SCRUM es adecuado para proyectos de IA: la calidad del output de un '
    'sistema LLM es desconocida hasta que se prueba con datos reales; los ciclos '
    'cortos permiten detectar y corregir problemas de prompt y arquitectura rapidamente.',
    'La dimension multidisciplinaria: en este proyecto, el equipo integro roles de '
    'desarrollo (backend, frontend) con roles instruccionales (LxD, Docente Revisor), '
    'lo que exige una coordinacion explicita y roles bien definidos dentro del sprint.',
    'El rol del Docente Revisor como validador en cada sprint: '
    'cada iteracion de prompts se valida con expertos reales, '
    'no solo con metricas automaticas.',
]

for pt in scrum_points:
    bullet(pt)

spacer()

# ── Save ──────────────────────────────────────────────────────────────────────

out = 'D:/Proyectos actuales/proyecto_tesis_upc/Capitulo2_Marcoteorico_v1.docx'
doc.save(out)
print(f'Saved: {out}')
