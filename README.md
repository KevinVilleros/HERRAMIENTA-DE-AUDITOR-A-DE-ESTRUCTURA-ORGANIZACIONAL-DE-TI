# HERRAMIENTA DE AUDITORÍA DE ESTRUCTURA ORGANIZACIONAL DE TI

## Descripción

Software diseñado para evaluar la **Estructura Orgánica del Área de Sistemas de Información (SI)** de una organización, con foco en **Auditoría Informática**.

La herramienta facilita la comparación de la estructura actual con modelos ideales o normativos basados en estándares internacionales (ITIL v4, ISO 27001, COBIT 2019, COSO).

---

## Características Principales

### 1. **Funcionalidad de Evaluación**
- Ingreso flexible de estructura organizacional (organigrama)
- Ingreso de funciones y responsabilidades por rol
- Comparación automática con estándares de referencia
- Identificación de brechas (gaps), roles faltantes, segregación inadecuada
- Cálculo de nivel de cumplimiento (0-100%)

### 2. **Análisis Completo**
- **Validación de Roles**: Verifica existencia de roles críticos
- **Validación de Funciones**: Asegura que funciones críticas estén asignadas
- **Segregación de Funciones**: Identifica funciones incompatibles en un rol
- **Duplicación de Funciones**: Detecta funciones asignadas a múltiples roles
- **Cadena de Mando**: Valida estructura jerárquica clara
- **Cobertura de Responsabilidades**: Analiza completitud de funciones por rol

### 3. **Base Legal y Normativa**
- Módulo integrado de "Ayuda / Base Legal"
- Justificación de por qué se audita estructura organizacional
- Referencias a estándares internacionales:
  - ISO/IEC 27001:2022
  - ITIL v4
  - COBIT 2019
  - COSO Framework
  - Leyes y regulaciones locales

### 4. **Reportes Profesionales**
- Reporte resumido con métricas clave
- Detalle de hallazgos por gravedad
- Recomendaciones de acción
- Visualización de estructura actual

---

## Requisitos del Sistema

- **Python**: 3.7 o superior
- **Dependencias**: Ninguna (uso de bibliotecas estándar de Python)
- **Sistemas Operativos**: Windows, Linux, macOS

---

## Instalación y Uso

### 1. Opción A: Usar la Interfaz Interactiva

```bash
python main.py
```

Esto abre un menú interactivo con las opciones:
- Crear/Editar Estructura Organizacional
- Ingresar o Editar Roles y Funciones
- Evaluar Estructura (Auditoría)
- Generar Reporte Completo
- Consultar Base Legal y Normativa
- Ver Datos de Ejemplo (Demo)
- Salir

### 2. Opción B: Ejecutar Script de Prueba

```bash
python test_simple.py
```

Ejecuta 3 pruebas automáticas que demuestran la funcionalidad:
- Prueba 1: Estructura bien configurada
- Prueba 2: Estructura incompleta con brechas
- Prueba 3: Segregación inadecuada de funciones

### 3. Opción C: Usar como Biblioteca Python

```python
from modelos import EstructuraOrganica, Rol
from motor_evaluacion import MotorDeEvaluacion

# Crear estructura
estructura = EstructuraOrganica("Mi Empresa", "Descripción")

# Agregar roles y funciones
director = Rol("Director de Sistemas de Informacion", nivel=1)
director.agregar_funcion("Planificacion estrategica de TI")
estructura.agregar_rol(director)

# Evaluar
motor = MotorDeEvaluacion()
cumplimiento, hallazgos = motor.evaluar_estructura(estructura)

print(f"Cumplimiento: {cumplimiento:.2f}%")
print(f"Hallazgos: {len(hallazgos)}")
```

---

## Estructura del Proyecto

