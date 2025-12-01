# DIAGRAMAS UML - HERRAMIENTA DE AUDITORÍA INFORMÁTICA
## Evaluación de la Estructura Orgánica del Área de TI

---

## 1. DIAGRAMA DE CASOS DE USO

```
┌─────────────────────────────────────────────────────────────┐
│                      SISTEMA DE AUDITORÍA TI                │
│                  (Evaluación Estructural del SI)            │
└─────────────────────────────────────────────────────────────┘

                              ┌──────────────┐
                              │   AUDITOR    │
                              │   (Usuario)  │
                              └──────┬───────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
        ▼                            ▼                            ▼
   ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
   │   INGRESAR   │          │  EVALUAR     │          │  GENERAR     │
   │   ESTRUCTURA │          │  ESTRUCTURA  │          │  REPORTE     │
   │  ORGÁNICA    │          │              │          │              │
   └──────────────┘          └──────────────┘          └──────────────┘
        │                            │                       ▲
        │         ┌──────────────────┴───────────────────────┘
        │         │
        │         ▼
        │    ┌──────────────────────────────┐
        │    │   COMPARAR CON ESTÁNDARES    │
        │    │   (Motor de Evaluación)      │
        │    └──────────────────────────────┘
        │         ▲
        │         │
        └─────────┤
                  │
        ┌─────────▼───────────┐
        │   CONSULTAR BASE    │
        │   LEGAL/NORMATIVA   │
        │   (Ayuda)           │
        └─────────────────────┘
```

### Descripciones de Casos de Uso:

1. **Ingresar Estructura Orgánica**: El auditor ingresa los datos de la estructura actual del departamento (roles, posiciones, reportes).
2. **Evaluar Estructura**: El sistema compara la estructura ingresada con un estándar de referencia.
3. **Generar Reporte**: Se produce un reporte con hallazgos, brechas identificadas y puntuación de cumplimiento.
4. **Consultar Base Legal**: El auditor accede a la documentación normativa que justifica los estándares de evaluación.

---

## 2. DIAGRAMA DE CLASES

```
┌──────────────────────────────────────────────────────────────┐
│                      ESTRUCTURA PRINCIPAL                     │
└──────────────────────────────────────────────────────────────┘

        ┌─────────────────────────────────────┐
        │      EstructuraOrganica             │
        ├─────────────────────────────────────┤
        │ - nombre: str                       │
        │ - descripcion: str                  │
        │ - roles: list[Rol]                  │
        │ - nivel_cumplimiento: float         │
        │ - documentos_legales: list[DocLeg] │
        ├─────────────────────────────────────┤
        │ + agregar_rol(rol: Rol)            │
        │ + obtener_roles()                  │
        │ + evaluar()                        │
        │ + generar_reporte()                │
        └─────────────────────────────────────┘
                      △
                      │ contiene
                      │
        ┌─────────────┴──────────────────────┐
        │                                    │
        ▼                                    ▼
    ┌──────────────┐              ┌──────────────────┐
    │      Rol     │              │  DocumentoLegal  │
    ├──────────────┤              ├──────────────────┤
    │ - titulo: str│              │ - nombre: str    │
    │ - descripcion│              │ - contenido: str │
    │ - funciones[]│              │ - fecha: str     │
    │ - reporta_a: │              │ - referencia: str│
    │   Rol (o None)              ├──────────────────┤
    │ - segregacion: │            │ + mostrar()      │
    │   dict (func) │            │ + validar()      │
    ├──────────────┤              └──────────────────┘
    │ + obtener_  │
    │   funciones()│
    │ + tiene_  │
    │   segregacion()│
    │ + generar_  │
    │   hallazgos()│
    └──────────────┘
            △
            │ utiliza
            │
    ┌───────┴──────────────┐
    │                      │
    ▼                      ▼
┌──────────────┐    ┌──────────────────┐
│  Hallazgo    │    │MotorDeEvaluacion │
├──────────────┤    ├──────────────────┤
│ - tipo: str  │    │ - estándares: {} │
│ - descripcion│    │ - roles_minimos[]│
│ - gravedad:  │    │ - funciones_[]   │
│   {crítico,  │    ├──────────────────┤
│   alto,      │    │ + comparar_      │
│   medio,     │    │   estructuras()  │
│   bajo}      │    │ + identificar_   │
│ - rol_ref: Rol     │   brechas()      │
├──────────────┤    │ + calcular_      │
│ + __str__()  │    │   cumplimiento() │
│ + obtener_   │    │ + generar_       │
│   recomenda- │    │   hallazgos()    │
│   ciones()   │    └──────────────────┘
└──────────────┘
```

### Relaciones Principales:

- **EstructuraOrganica** contiene múltiples objetos **Rol**
- **EstructuraOrganica** contiene múltiples objetos **DocumentoLegal**
- **Rol** puede generar **Hallazgos**
- **MotorDeEvaluacion** procesa **EstructuraOrganica** y genera **Hallazgos**

