"""
MÓDULO DE MODELOS - HERRAMIENTA DE AUDITORÍA DE ESTRUCTURA ORGÁNICA
Definición de las clases principales del sistema.

Clases:
- Rol: Representa un puesto o posición en la estructura organizacional
- Hallazgo: Representa un incumplimiento o brecha identificada
- DocumentoLegal: Representa documentos normativos de referencia
- EstructuraOrganica: Contenedor principal de la estructura a evaluar
"""

from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime


class GravedadEnum(Enum):
    """Niveles de gravedad de los hallazgos."""
    CRÍTICO = "CRÍTICO"
    ALTO = "ALTO"
    MEDIO = "MEDIO"
    BAJO = "BAJO"


class TipoHallazgoEnum(Enum):
    """Tipos de hallazgos identificables en la auditoría."""
    ROL_FALTANTE = "ROL_FALTANTE"
    FUNCIÓN_NO_ASIGNADA = "FUNCIÓN_NO_ASIGNADA"
    SEGREGACIÓN_INADECUADA = "SEGREGACIÓN_INADECUADA"
    FUNCIÓN_DUPLICADA = "FUNCIÓN_DUPLICADA"
    SIN_SUPERVISOR = "SIN_SUPERVISOR"
    REPORTES_MÚLTIPLES = "REPORTES_MÚLTIPLES"


class Rol:
    """
    Representa un rol o posición en la estructura organizacional.
    
    Atributos:
        titulo: Nombre del rol (e.g., "Director de SI", "DBA")
        descripcion: Descripción breve del rol
        funciones: Lista de funciones/responsabilidades asignadas
        reporta_a: Referencia al rol supervisor (puede ser None para Director)
        nivel: Nivel jerárquico (1=Director, 2=Jefe, 3=Especialista, etc.)
    """
    
    def __init__(self, titulo: str, descripcion: str = "", nivel: int = 1):
        """Inicializa un nuevo rol."""
        self.titulo = titulo
        self.descripcion = descripcion
        self.funciones: List[str] = []
        self.reporta_a: Optional['Rol'] = None
        self.nivel = nivel
        self.subordinados: List['Rol'] = []
    
    def agregar_función(self, función: str) -> None:
        """Añade una función/responsabilidad al rol."""
        if función not in self.funciones:
            self.funciones.append(función)
    
    # Alias sin acentos para compatibilidad
    def agregar_funcion(self, funcion: str) -> None:
        """Alias: agregar_función sin acentos."""
        self.agregar_función(funcion)
    
    def eliminar_función(self, función: str) -> None:
        """Elimina una función del rol."""
        if función in self.funciones:
            self.funciones.remove(función)
    
    def obtener_funciones(self) -> List[str]:
        """Retorna la lista de funciones asignadas."""
        return self.funciones.copy()
    
    def establecer_supervisor(self, rol_supervisor: Optional['Rol']) -> None:
        """Establece el rol supervisor de este rol."""
        self.reporta_a = rol_supervisor
        if rol_supervisor and self not in rol_supervisor.subordinados:
            rol_supervisor.subordinados.append(self)
    
    def tiene_función(self, función: str) -> bool:
        """Verifica si el rol tiene una función específica."""
        return función in self.funciones
    
    def __str__(self) -> str:
        """Representación en string del rol."""
        return f"{self.titulo} (Nivel {self.nivel})"
    
    def __repr__(self) -> str:
        """Representación detallada del rol."""
        return f"Rol(titulo='{self.titulo}', funciones={len(self.funciones)})"