```
par2/
├── main.py                  # Punto de entrada (interfaz interactiva)
├── test_simple.py           # Script de prueba con 3 escenarios
├── interfaz.py              # Interfaz de usuario (menú)
├── modelos.py               # Definición de clases (Rol, Hallazgo, etc)
├── motor_evaluacion.py      # Lógica de auditoría
├── base_legal.py            # Documentación normativa
├── DIAGRAMAS_UML.md         # Documentación UML completa
├── README.md                # Este archivo
└── prueba_demo.py           # Script de prueba adicional
```

---

## Componentes Principales

### **modelos.py**
Define las entidades principales:
- `Rol`: Representa un puesto en la estructura
- `Hallazgo`: Representa un hallazgo o brecha identificada
- `DocumentoLegal`: Referencias normativas
- `EstructuraOrganica`: Contenedor de toda la estructura

### **motor_evaluacion.py**
Implementa la lógica de auditoría:
- Carga estándares de referencia
- Compara estructura actual con estándares
- Identifica brechas y hallazgos
- Calcula nivel de cumplimiento
- Genera recomendaciones

### **base_legal.py**
Proporciona documentación normativa:
- Justificación de la auditoría
- Referencias a ISO 27001
- Referencias a ITIL v4
- Referencias a COBIT 2019
- Referencias a COSO Framework

### **interfaz.py**
Gestiona la interacción con el usuario:
- Menú principal
- Gestión de roles
- Evaluación de estructura
- Generación de reportes
- Consulta de base legal

---

## Estándares de Referencia Implementados

### Roles Requeridos Mínimos:
1. Director de Sistemas de Informacion
2. Jefe de Operaciones/Infraestructura
3. Jefe de Desarrollo/Software
4. Jefe de Seguridad Informatica
5. Administrador de Bases de Datos
6. Administrador de Sistemas/Red

### Funciones Críticas:
- Planificacion estrategica de TI
- Gestion de riesgos TI
- Gestion de seguridad informatica
- Cumplimiento normativo
- Gestion de cambios
- Gestion de incidentes
- Recuperacion ante desastres
- Auditoria interna de seguridad

### Reglas de Segregación de Funciones:
- NO: Aprobación + Ejecución de cambios
- NO: Crear usuario + Asignar permisos
- NO: Ejecución transacciones + Auditoría

---

## Escala de Cumplimiento

| Rango | Clasificación | Significado |
|-------|---------------|-------------|
| 90-100% | CUMPLIMIENTO ALTO | Estructura adecuada |
| 70-89% | CUMPLIMIENTO MODERADO | Requiere mejoras |
| 50-69% | CUMPLIMIENTO BAJO | Mejoras urgentes |
| < 50% | CUMPLIMIENTO CRÍTICO | Reconfiguración necesaria |

---

## Ejemplos de Uso

### Ejemplo 1: Crear Estructura Manualmente

```
Menu -> 1: Crear Estructura
  Nombre: "Empresa ABC"
  Descripción: "Departamento de TI"

Menu -> 2: Ingresar Roles
  Opción 1: Agregar Rol
    Título: "Director de Sistemas de Informacion"
    Nivel: 1
    
  Opción 1: Agregar Rol
    Título: "Jefe de Operaciones"
    Nivel: 2
    
  (Agregar más roles según sea necesario)

Menu -> 2: Ingresar Roles
  Opción 2: Editar Funciones de un Rol
    Seleccionar: "Director de Sistemas de Informacion"
    Agregar: "Planificacion estrategica de TI"
    Agregar: "Gestion de riesgos TI"
    (Agregar más funciones)

Menu -> 3: Evaluar Estructura
  (El sistema analiza y genera hallazgos)

Menu -> 4: Generar Reporte
  (Se muestra reporte completo con recomendaciones)

Menu -> 5: Consultar Base Legal
  (Se muestran estándares y justificación)
```

### Ejemplo 2: Cargar Datos de Demostración