---

## 3. DIAGRAMA DE FLUJO DE DATOS (DFD - Nivel 1)

```
INICIO
  │
  ▼
┌─────────────────────────┐
│  1. CAPTURA DE DATOS    │
│  Estructura Orgánica    │
│  - Roles               │
│  - Funciones           │
│  - Reportes            │
└──────────┬──────────────┘
           │
           ▼
    ┌──────────────────┐
    │ ALMACÉN 1        │
    │ Estructura       │
    │ Actual (JSON)    │
    └────────┬─────────┘
             │
             ▼
  ┌─────────────────────────────┐
  │  2. PROCESO DE AUDITORÍA    │
  │  Motor de Evaluación:       │
  │  - Cargar estándares        │
  │  - Comparar roles           │
  │  - Validar segregación      │
  │  - Identificar brechas      │
  │  - Calcular cumplimiento    │
  └──────────┬──────────────────┘
             │
      ┌──────┴──────┐
      │             │
      ▼             ▼
 ┌─────────┐  ┌──────────────┐
 │ALMACÉN 2│  │  ALMACÉN 3   │
 │Estándares  │  Base Normativa
 │Referencia  │  (Documentos 
 │(BD)        │   Legales)
 └─────────┘  └──────────────┘
      │             │
      └──────┬──────┘
             │
             ▼
  ┌─────────────────────────┐
  │ 3. GENERACIÓN REPORTE   │
  │  - Hallazgos críticos   │
  │  - Brechas identificadas│
  │  - Puntuación           │
  │  - Recomendaciones      │
  └──────────┬──────────────┘
             │
             ▼
  ┌─────────────────────────┐
  │  4. SALIDA AL AUDITOR   │
  │  - Reporte formateado   │
  │  - Visualización texto  │
  │  - Datos para impresión │
  └──────────┬──────────────┘
             │
             ▼
           FIN
```

---

## 4. PSEUDOCÓDIGO - MOTOR DE EVALUACIÓN

