"""
MÓDULO DE BASE LEGAL Y NORMATIVA
Contiene la documentación legal que justifica los estándares de evaluación.

Este módulo implementa el requisito 3: "Módulo de Ayuda: Implementa una opción 
en el menú principal llamada 'Ayuda / Base Legal'".
"""

from modelos import DocumentoLegal


class BaseLegal:
    """
    Gestiona los documentos normativos y legales de referencia.
    """
    
    @staticmethod
    def obtener_documentos() -> list:
        """
        Retorna la lista de documentos legales utilizados como base
        para la evaluación de la estructura orgánica.
        """
        documentos = []
        
        # Documento 1: Justificación General
        doc1 = DocumentoLegal(
            nombre="JUSTIFICACIÓN DE LA AUDITORÍA DE ESTRUCTURA ORGÁNICA",
            contenido="""
La auditoría de la estructura organizacional del área de Sistemas de Información 
(SI) es un proceso fundamental en la Auditoría Informática. Esta evaluación se 
realiza para:

1. GARANTIZAR LA SEGREGACIÓN DE FUNCIONES
   - Prevenir conflictos de intereses
   - Evitar concentración de poder en individuos
   - Asegurar controles internos efectivos

2. VALIDAR LA COBERTURA DE RESPONSABILIDADES
   - Verificar que todas las funciones críticas estén asignadas
   - Identificar roles faltantes o duplicados
   - Asegurar líneas de autoridad claras

3. CUMPLIMIENTO NORMATIVO
   - Satisfacer requisitos de Leyes y Regulaciones
   - Alinearse con estándares de Gobierno Corporativo
   - Implementar mejores prácticas de TI

4. MITIGACIÓN DE RIESGOS
   - Reducir riesgos operacionales
   - Prevenir fraude o negligencia
   - Asegurar continuidad del negocio

5. MEJORA DE GOBERNANZA
   - Establecer una estructura clara y eficiente
   - Mejorar la toma de decisiones
   - Facilitar la auditoría y el control

ALCANCE
Esta auditoría evalúa la estructura organizacional del área de SI contra 
estándares internacionales de buenas prácticas, identificando brechas y 
formulando recomendaciones de mejora.
            """,
            referencia="Normas de Auditoría Informática"
        )
        documentos.append(doc1)
        
        # Documento 2: ISO 27001
        doc2 = DocumentoLegal(
            nombre="ISO/IEC 27001:2022 - Gestión de Seguridad de la Información",
            contenido="""
La norma ISO/IEC 27001 es el estándar internacional más reconocido para la 
gestión de seguridad de la información. Establece requisitos para:

A.6 ORGANIZACIÓN DE LA INFORMACIÓN (Annex A - Control 6)

A.6.1 - Responsabilidades y competencias de la información
   • Establecer responsabilidades clara para la gestión de información
   • Asignar roles y responsabilidades apropiados
   • Definir competencias requeridas para cada rol
   • Realizar evaluaciones de competencias

A.6.2 - Segregación de funciones
   • Segregar funciones conflictivas
   • Prevenir autorización no autorizada
   • Distribuir responsabilidades críticas entre múltiples personas
   • Revisar periódicamente la segregación

A.6.3 - Separación de deberes
   • Las siguientes funciones deben estar separadas:
     - Solicitud y aprobación de cambios
     - Desarrollo y prueba de cambios
     - Implementación y auditoría de cambios
     - Administración y auditoría

REQUISITOS APLICABLES A LA ESTRUCTURA ORGÁNICA:

1. Debe existir un responsable de seguridad de la información
2. Debe establecerse una estructura clara de mando
3. Las funciones conflictivas deben estar segregadas
4. Los roles deben tener responsabilidades bien definidas
5. Debe existir capacitación en seguridad
6. Las decisiones de seguridad deben ser documentadas

CRITERIOS DE CUMPLIMIENTO (para esta auditoría):
✓ Existe un Jefe/Director de Seguridad Informática
✓ Existe segregación clara entre roles operacionales y de auditoría
✓ Todas las funciones críticas de seguridad están asignadas
✓ Existe una línea clara de reporte en temas de seguridad
            """,
            referencia="ISO/IEC 27001:2022, Clause 6.2",
            fecha_publicación="2022"
        )
        documentos.append(doc2)
        
        # Documento 3: ITIL v4
        doc3 = DocumentoLegal(
            nombre="ITIL v4 - IT Service Management",
            contenido="""
ITIL (Information Technology Infrastructure Library) v4 proporciona un marco 
de buenas prácticas para la gestión de servicios de TI. Los principios 
aplicables a la estructura organizacional incluyen:

ESTRUCTURA ORGANIZACIONAL RECOMENDADA (ITIL):

1. NIVEL ESTRATÉGICO
   Rol: Director de Sistemas de Información
   Responsabilidades:
   - Alineación de TI con el negocio
   - Planificación estratégica plurianual
   - Gestión de cartera de servicios
   - Governance y Compliance

2. NIVEL TÁCTICO
   Roles: Jefes de Áreas (Operaciones, Desarrollo, Seguridad)
   Responsabilidades:
   - Gestión de servicios e incidentes
   - Planificación de cambios
   - Gestión de configuración
   - Mejora continua

3. NIVEL OPERACIONAL
   Roles: Especialistas (Administradores, Técnicos)
   Responsabilidades:
   - Operación de sistemas
   - Monitoreo y alertas
   - Resolución de problemas
   - Documentación técnica

PROCESOS ITIL Y ROLES REQUERIDOS:

- Incident Management → Especialista de Incidentes/DBA
- Change Management → Jefe de Desarrollo + Jefe de Operaciones
- Problem Management → Equipo de Diagnóstico
- Release Management → Jefe de Desarrollo
- Configuration Management → Administrador de Sistemas
- Service Continuity → Director de SI + Jefe de Operaciones
- Availability Management → Jefe de Operaciones
- Capacity Management → Administrador de Sistemas
- Security Management → Jefe de Seguridad

REQUISITOS ESTRUCTURALES:
✓ Mínimo 1 director a nivel de servicios
✓ Mínimo 1 responsable por cada área funcional principal
✓ Separación clara entre desarrollo y operación
✓ Responsable dedicado para cambios y releases
✓ Responsable de seguridad independiente
            """,
            referencia="ITIL v4 Foundation, 2019",
            fecha_publicación="2019"
        )
        documentos.append(doc3)
        
        # Documento 4: COBIT 2019
        doc4 = DocumentoLegal(
            nombre="COBIT 2019 - Gobierno Corporativo de TI",
            contenido="""
COBIT (Control Objectives for Information and Related Technology) es un 
framework integrado desarrollado por ISACA para el gobierno y gestión de TI.

DOMINIO: GOVERN - ESTRUCTURA ORGANIZACIONAL (EDM02)

Objetivo de Governance: 
"Garantizar que la estructura, autoridades y responsabilidades de TI estén 
establecidas para facilitar el logro de objetivos de TI"

COMPONENTES DE ESTRUCTURA REQUERIDA:

1. Marco de Gobernanza
   - Definición clara de roles y responsabilidades
   - Documentación de la estructura organizacional
   - Establecimiento de autoridades y límites de decisión

2. Estructura de Comités
   - Comité de Dirección de TI (CIO + Ejecutivos)
   - Comité de Seguridad de la Información
   - Comité de Auditoría Interna

3. Roles Críticos
   - Chief Information Officer (CIO) / Director de SI
   - Chief Information Security Officer (CISO)
   - Chief Data Officer (CDO) o DBA
   - Enterprise Architect
   - Risk & Compliance Officer

4. Líneas de Reporte
   - La función de Auditoría debe reportar al máximo nivel
   - La Seguridad debe tener independencia funcional
   - El CIO debe reportar a la Junta Directiva

CRITERIOS DE EVALUACIÓN PARA ESTA AUDITORÍA:

Requisitos CRÍTICOS (Cumplimiento >90%):
[ ] Existe un Director/CIO de Sistemas
[ ] Existe un responsable de Seguridad Informática
[ ] Existe segregación entre Auditoría y Operación
[ ] Todas las funciones críticas están documentadas y asignadas

Requisitos IMPORTANTES (Cumplimiento 70-90%):
[ ] Existe responsable de Calidad de Software
[ ] Existe responsable de Infraestructura
[ ] Existe responsable de Administración de Datos
[ ] Los roles tienen supervisores claramente definidos

Requisitos RECOMENDADOS (Cumplimiento 50-70%):
[ ] Existe responsable de Continuidad de Negocio
[ ] Existe responsable de Archivos y Documentación
[ ] Se realizan evaluaciones de competencias
[ ] Existe plan de sucesión para roles críticos
            """,
            referencia="COBIT 2019, EDM02",
            fecha_publicación="2019"
        )
        documentos.append(doc4)
        
        # Documento 5: COSO Framework
        doc5 = DocumentoLegal(
            nombre="COSO - Marco de Control Interno",
            contenido="""
El Framework COSO (Committee of Sponsoring Organizations) es el estándar 
más ampliamente aceptado para el establecimiento de sistemas de control 
interno en organizaciones.

DIMENSIÓN: AMBIENTE DE CONTROL

Componente 1: Responsabilidades, Autoridades y Competencias
El ambiente de control debe incluir:

1. ESTABLECIMIENTO DE RESPONSABILIDADES
   - Roles y responsabilidades formalmente documentados
   - Autoridades claramente definidas y comunicadas
   - Segregación de funciones donde sea posible

2. COMPETENCIAS REQUERIDAS
   - Perfiles de puesto definidos
   - Requisitos de conocimiento y experiencia
   - Evaluación de competencias
   - Planes de capacitación

3. SEGREGACIÓN DE FUNCIONES
   Las siguientes funciones deben estar separadas:
   
   Transacciones:
   - Iniciación de transacciones
   - Aprobación de transacciones
   - Registro de transacciones
   - Custodia de activos
   - Conciliación
   - Auditoría
   
   Accesos de Sistema:
   - Otorgamiento de derechos
   - Uso de sistemas
   - Monitoreo de accesos

4. LÍNEAS DE REPORTE Y CADENA DE MANDO
   - Línea de reporte única para cada persona
   - Excepto para funciones específicas (ej. Auditoría)
   - Autoridades de decisión claramente asignadas

5. RESPONSABILIDADES DE AUDITORÍA INTERNA
   - La función de auditoría debe ser independiente
   - Debe reportar a la máxima autoridad
   - No debe tener responsabilidades operacionales
   - Debe tener acceso irrestricto a la información

MAPEO A ESTRUCTURA ORGÁNICA DE TI:

Segregación típica recomendada:
- Cambios deben ser aprobados por Jefe diferente al que ejecuta
- Bases de datos deben administrarse separadamente de desarrollo
- Seguridad debe ser independiente de operaciones
- Auditoría debe ser externa o independiente de IT

INDICADORES DE CONTROL DEFICIENTE:
✗ Roles acumulativos (ej. DBA + Auditor)
✗ Sin supervisión en roles operacionales críticos
✗ Funciones conflictivas en un solo rol
✗ Ausencia de documentación de autoridades
✗ Sin separación entre desarrollo y producción
            """,
            referencia="COSO Internal Control Framework, 2013",
            fecha_publicación="2013"
        )
        documentos.append(doc5)
        
        # Documento 6: Leyes y Regulaciones Locales
        doc6 = DocumentoLegal(
            nombre="MARCOS LEGALES Y REGULATORIOS APLICABLES",
            contenido="""
Dependiendo de la jurisdicción y sector industrial, aplican diferentes 
marcos regulatorios. Esta auditoría considera:

1. LEYES GENERALES DE AUDITORÍA Y CONTROL INTERNO
   - Ley de Auditoría Interna (o equivalente por país)
   - Código de Buen Gobierno Corporativo
   - Leyes de Transparencia y Acceso a Información
   - Regulaciones de Supervisión Bancaria (si aplica)

2. LEYES DE PROTECCIÓN DE DATOS
   - GDPR (Europa)
   - Leyes de Protección de Datos Personales (LPPDP)
   - Regulaciones de Privacidad Sector Salud (HIPAA)
   - Regulaciones PCI DSS (para comercio electrónico)

3. LEYES DE CONTINUIDAD DE NEGOCIO
   - Requisitos de disponibilidad de servicios críticos
   - Planes de recuperación ante desastres
   - Backup y archivos de datos

4. LEYES TRIBUTARIAS Y LABORALES
   - Requisitos de auditoría tributaria
   - Regulaciones de seguridad y salud ocupacional
   - Regulaciones de empleo y relaciones laborales

ESTÁNDARES ESPECÍFICOS POR INDUSTRIA:

Sector Bancario:
- Basilea III (Regulación de Bancos Centrales)
- Requerimientos de Seguridad Bancaria
- Regulaciones Anti-Lavado de Dinero (AML)

Sector Salud:
- HIPAA (Portability and Accountability Act)
- Leyes de Confidencialidad Médica
- Estándares de Auditoría de Sistemas de Salud

Sector Público:
- Leyes de Administración Pública
- Leyes de Contratación Estatal
- Regulaciones de Gobierno Electrónico

Sector Financiero:
- Regulaciones de la Bolsa de Valores
- Estándares de Auditoría Financiera (IFRS)
- Regulaciones de Fondos de Pensiones

APLICACIÓN A ESTA AUDITORÍA:
Este software aplica el principio general de segregación de funciones y 
establecimiento de una estructura clara, que es aplicable a TODAS las 
jurisdicciones y sectores como base de un sistema de control interno sólido.
            """,
            referencia="Legislación Local y Regulaciones Internacionales"
        )
        documentos.append(doc6)
        
        return documentos
    
    @staticmethod
    def mostrar_base_legal() -> str:
        """
        Genera una presentación formateada de la base legal.
        """
        documentos = BaseLegal.obtener_documentos()
        
        salida = "\n"
        salida += "╔" + "═"*68 + "╗\n"
        salida += "║" + " "*68 + "║\n"
        salida += "║" + "  BASE LEGAL Y NORMATIVA DE EVALUACIÓN".center(68) + "║\n"
        salida += "║" + "  Auditoría de Estructura Orgánica - Área de TI".center(68) + "║\n"
        salida += "║" + " "*68 + "║\n"
        salida += "╚" + "═"*68 + "╝\n"
        
        for i, doc in enumerate(documentos, 1):
            salida += f"\n[DOCUMENTO {i} DE {len(documentos)}]\n"
            salida += doc.mostrar()
        
        salida += "\n"
        salida += "═"*70 + "\n"
        salida += "FIN DE LA BASE LEGAL Y NORMATIVA\n"
        salida += "═"*70 + "\n"
        
        return salida
    
    @staticmethod
    def obtener_resumen_base_legal() -> str:
        """
        Retorna un resumen rápido de la base legal.
        """
        resumen = """
╔════════════════════════════════════════════════════════════════════════╗
║                    RESUMEN DE BASE LEGAL                              ║
║           Fundamentos para la Evaluación de Estructura Orgánica        ║
╚════════════════════════════════════════════════════════════════════════╝

PROPÓSITO DE LA AUDITORÍA:
─────────────────────────
La auditoría de estructura orgánica del área de TI se realiza para:
  ✓ Verificar segregación de funciones y controles internos
  ✓ Validar cobertura de responsabilidades críticas
  ✓ Cumplir con estándares de gobierno corporativo y normativas
  ✓ Mitigar riesgos operacionales y de seguridad
  ✓ Mejorar la gobernanza y eficiencia de TI

ESTÁNDARES DE REFERENCIA:
──────────────────────────
  1. ISO/IEC 27001:2022 - Gestión de Seguridad de la Información
  2. ITIL v4 - IT Service Management Framework
  3. COBIT 2019 - Governance & Management of Enterprise IT
  4. COSO - Marco de Control Interno
  5. Leyes y Regulaciones Locales (por jurisdicción)

ROLES REQUERIDOS (mínimo):
──────────────────────────
  □ Director de Sistemas de Información
  □ Jefe de Operaciones/Infraestructura
  □ Jefe de Desarrollo de Software
  □ Jefe de Seguridad Informática
  □ Administrador de Bases de Datos
  □ Administrador de Sistemas/Red

FUNCIONES CRÍTICAS (deben estar asignadas):
────────────────────────────────────────────
  □ Planificación estratégica de TI
  □ Gestión de riesgos TI
  □ Gestión de seguridad informática
  □ Cumplimiento normativo
  □ Gestión de cambios
  □ Gestión de incidentes
  □ Recuperación ante desastres
  □ Auditoría interna de seguridad

REGLAS DE SEGREGACIÓN (funciones incompatibles):
─────────────────────────────────────────────────
  ✗ Aprobación Y Ejecución de cambios
  ✗ Crear usuario Y Asignar permisos (desarrollo)
  ✗ Ejecución de transacciones Y Auditoría de las mismas
  ✗ Desarrollo de código Y Prueba de calidad
  ✗ Operación de sistemas Y Auditoría de sistemas

CRITERIOS DE CUMPLIMIENTO:
──────────────────────────
  90-100%  → CUMPLIMIENTO ALTO        (Estructura adecuada)
   70-89%  → CUMPLIMIENTO MODERADO    (Requiere mejoras)
   50-69%  → CUMPLIMIENTO BAJO        (Mejoras urgentes)
   < 50%   → CUMPLIMIENTO CRÍTICO     (Reconfiguración necesaria)

Para consultar la documentación completa, seleccione "Ver Documentos Legales"
desde el menú principal.

═══════════════════════════════════════════════════════════════════════════
        """
        return resumen