class Hallazgo:
    """
    Representa un hallazgo de auditoría (brecha, incumplimiento, etc).
    
    Atributos:
        tipo: Tipo de hallazgo (enum TipoHallazgoEnum)
        descripcion: Descripción detallada del hallazgo
        gravedad: Nivel de gravedad (enum GravedadEnum)
        rol_afectado: Rol relacionado con el hallazgo
        recomendación: Sugerencia para remediar el hallazgo
        fecha_identificación: Fecha en que se identificó el hallazgo
    """
    
    def __init__(
        self,
        tipo: TipoHallazgoEnum,
        descripcion: str,
        gravedad: GravedadEnum,
        rol_afectado: Optional[Rol] = None,
        recomendación: str = ""
    ):
        """Inicializa un nuevo hallazgo."""
        self.tipo = tipo
        self.descripcion = descripcion
        self.gravedad = gravedad
        self.rol_afectado = rol_afectado
        self.recomendación = recomendación
        self.fecha_identificación = datetime.now()
    
    def obtener_recomendaciones(self) -> str:
        """Retorna las recomendaciones para remediar el hallazgo."""
        if self.recomendación:
            return self.recomendación
        
        # Generar recomendaciones automáticas según el tipo de hallazgo
        recomendaciones_auto = {
            TipoHallazgoEnum.ROL_FALTANTE: 
                f"Crear el rol '{self.rol_afectado.titulo if self.rol_afectado else 'especificado'}' en la estructura.",
            TipoHallazgoEnum.FUNCIÓN_NO_ASIGNADA:
                f"Asignar la función faltante al rol responsable.",
            TipoHallazgoEnum.SEGREGACIÓN_INADECUADA:
                f"Revisar y segregar las funciones conflictivas en roles diferentes.",
            TipoHallazgoEnum.FUNCIÓN_DUPLICADA:
                f"Consolidar la función en un único rol responsable.",
            TipoHallazgoEnum.SIN_SUPERVISOR:
                f"Asignar un supervisor al rol '{self.rol_afectado.titulo if self.rol_afectado else 'especificado'}'.",
            TipoHallazgoEnum.REPORTES_MÚLTIPLES:
                f"Establecer una cadena de mando clara y única.",
        }
        
        return recomendaciones_auto.get(
            self.tipo,
            "Revisar la configuración del rol."
        )
    
    def obtener_prioridad_numérica(self) -> int:
        """Retorna un número para ordenar por prioridad (mayor = más prioritario)."""
        prioridades = {
            GravedadEnum.CRÍTICO: 4,
            GravedadEnum.ALTO: 3,
            GravedadEnum.MEDIO: 2,
            GravedadEnum.BAJO: 1
        }
        return prioridades.get(self.gravedad, 0)
    
    def __str__(self) -> str:
        """Representación en string del hallazgo."""
        rol_str = f" ({self.rol_afectado})" if self.rol_afectado else ""
        return f"[{self.gravedad.value}] {self.tipo.value}: {self.descripcion}{rol_str}"
    
    def __repr__(self) -> str:
        """Representación detallada del hallazgo."""
        return f"Hallazgo(tipo={self.tipo.name}, gravedad={self.gravedad.name})"


class DocumentoLegal:
    """
    Representa un documento normativo o legal de referencia.
    
    Atributos:
        nombre: Nombre del documento (e.g., "ISO 27001")
        contenido: Descripción o fragmento del contenido
        referencia: URL o referencia bibliográfica
        fecha_publicación: Fecha de publicación del documento
        aplicable: Si es aplicable a la evaluación
    """
    
    def __init__(
        self,
        nombre: str,
        contenido: str,
        referencia: str = "",
        fecha_publicación: str = ""
    ):
        """Inicializa un nuevo documento legal."""
        self.nombre = nombre
        self.contenido = contenido
        self.referencia = referencia
        self.fecha_publicación = fecha_publicación
        self.aplicable = True
    
    def mostrar(self) -> str:
        """Retorna una representación formateada del documento."""
        output = f"\n{'='*70}\n"
        output += f"DOCUMENTO: {self.nombre}\n"
        output += f"{'='*70}\n"
        
        if self.fecha_publicación:
            output += f"Fecha de Publicación: {self.fecha_publicación}\n"
        
        if self.referencia:
            output += f"Referencia: {self.referencia}\n"
        
        output += f"\n{self.contenido}\n"
        output += f"{'='*70}\n"
        
        return output
    
    def __str__(self) -> str:
        """Representación en string del documento."""
        return f"{self.nombre} ({self.referencia})"