```
ALGORITMO MotorDeEvaluacion::Evaluar(estructura_actual)

ENTRADA: 
  estructura_actual: EstructuraOrganica
  
SALIDA:
  - nivel_cumplimiento: float (0-100%)
  - hallazgos: list[Hallazgo]
  - recomendaciones: str

PROCESO:

1. CARGAR ESTÁNDARES DE REFERENCIA
   estándares ← BD_Estándares
   roles_requeridos ← estándares['roles_minimos']
   funciones_obligatorias ← estándares['funciones_críticas']
   reglas_segregación ← estándares['segregación_funciones']

2. VALIDACIÓN INICIAL
   SI estructura_actual.roles está vacío ENTONCES
       RETORNAR: cumplimiento=0%, hallazgo="Sin estructura definida"
   FIN SI

3. COMPARACIÓN DE ROLES
   roles_actuales ← estructura_actual.obtener_roles()
   roles_faltantes ← roles_requeridos - roles_actuales
   roles_extra ← roles_actuales - roles_requeridos
   
   POR CADA rol_faltante EN roles_faltantes:
       hallazgo ← Hallazgo(
           tipo="ROL_FALTANTE",
           descripción="No existe el rol: " + rol_faltante.titulo,
           gravedad="CRÍTICO",
           rol_ref=rol_faltante
       )
       hallazgos.agregar(hallazgo)
   FIN POR CADA

4. VALIDACIÓN DE FUNCIONES
   POR CADA rol EN roles_actuales:
       funciones_asignadas ← rol.obtener_funciones()
       
       POR CADA función_obligatoria EN funciones_obligatorias:
           SI función_obligatoria NO EN funciones_asignadas ENTONCES
               hallazgo ← Hallazgo(
                   tipo="FUNCIÓN_NO_ASIGNADA",
                   descripción=función_obligatoria + " no asignada a " + rol.titulo,
                   gravedad="ALTO",
                   rol_ref=rol
               )
               hallazgos.agregar(hallazgo)
           FIN SI
       FIN POR CADA
   FIN POR CADA

5. VALIDACIÓN DE SEGREGACIÓN DE FUNCIONES
   POR CADA rol EN roles_actuales:
       funciones_rol ← rol.obtener_funciones()
       
       POR CADA regla DE segregación EN reglas_segregación:
           func_incompatibles ← regla.obtener_funciones_incompatibles()
           
           SI alguna(func_incompatibles) EN funciones_rol ENTONCES
               hallazgo ← Hallazgo(
                   tipo="SEGREGACIÓN_INADECUADA",
                   descripción="Rol " + rol.titulo + " tiene funciones incompatibles",
                   gravedad="CRÍTICO",
                   rol_ref=rol
               )
               hallazgos.agregar(hallazgo)
           FIN SI
       FIN POR CADA
   FIN POR CADA

6. DETECCIÓN DE FUNCIONES DUPLICADAS
   funciones_asignadas ← {}
   
   POR CADA rol EN roles_actuales:
       POR CADA función EN rol.obtener_funciones():
           SI función EN funciones_asignadas ENTONCES
               hallazgo ← Hallazgo(
                   tipo="FUNCIÓN_DUPLICADA",
                   descripción=función + " asignada a múltiples roles",
                   gravedad="MEDIO",
                   rol_ref=rol
               )
               hallazgos.agregar(hallazgo)
           SINO
               funciones_asignadas[función] ← rol.titulo
           FIN SI
       FIN POR CADA
   FIN POR CADA

7. VALIDACIÓN DE CADENA DE MANDO
   POR CADA rol EN roles_actuales:
       SI rol.reporta_a = NULL Y rol.titulo ≠ "Director" ENTONCES
           hallazgo ← Hallazgo(
               tipo="SIN_SUPERVISOR",
               descripción="Rol " + rol.titulo + " sin supervisor asignado",
               gravedad="ALTO",
               rol_ref=rol
           )
           hallazgos.agregar(hallazgo)
       FIN SI
   FIN POR CADA

8. CÁLCULO DE NIVEL DE CUMPLIMIENTO
   total_requisitos ← |roles_requeridos| + 
                      |funciones_obligatorias| + 
                      |reglas_segregación|
   
   requisitos_cumplidos ← total_requisitos - |hallazgos|
   
   nivel_cumplimiento ← (requisitos_cumplidos / total_requisitos) * 100
   
   SI nivel_cumplimiento < 0 ENTONCES
       nivel_cumplimiento ← 0
   FIN SI

9. GENERACIÓN DE RECOMENDACIONES
   recomendaciones ← ""
   
   POR CADA hallazgo EN hallazgos:
       SI hallazgo.gravedad = "CRÍTICO" ENTONCES
           recomendaciones += "URGENTE: " + hallazgo.obtener_recomendaciones() + "\n"
       FIN SI
   FIN POR CADA
   
   POR CADA hallazgo EN hallazgos:
       SI hallazgo.gravedad = "ALTO" ENTONCES
           recomendaciones += "IMPORTANTE: " + hallazgo.obtener_recomendaciones() + "\n"
       FIN SI
   FIN POR CADA

10. CLASIFICACIÓN DE CUMPLIMIENTO
    SI nivel_cumplimiento >= 90 ENTONCES
        clasificación ← "CUMPLIMIENTO ALTO"
    SI SINO nivel_cumplimiento >= 70 ENTONCES
        clasificación ← "CUMPLIMIENTO MODERADO"
    SI SINO nivel_cumplimiento >= 50 ENTONCES
        clasificación ← "CUMPLIMIENTO BAJO"
    SI SINO
        clasificación ← "CUMPLIMIENTO CRÍTICO"
    FIN SI

RETORNAR:
    - nivel_cumplimiento
    - hallazgos
    - recomendaciones
    - clasificación

FIN ALGORITMO
```

---

## 5. MATRIZ DE TRAZABILIDAD

| Requerimiento | Caso de Uso | Clase(s) | Método(s) |
|---|---|---|---|
| Ingresar estructura | Ingresar Estructura | EstructuraOrganica, Rol | agregar_rol() |
| Ingresar funciones | Evaluar Estructura | Rol | obtener_funciones() |
| Comparar con estándares | Evaluar Estructura | MotorDeEvaluacion | comparar_estructuras() |
| Identificar brechas | Generar Reporte | MotorDeEvaluacion, Hallazgo | identificar_brechas() |
| Calcular cumplimiento | Generar Reporte | MotorDeEvaluacion | calcular_cumplimiento() |
| Mostrar base legal | Consultar Base Legal | DocumentoLegal | mostrar() |
| Generar reporte | Generar Reporte | EstructuraOrganica | generar_reporte() |

---

## 6. ESPECIFICACIONES TÉCNICAS

### Tipos de Hallazgos:
- **ROL_FALTANTE** → Gravedad: CRÍTICO
- **FUNCIÓN_NO_ASIGNADA** → Gravedad: ALTO
- **SEGREGACIÓN_INADECUADA** → Gravedad: CRÍTICO
- **FUNCIÓN_DUPLICADA** → Gravedad: MEDIO
- **SIN_SUPERVISOR** → Gravedad: ALTO

### Escala de Cumplimiento:
- **90-100%**: Cumplimiento Alto ✓
- **70-89%**: Cumplimiento Moderado ◐
- **50-69%**: Cumplimiento Bajo ✗
- **< 50%**: Cumplimiento Crítico ✗✗

### Estándares de Referencia (ITIL + ISO 27001):
1. Director de Sistemas de Información
2. Jefe de Operaciones/Infraestructura
3. Jefe de Desarrollo
4. Jefe de Seguridad Informática
5. Administrador de Base de Datos
6. Administrador de Sistemas/Red
7. Especialista en Seguridad

