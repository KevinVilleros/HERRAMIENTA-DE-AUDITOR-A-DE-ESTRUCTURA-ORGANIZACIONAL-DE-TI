"""
MÓDULO DEL MOTOR DE EVALUACIÓN
Implementa la lógica de auditoría: comparación, validación y generación de hallazgos.

Funciones principales:
- Cargar estándares de referencia
- Comparar estructura actual con estándares
- Identificar brechas y hallazgos
- Calcular nivel de cumplimiento
- Generar recomendaciones
"""

from typing import List, Dict, Tuple, Optional
from modelos import (
    Rol, Hallazgo, EstructuraOrganica, 
    TipoHallazgoEnum, GravedadEnum
)


class MotorDeEvaluacion:
    """
    Motor principal de evaluación de estructuras organizacionales.
    
    Implementa los algoritmos de auditoría para identificar brechas,
    calcular cumplimiento y generar recomendaciones.
    """
    
    # ESTÁNDARES DE REFERENCIA (basados en ITIL e ISO 27001)
    ROLES_REQUERIDOS = {
        "Director de Sistemas de Información": {
            "nivel": 1,
            "funciones_clave": [
                "Planificación estratégica de TI",
                "Alineación con negocio",
                "Gestión de riesgos TI",
                "Gestión presupuestaria"
            ]
        },
        "Jefe de Operaciones/Infraestructura": {
            "nivel": 2,
            "funciones_clave": [
                "Gestión de infraestructura",
                "Monitoreo de sistemas",
                "Disponibilidad de servicios",
                "Mantenimiento de hardware"
            ]
        },
        "Jefe de Desarrollo/Software": {
            "nivel": 2,
            "funciones_clave": [
                "Gestión de proyectos de desarrollo",
                "Control de calidad de software",
                "Metodologías de desarrollo",
                "Integración continua"
            ]
        },
        "Jefe de Seguridad Informática": {
            "nivel": 2,
            "funciones_clave": [
                "Gestión de seguridad informática",
                "Cumplimiento normativo",
                "Gestión de incidentes de seguridad",
                "Auditoría interna de seguridad"
            ]
        },
        "Administrador de Bases de Datos": {
            "nivel": 3,
            "funciones_clave": [
                "Gestión de bases de datos",
                "Backup y recuperación",
                "Optimización de rendimiento",
                "Seguridad de datos"
            ]
        },
        "Administrador de Sistemas/Red": {
            "nivel": 3,
            "funciones_clave": [
                "Administración de redes",
                "Gestión de servidores",
                "Configuración de sistemas",
                "Soporte técnico de infraestructura"
            ]
        }
    }
    
    # FUNCIONES CRÍTICAS QUE DEBEN ESTAR ASIGNADAS
    FUNCIONES_CRÍTICAS = [
        "Planificación estratégica de TI",
        "Gestión de riesgos TI",
        "Gestión de seguridad informática",
        "Cumplimiento normativo",
        "Gestión de cambios",
        "Gestión de incidentes",
        "Recuperación ante desastres",
        "Auditoría interna de seguridad"
    ]
    
    # REGLAS DE SEGREGACIÓN DE FUNCIONES
    SEGREGACIÓN_FUNCIONES = {
        "Autorización y Ejecución": [
            "Aprobación de cambios",
            "Ejecución de cambios"
        ],
        "Validación y Uso": [
            "Crear usuario",
            "Asignar permisos",
            "Ejecutar transacción"
        ],
        "Auditoría y Operación": [
            "Ejecución de transacciones críticas",
            "Auditoría de transacciones"
        ]
    }
    
    def __init__(self):
        """Inicializa el motor de evaluación."""
        self.estructura_evaluada: Optional[EstructuraOrganica] = None
        self.nivel_cumplimiento: float = 0.0
        self.hallazgos: List[Hallazgo] = []
    
    def evaluar_estructura(self, estructura: EstructuraOrganica) -> Tuple[float, List[Hallazgo]]:
        """
        MÉTODO PRINCIPAL: Evalúa una estructura organizacional.
        
        Argumentos:
            estructura: EstructuraOrganica a evaluar
        
        Retorna:
            Tupla (nivel_cumplimiento, lista_hallazgos)
        """
        self.estructura_evaluada = estructura
        self.hallazgos = []
        
        # Validación inicial
        if not estructura.obtener_roles():
            self._crear_hallazgo(
                tipo=TipoHallazgoEnum.ROL_FALTANTE,
                descripcion="No hay roles definidos en la estructura",
                gravedad=GravedadEnum.CRÍTICO,
                recomendación="Ingrese la estructura organizacional completa"
            )
            estructura.nivel_cumplimiento = 0.0
            estructura.hallazgos = self.hallazgos
            return 0.0, self.hallazgos
        
        # Ejecución de validaciones
        self._validar_roles_requeridos(estructura)
        self._validar_funciones_críticas(estructura)
        self._validar_segregacion_funciones(estructura)
        self._validar_duplicacion_funciones(estructura)
        self._validar_cadena_mando(estructura)
        self._validar_cobertura_funciones(estructura)
        
        # Cálculo del nivel de cumplimiento
        self.nivel_cumplimiento = self._calcular_cumplimiento(estructura)
        
        # Guardar resultados en la estructura
        estructura.nivel_cumplimiento = self.nivel_cumplimiento
        estructura.hallazgos = self.hallazgos
        estructura.fecha_evaluación = self._obtener_fecha_actual()
        
        return self.nivel_cumplimiento, self.hallazgos
    
    def _validar_roles_requeridos(self, estructura: EstructuraOrganica) -> None:
        """
        VALIDACIÓN 1: Verifica que existan los roles requeridos.
        """
        roles_estructura = {rol.titulo for rol in estructura.obtener_roles()}
        
        for rol_requerido in self.ROLES_REQUERIDOS.keys():
            if rol_requerido not in roles_estructura:
                self._crear_hallazgo(
                    tipo=TipoHallazgoEnum.ROL_FALTANTE,
                    descripcion=f"No existe el rol requerido: '{rol_requerido}'",
                    gravedad=GravedadEnum.CRÍTICO,
                    rol_afectado=None,
                    recomendación=f"Crear el rol '{rol_requerido}' en la estructura organizacional"
                )
    
    def _validar_funciones_críticas(self, estructura: EstructuraOrganica) -> None:
        """
        VALIDACIÓN 2: Verifica que las funciones críticas estén asignadas.
        """
        funciones_asignadas = self._obtener_todas_funciones(estructura)
        
        for función_crítica in self.FUNCIONES_CRÍTICAS:
            if función_crítica not in funciones_asignadas:
                self._crear_hallazgo(
                    tipo=TipoHallazgoEnum.FUNCIÓN_NO_ASIGNADA,
                    descripcion=f"Función crítica no asignada: '{función_crítica}'",
                    gravedad=GravedadEnum.CRÍTICO,
                    recomendación=f"Asignar la función '{función_crítica}' a un rol específico"
                )
    
    def _validar_segregacion_funciones(self, estructura: EstructuraOrganica) -> None:
        """
        VALIDACIÓN 3: Verifica que no haya funciones incompatibles en un mismo rol.
        """
        for rol in estructura.obtener_roles():
            funciones_rol = set(rol.obtener_funciones())
            
            for regla_nombre, funciones_incompatibles in self.SEGREGACIÓN_FUNCIONES.items():
                funciones_en_conflicto = funciones_rol & set(funciones_incompatibles)
                
                if len(funciones_en_conflicto) > 1:
                    self._crear_hallazgo(
                        tipo=TipoHallazgoEnum.SEGREGACIÓN_INADECUADA,
                        descripcion=f"Rol '{rol.titulo}' tiene funciones incompatibles (regla: {regla_nombre}): {', '.join(funciones_en_conflicto)}",
                        gravedad=GravedadEnum.CRÍTICO,
                        rol_afectado=rol,
                        recomendación=f"Segregar las funciones {', '.join(funciones_en_conflicto)} en roles diferentes"
                    )
    
    def _validar_duplicacion_funciones(self, estructura: EstructuraOrganica) -> None:
        """
        VALIDACIÓN 4: Identifica funciones asignadas a múltiples roles (duplicación).
        """
        funciones_por_rol = {}
        
        for rol in estructura.obtener_roles():
            for función in rol.obtener_funciones():
                if función not in funciones_por_rol:
                    funciones_por_rol[función] = []
                funciones_por_rol[función].append(rol)
        
        # Identificar funciones duplicadas
        for función, roles_asignados in funciones_por_rol.items():
            if len(roles_asignados) > 1:
                roles_str = ", ".join([r.titulo for r in roles_asignados])
                self._crear_hallazgo(
                    tipo=TipoHallazgoEnum.FUNCIÓN_DUPLICADA,
                    descripcion=f"Función '{función}' asignada a múltiples roles: {roles_str}",
                    gravedad=GravedadEnum.MEDIO,
                    rol_afectado=roles_asignados[0],
                    recomendación=f"Consolidar la función '{función}' en un único rol responsable"
                )
    
    def _validar_cadena_mando(self, estructura: EstructuraOrganica) -> None:
        """
        VALIDACIÓN 5: Verifica que exista una cadena de mando clara.
        """
        roles = estructura.obtener_roles()
        
        # Debe existir al menos un director
        directores = [r for r in roles if r.nivel == 1]
        if not directores:
            self._crear_hallazgo(
                tipo=TipoHallazgoEnum.SIN_SUPERVISOR,
                descripcion="No existe un Director o líder de nivel superior",
                gravedad=GravedadEnum.CRÍTICO,
                recomendación="Establecer un Director de Sistemas como líder máximo"
            )
        
        # Cada rol (excepto directores) debe tener supervisor
        for rol in roles:
            if rol.nivel > 1 and rol.reporta_a is None:
                self._crear_hallazgo(
                    tipo=TipoHallazgoEnum.SIN_SUPERVISOR,
                    descripcion=f"Rol '{rol.titulo}' no tiene supervisor asignado",
                    gravedad=GravedadEnum.ALTO,
                    rol_afectado=rol,
                    recomendación=f"Asignar un supervisor al rol '{rol.titulo}'"
                )
    
    def _validar_cobertura_funciones(self, estructura: EstructuraOrganica) -> None:
        """
        VALIDACIÓN 6: Verifica cobertura de funciones por rol.
        """
        for rol_esperado, config in self.ROLES_REQUERIDOS.items():
            rol_encontrado = estructura.obtener_rol(rol_esperado)
            
            if rol_encontrado:
                funciones_esperadas = set(config["funciones_clave"])
                funciones_asignadas = set(rol_encontrado.obtener_funciones())
                funciones_faltantes = funciones_esperadas - funciones_asignadas
                
                # Alertar si faltan funciones esperadas para este rol
                if funciones_faltantes:
                    self._crear_hallazgo(
                        tipo=TipoHallazgoEnum.FUNCIÓN_NO_ASIGNADA,
                        descripcion=f"Al rol '{rol_esperado}' le faltan funciones esperadas: {', '.join(funciones_faltantes)}",
                        gravedad=GravedadEnum.ALTO,
                        rol_afectado=rol_encontrado,
                        recomendación=f"Asignar las funciones faltantes al rol '{rol_esperado}'"
                    )
    
    def _calcular_cumplimiento(self, estructura: EstructuraOrganica) -> float:
        """
        Calcula el porcentaje de cumplimiento.
        
        Fórmula:
            cumplimiento = (requisitos_cumplidos / total_requisitos) * 100
        """
        # Definir requisitos base
        total_requisitos = 0
        requisitos_cumplidos = 0
        
        # Requisito 1: Roles requeridos (peso: 40%)
        total_requisitos += len(self.ROLES_REQUERIDOS) * 4
        roles_estructura = {rol.titulo for rol in estructura.obtener_roles()}
        requisitos_cumplidos += sum(
            4 for rol in self.ROLES_REQUERIDOS if rol in roles_estructura
        )
        
        # Requisito 2: Funciones críticas (peso: 40%)
        funciones_asignadas = self._obtener_todas_funciones(estructura)
        total_requisitos += len(self.FUNCIONES_CRÍTICAS) * 4
        requisitos_cumplidos += sum(
            4 for func in self.FUNCIONES_CRÍTICAS if func in funciones_asignadas
        )
        
        # Requisito 3: Segregación de funciones (peso: 20%)
        total_requisitos += len(self.SEGREGACIÓN_FUNCIONES) * 2
        hallazgos_segregación = [
            h for h in self.hallazgos 
            if h.tipo == TipoHallazgoEnum.SEGREGACIÓN_INADECUADA
        ]
        requisitos_cumplidos += (len(self.SEGREGACIÓN_FUNCIONES) - len(hallazgos_segregación)) * 2
        
        # Evitar división por cero
        if total_requisitos == 0:
            return 0.0
        
        cumplimiento = (requisitos_cumplidos / total_requisitos) * 100
        
        # Limitar entre 0 y 100
        return min(max(cumplimiento, 0.0), 100.0)
    
    def _crear_hallazgo(
        self,
        tipo: TipoHallazgoEnum,
        descripcion: str,
        gravedad: GravedadEnum,
        rol_afectado: Optional[Rol] = None,
        recomendación: str = ""
    ) -> None:
        """
        Crea y registra un nuevo hallazgo.
        
        Evita duplicados verificando que no exista un hallazgo idéntico.
        """
        # Verificar si ya existe un hallazgo similar
        for h in self.hallazgos:
            if (h.tipo == tipo and h.descripcion == descripcion 
                and h.rol_afectado == rol_afectado):
                return  # Evitar duplicado
        
        hallazgo = Hallazgo(
            tipo=tipo,
            descripcion=descripcion,
            gravedad=gravedad,
            rol_afectado=rol_afectado,
            recomendación=recomendación
        )
        self.hallazgos.append(hallazgo)
    
    def _obtener_todas_funciones(self, estructura: EstructuraOrganica) -> set:
        """Retorna el conjunto de todas las funciones asignadas."""
        funciones = set()
        for rol in estructura.obtener_roles():
            funciones.update(rol.obtener_funciones())
        return funciones
    
    def _obtener_fecha_actual(self) -> str:
        """Retorna la fecha actual en formato legible."""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def obtener_recomendaciones(self) -> str:
        """
        Genera un texto con todas las recomendaciones ordenadas por gravedad.
        """
        if not self.hallazgos:
            return "\n✓ No hay hallazgos. La estructura cumple con los estándares.\n"
        
        # Ordenar hallazgos por prioridad
        hallazgos_ordenados = sorted(
            self.hallazgos,
            key=lambda h: h.obtener_prioridad_numérica(),
            reverse=True
        )
        
        recomendaciones = "\n"
        recomendaciones += "="*70 + "\n"
        recomendaciones += "RECOMENDACIONES Y ACCIONES REQUERIDAS\n"
        recomendaciones += "="*70 + "\n\n"
        
        gravedades_procesadas = set()
        
        for hallazgo in hallazgos_ordenados:
            gravedad = hallazgo.gravedad.value
            
            if gravedad not in gravedades_procesadas:
                recomendaciones += f"\n{gravedad}:\n"
                recomendaciones += "-" * 70 + "\n"
                gravedades_procesadas.add(gravedad)
            
            recomendaciones += f"• {hallazgo.descripcion}\n"
            recomendaciones += f"  → {hallazgo.obtener_recomendaciones()}\n\n"
        
        recomendaciones += "="*70 + "\n"
        
        return recomendaciones
    
    def obtener_clasificación_cumplimiento(self, nivel: float) -> str:
        """Retorna la clasificación textual del nivel de cumplimiento."""
        if nivel >= 90:
            return "CUMPLIMIENTO ALTO"
        elif nivel >= 70:
            return "CUMPLIMIENTO MODERADO"
        elif nivel >= 50:
            return "CUMPLIMIENTO BAJO"
        else:
            return "CUMPLIMIENTO CRÍTICO"
    
    # Alias sin acentos
    def obtener_clasificacion_cumplimiento(self, nivel: float) -> str:
        """Alias: obtener_clasificación_cumplimiento sin acentos."""
        return self.obtener_clasificación_cumplimiento(nivel)