class EstructuraOrganica:
    """
    Contenedor principal que representa la estructura organizacional completa.
    
    Atributos:
        nombre: Nombre de la organización o departamento
        descripcion: Descripción de la estructura
        roles: Lista de roles en la estructura
        documentos_legales: Documentos normativos asociados
        nivel_cumplimiento: Porcentaje de cumplimiento (calculado)
        hallazgos: Lista de hallazgos identificados en la evaluación
        fecha_evaluación: Fecha de la última evaluación
    """
    
    def __init__(self, nombre: str, descripcion: str = ""):
        """Inicializa una nueva estructura organizacional."""
        self.nombre = nombre
        self.descripcion = descripcion
        self.roles: List[Rol] = []
        self.documentos_legales: List[DocumentoLegal] = []
        self.nivel_cumplimiento: float = 0.0
        self.hallazgos: List[Hallazgo] = []
        self.fecha_evaluación: Optional[str] = None
    
    def agregar_rol(self, rol: Rol) -> None:
        """Añade un rol a la estructura."""
        if rol not in self.roles:
            self.roles.append(rol)
    
    def eliminar_rol(self, titulo_rol: str) -> bool:
        """Elimina un rol de la estructura por su título."""
        for rol in self.roles:
            if rol.titulo == titulo_rol:
                self.roles.remove(rol)
                return True
        return False
    
    def obtener_rol(self, titulo: str) -> Optional[Rol]:
        """Obtiene un rol por su título."""
        for rol in self.roles:
            if rol.titulo == titulo:
                return rol
        return None
    
    def obtener_roles(self) -> List[Rol]:
        """Retorna la lista de roles."""
        return self.roles.copy()
    
    def agregar_documento_legal(self, documento: DocumentoLegal) -> None:
        """Añade un documento legal/normativo."""
        if documento not in self.documentos_legales:
            self.documentos_legales.append(documento)
    
    def obtener_documentos_legales(self) -> List[DocumentoLegal]:
        """Retorna la lista de documentos legales."""
        return self.documentos_legales.copy()
    
    def agregar_hallazgo(self, hallazgo: Hallazgo) -> None:
        """Añade un hallazgo a la estructura."""
        if hallazgo not in self.hallazgos:
            self.hallazgos.append(hallazgo)
    
    def obtener_hallazgos(self) -> List[Hallazgo]:
        """Retorna la lista de hallazgos."""
        return self.hallazgos.copy()
    
    def obtener_hallazgos_por_gravedad(self, gravedad: GravedadEnum) -> List[Hallazgo]:
        """Retorna hallazgos filtrados por gravedad."""
        return [h for h in self.hallazgos if h.gravedad == gravedad]
    
    def contar_hallazgos_por_gravedad(self) -> Dict[str, int]:
        """Retorna conteo de hallazgos por nivel de gravedad."""
        conteo = {
            "CRÍTICO": len(self.obtener_hallazgos_por_gravedad(GravedadEnum.CRÍTICO)),
            "ALTO": len(self.obtener_hallazgos_por_gravedad(GravedadEnum.ALTO)),
            "MEDIO": len(self.obtener_hallazgos_por_gravedad(GravedadEnum.MEDIO)),
            "BAJO": len(self.obtener_hallazgos_por_gravedad(GravedadEnum.BAJO))
        }
        return conteo
    
    def obtener_total_funciones(self) -> int:
        """Retorna el total de funciones asignadas en todos los roles."""
        return sum(len(rol.funciones) for rol in self.roles)
    
    def generar_reporte(self) -> str:
        """Genera un reporte completo de la estructura y evaluación."""
        reporte = "\n"
        reporte += "="*70 + "\n"
        reporte += "REPORTE DE AUDITORÍA - ESTRUCTURA ORGANIZACIONAL\n"
        reporte += "="*70 + "\n\n"
        
        reporte += f"DEPARTAMENTO: {self.nombre}\n"
        reporte += f"DESCRIPCIÓN: {self.descripcion}\n"
        reporte += f"NIVEL DE CUMPLIMIENTO: {self.nivel_cumplimiento:.2f}%\n"
        reporte += f"FECHA DE EVALUACIÓN: {self.fecha_evaluación or 'No evaluada'}\n"
        reporte += f"TOTAL DE ROLES: {len(self.roles)}\n"
        reporte += f"TOTAL DE FUNCIONES: {self.obtener_total_funciones()}\n"
        reporte += f"TOTAL DE HALLAZGOS: {len(self.hallazgos)}\n\n"
        
        conteos = self.contar_hallazgos_por_gravedad()
        reporte += "DISTRIBUCIÓN DE HALLAZGOS:\n"
        reporte += f"  - Críticos: {conteos['CRÍTICO']}\n"
        reporte += f"  - Altos: {conteos['ALTO']}\n"
        reporte += f"  - Medios: {conteos['MEDIO']}\n"
        reporte += f"  - Bajos: {conteos['BAJO']}\n\n"
        
        reporte += "="*70 + "\n"
        
        return reporte
    
    def __str__(self) -> str:
        """Representación en string de la estructura."""
        return f"Estructura Orgánica: {self.nombre} ({len(self.roles)} roles)"
    
    def __repr__(self) -> str:
        """Representación detallada de la estructura."""
        return f"EstructuraOrganica(nombre='{self.nombre}', roles={len(self.roles)}, hallazgos={len(self.hallazgos)})"