```
Menu -> 6: Ver Datos de Ejemplo
  (Carga una estructura de ejemplo)

Menu -> 3: Evaluar Estructura
  (Evalúa el ejemplo)

Menu -> 4: Generar Reporte
  (Visualiza el reporte)
```

---

## Hallazgos Identificables

| Tipo | Gravedad | Descripción |
|------|----------|-------------|
| ROL_FALTANTE | CRÍTICO | Rol requerido no existe |
| FUNCIÓN_NO_ASIGNADA | CRÍTICO | Función crítica no está asignada |
| SEGREGACIÓN_INADECUADA | CRÍTICO | Funciones incompatibles en un rol |
| FUNCIÓN_DUPLICADA | MEDIO | Función asignada a múltiples roles |
| SIN_SUPERVISOR | ALTO | Rol sin supervisor definido |
| REPORTES_MÚLTIPLES | ALTO | Múltiples líneas de reporte |

---

## Diagrama de Flujo General

```
INICIO
  |
  v
┌────────────────────────┐
│ Crear Estructura       │
│ Ingresa Roles          │
│ Ingresa Funciones      │
└─────────┬──────────────┘
          |
          v
┌────────────────────────┐
│ Motor de Evaluación    │
│ 1. Validar Roles       │
│ 2. Validar Funciones   │
│ 3. Segregación         │
│ 4. Duplicación         │
│ 5. Cadena de Mando     │
│ 6. Cobertura           │
└─────────┬──────────────┘
          |
          v
┌────────────────────────┐
│ Calcular Cumplimiento  │
│ Generar Hallazgos      │
│ Elaborar Recomendaciones
└─────────┬──────────────┘
          |
          v
┌────────────────────────┐
│ Mostrar Reporte        │
│ Hallazgos por Gravedad │
│ Puntuación             │
│ Recomendaciones        │
└─────────┬──────────────┘
          |
          v
        FIN
```

---

## Notas Importantes

1. **Nombres de Roles**: Use nombres consistentes. Pueden incluir espacios (ej: "Jefe de Operaciones")
2. **Funciones**: Escriba funciones de manera específica (ej: "Gestion de seguridad informatica")
3. **Sin Acentos**: Por compatibilidad, evite acentos en la interfaz de entrada
4. **Jerarquía**: Asigne supervisores para todos los roles excepto el Director
5. **Funciones Críticas**: Asegúrese de asignar todas las 8 funciones críticas definidas

---

## Estándares Implementados

### ISO/IEC 27001:2022
- Segregación de funciones
- Gestión de seguridad de la información
- Responsabilidades y competencias

### ITIL v4
- Niveles organizacionales (Estratégico, Táctico, Operacional)
- Procesos de gestión de servicios
- Roles por servicio

### COBIT 2019
- Governance de TI
- Roles y autoridades
- Comités de dirección

### COSO Framework
- Control interno
- Responsabilidades
- Segregación de funciones

---

## Troubleshooting

### Error: "AttributeError" al ejecutar
**Solución**: Asegúrese de estar en el directorio correcto y que todos los archivos .py estén presentes.

### Problemas de Codificación en Windows
**Solución**: Use `test_simple.py` en lugar de `prueba_demo.py` (versión simplificada sin caracteres especiales).

### Estructura no se evalúa
**Solución**: Verifique que:
- Tenga al menos 1 rol definido
- El rol tenga al menos 1 función asignada
- Use nombres de roles consistentes

---

## Créditos y Referencias

- **Basado en**: Estándares ITIL, ISO 27001, COBIT 2019, COSO
- **Lenguaje**: Python 3.7+
- **Versión**: 1.0
- **Año**: 2025

---

## Licencia

Este software se proporciona "tal cual" para propósitos educativos y de auditoría.

---

## Contacto y Soporte

Para preguntas o sugerencias sobre esta herramienta de auditoría, revise la documentación UML en `DIAGRAMAS_UML.md`.

---

**Última actualización**: 01/12/2025
