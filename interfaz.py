"""
MÓDULO DE INTERFAZ DE USUARIO
Implementa el menú interactivo de consola para la herramienta de auditoría.

Menú principal con opciones:
1. Ingresar Estructura Organizacional
2. Evaluar Estructura
3. Generar Reporte
4. Consultar Base Legal/Ayuda
5. Salir
"""

from typing import Optional
from modelos import EstructuraOrganica, Rol, GravedadEnum
from motor_evaluacion import MotorDeEvaluacion
from base_legal import BaseLegal
import os
import sys


class InterfazUsuario:
    """
    Gestiona la interfaz de usuario y navegación del sistema.
    """
    
    def __init__(self):
        """Inicializa la interfaz de usuario."""
        self.estructura: Optional[EstructuraOrganica] = None
        self.motor = MotorDeEvaluacion()
        self.evaluado = False
    
    def limpiar_pantalla(self) -> None:
        """Limpia la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pausar(self) -> None:
        """Pausa la ejecución hasta que el usuario presione Enter."""
        input("\nPresione Enter para continuar...")
    
    def mostrar_encabezado(self) -> None:
        """Muestra el encabezado principal del sistema."""
        print("\n")
        print("╔" + "═"*68 + "╗")
        print("║" + " "*68 + "║")
        print("║" + "  HERRAMIENTA DE AUDITORÍA - ESTRUCTURA ORGANIZACIONAL".center(68) + "║")
        print("║" + "  ÁREA DE SISTEMAS DE INFORMACIÓN (SI)".center(68) + "║")
        print("║" + " "*68 + "║")
        print("╚" + "═"*68 + "╝")
        print()
    
    def mostrar_menú_principal(self) -> None:
        """Muestra el menú principal."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        
        if self.estructura:
            print(f"► ESTRUCTURA ACTUAL: {self.estructura.nombre}")
            print(f"  - Roles: {len(self.estructura.roles)}")
            print(f"  - Estado: {'Evaluada' if self.evaluado else 'Sin evaluar'}")
            if self.evaluado:
                print(f"  - Cumplimiento: {self.estructura.nivel_cumplimiento:.2f}%")
            print()
        
        print("OPCIONES DEL MENÚ:")
        print("─" * 70)
        print("  1) Crear/Editar Estructura Organizacional")
        print("  2) Ingresar o Editar Roles y Funciones")
        print("  3) Evaluar Estructura (Auditoría)")
        print("  4) Generar Reporte Completo")
        print("  5) Consultar Base Legal y Normativa")
        print("  6) Ver Datos de Ejemplo (Demo)")
        print("  0) Salir del Sistema")
        print("─" * 70)
    
    def menú_principal(self) -> bool:
        """
        Menú principal del sistema.
        
        Retorna:
            False si el usuario elige salir, True en caso contrario
        """
        self.mostrar_menú_principal()
        
        opción = input("Seleccione una opción (0-6): ").strip()
        
        if opción == "0":
            return False
        elif opción == "1":
            self.crear_estructura()
        elif opción == "2":
            self.gestionar_roles()
        elif opción == "3":
            self.evaluar_estructura()
        elif opción == "4":
            self.generar_reporte()
        elif opción == "5":
            self.mostrar_base_legal()
        elif opción == "6":
            self.cargar_demo()
        else:
            print("\n✗ Opción inválida. Intente nuevamente.")
            self.pausar()
        
        return True
    
    def crear_estructura(self) -> None:
        """Permite al usuario crear una nueva estructura organizacional."""
        self.limpiar_pantalla()
        print("\n╔════════════════════════════════════════════════════════════════════════╗")
        print("║              CREAR NUEVA ESTRUCTURA ORGANIZACIONAL                     ║")
        print("╚════════════════════════════════════════════════════════════════════════╝\n")
        
        nombre = input("Ingrese el nombre de la organización/departamento: ").strip()
        if not nombre:
            print("✗ El nombre no puede estar vacío.")
            self.pausar()
            return
        
        descripcion = input("Ingrese una descripción breve (opcional): ").strip()
        
        self.estructura = EstructuraOrganica(nombre, descripcion)
        self.evaluado = False
        
        print(f"\n✓ Estructura '{nombre}' creada exitosamente.")
        print("\nAhora puede agregar roles a la estructura.")
        self.pausar()
    
    def gestionar_roles(self) -> None:
        """Menú para agregar y editar roles."""
        if not self.estructura:
            print("\n✗ Primero debe crear una estructura organizacional.")
            self.pausar()
            return
        
        while True:
            self.limpiar_pantalla()
            print("\n╔════════════════════════════════════════════════════════════════════════╗")
            print("║                    GESTIÓN DE ROLES Y FUNCIONES                       ║")
            print("╚════════════════════════════════════════════════════════════════════════╝\n")
            
            print(f"Estructura: {self.estructura.nombre}\n")
            
            roles = self.estructura.obtener_roles()
            if roles:
                print("ROLES ACTUALES:")
                print("─" * 70)
                for i, rol in enumerate(roles, 1):
                    supervisor = rol.reporta_a.titulo if rol.reporta_a else "Ninguno"
                    print(f"  {i}. {rol.titulo} (Nivel {rol.nivel}, Supervisor: {supervisor})")
                    if rol.funciones:
                        for func in rol.funciones:
                            print(f"     • {func}")
                print()
            
            print("OPCIONES:")
            print("─" * 70)
            print("  1) Agregar un nuevo rol")
            print("  2) Editar funciones de un rol")
            print("  3) Establecer supervisor de un rol")
            print("  4) Eliminar un rol")
            print("  0) Volver al menú principal")
            print("─" * 70)
            
            opción = input("Seleccione una opción (0-4): ").strip()
            
            if opción == "0":
                break
            elif opción == "1":
                self.agregar_rol()
            elif opción == "2":
                self.editar_funciones_rol()
            elif opción == "3":
                self.establecer_supervisor()
            elif opción == "4":
                self.eliminar_rol()
            else:
                print("\n✗ Opción inválida.")
                self.pausar()
    
    def agregar_rol(self) -> None:
        """Agrega un nuevo rol a la estructura."""
        print("\n" + "─"*70)
        print("AGREGAR NUEVO ROL")
        print("─"*70)
        
        titulo = input("Título del rol (ej: 'Director de SI'): ").strip()
        if not titulo:
            print("✗ El título no puede estar vacío.")
            self.pausar()
            return
        
        descripcion = input("Descripción breve del rol (opcional): ").strip()
        
        nivel_str = input("Nivel jerárquico (1=Director, 2=Jefe, 3=Especialista, default=1): ").strip()
        try:
            nivel = int(nivel_str) if nivel_str else 1
        except ValueError:
            nivel = 1
        
        rol = Rol(titulo, descripcion, nivel)
        self.estructura.agregar_rol(rol)
        
        print(f"\n✓ Rol '{titulo}' agregado exitosamente.")
        self.pausar()
    
    def editar_funciones_rol(self) -> None:
        """Edita las funciones de un rol existente."""
        roles = self.estructura.obtener_roles()
        if not roles:
            print("\n✗ No hay roles para editar.")
            self.pausar()
            return
        
        print("\n" + "─"*70)
        print("EDITAR FUNCIONES DE UN ROL")
        print("─"*70)
        
        for i, rol in enumerate(roles, 1):
            print(f"  {i}. {rol.titulo}")
        
        try:
            índice = int(input("\nSeleccione el número del rol: ").strip()) - 1
            if 0 <= índice < len(roles):
                rol = roles[índice]
            else:
                print("✗ Opción inválida.")
                self.pausar()
                return
        except ValueError:
            print("✗ Ingrese un número válido.")
            self.pausar()
            return
        
        print(f"\nROL: {rol.titulo}")
        print("Funciones actuales:")
        if rol.funciones:
            for i, func in enumerate(rol.funciones, 1):
                print(f"  {i}. {func}")
        else:
            print("  (Sin funciones asignadas)")
        
        print("\nOPCIONES:")
        print("  1) Agregar función")
        print("  2) Eliminar función")
        print("  0) Volver")
        
        opción = input("\nSeleccione una opción (0-2): ").strip()
        
        if opción == "1":
            función = input("Ingrese la función a agregar: ").strip()
            if función:
                rol.agregar_función(función)
                print(f"✓ Función '{función}' agregada.")
        elif opción == "2":
            if rol.funciones:
                for i, func in enumerate(rol.funciones, 1):
                    print(f"  {i}. {func}")
                try:
                    idx = int(input("Seleccione el número de la función a eliminar: ").strip()) - 1
                    if 0 <= idx < len(rol.funciones):
                        función_eliminada = rol.funciones[idx]
                        rol.eliminar_función(función_eliminada)
                        print(f"✓ Función '{función_eliminada}' eliminada.")
                    else:
                        print("✗ Opción inválida.")
                except ValueError:
                    print("✗ Ingrese un número válido.")
        
        self.pausar()
    
    def establecer_supervisor(self) -> None:
        """Establece el supervisor de un rol."""
        roles = self.estructura.obtener_roles()
        if not roles:
            print("\n✗ No hay roles para asignar supervisor.")
            self.pausar()
            return
        
        print("\n" + "─"*70)
        print("ESTABLECER SUPERVISOR DE UN ROL")
        print("─"*70)
        
        print("Roles disponibles:")
        for i, rol in enumerate(roles, 1):
            supervisor = rol.reporta_a.titulo if rol.reporta_a else "Ninguno"
            print(f"  {i}. {rol.titulo} (Supervisor actual: {supervisor})")
        
        try:
            idx_rol = int(input("\nSeleccione el rol a asignar supervisor (número): ").strip()) - 1
            if not (0 <= idx_rol < len(roles)):
                print("✗ Opción inválida.")
                self.pausar()
                return
            
            rol = roles[idx_rol]
            
            print(f"\nRol seleccionado: {rol.titulo}")
            print("\nPosibles supervisores:")
            supervisores = [r for r in roles if r != rol]
            for i, supervisor in enumerate(supervisores, 1):
                print(f"  {i}. {supervisor.titulo}")
            print("  0. Ninguno (rol sin supervisor)")
            
            idx_supervisor = int(input("\nSeleccione el supervisor (número): ").strip())
            
            if idx_supervisor == 0:
                rol.establecer_supervisor(None)
                print(f"✓ Supervisor removido de '{rol.titulo}'.")
            elif 1 <= idx_supervisor <= len(supervisores):
                supervisor = supervisores[idx_supervisor - 1]
                rol.establecer_supervisor(supervisor)
                print(f"✓ '{rol.titulo}' ahora reporta a '{supervisor.titulo}'.")
            else:
                print("✗ Opción inválida.")
        
        except ValueError:
            print("✗ Ingrese un número válido.")
        
        self.pausar()
    
    def eliminar_rol(self) -> None:
        """Elimina un rol de la estructura."""
        roles = self.estructura.obtener_roles()
        if not roles:
            print("\n✗ No hay roles para eliminar.")
            self.pausar()
            return
        
        print("\n" + "─"*70)
        for i, rol in enumerate(roles, 1):
            print(f"  {i}. {rol.titulo}")
        
        try:
            idx = int(input("\nSeleccione el rol a eliminar (número): ").strip()) - 1
            if 0 <= idx < len(roles):
                rol = roles[idx]
                self.estructura.eliminar_rol(rol.titulo)
                print(f"✓ Rol '{rol.titulo}' eliminado.")
            else:
                print("✗ Opción inválida.")
        except ValueError:
            print("✗ Ingrese un número válido.")
        
        self.pausar()
    
    def evaluar_estructura(self) -> None:
        """Ejecuta la evaluación de auditoría."""
        if not self.estructura:
            print("\n✗ Primero debe crear una estructura organizacional.")
            self.pausar()
            return
        
        if not self.estructura.obtener_roles():
            print("\n✗ La estructura no tiene roles. Agregue roles antes de evaluar.")
            self.pausar()
            return
        
        print("\n" + "═"*70)
        print("REALIZANDO AUDITORÍA DE ESTRUCTURA ORGANIZACIONAL...")
        print("═"*70 + "\n")
        
        # Ejecutar evaluación
        cumplimiento, hallazgos = self.motor.evaluar_estructura(self.estructura)
        self.evaluado = True
        
        # Mostrar resultados
        print(self.estructura.generar_reporte())
        
        clasificación = self.motor.obtener_clasificación_cumplimiento(cumplimiento)
        print(f"CLASIFICACIÓN: {clasificación}\n")
        
        conteos = self.estructura.contar_hallazgos_por_gravedad()
        print(f"HALLAZGOS IDENTIFICADOS: {len(hallazgos)}")
        print(f"  • Críticos: {conteos['CRÍTICO']}")
        print(f"  • Altos: {conteos['ALTO']}")
        print(f"  • Medios: {conteos['MEDIO']}")
        print(f"  • Bajos: {conteos['BAJO']}\n")
        
        print("═"*70)
        self.pausar()
    
    def generar_reporte(self) -> None:
        """Genera y muestra el reporte completo."""
        if not self.estructura:
            print("\n✗ No hay estructura para reportar.")
            self.pausar()
            return
        
        if not self.evaluado:
            print("\n✗ Primero debe evaluar la estructura.")
            self.pausar()
            return
        
        self.limpiar_pantalla()
        
        # Reporte de estructura
        print(self.estructura.generar_reporte())
        
        # Hallazgos por gravedad
        print("\nDETALLE DE HALLAZGOS:")
        print("="*70)
        
        hallazgos_por_gravedad = {
            "CRÍTICO": self.estructura.obtener_hallazgos_por_gravedad(GravedadEnum.CRÍTICO),
            "ALTO": self.estructura.obtener_hallazgos_por_gravedad(GravedadEnum.ALTO),
            "MEDIO": self.estructura.obtener_hallazgos_por_gravedad(GravedadEnum.MEDIO),
            "BAJO": self.estructura.obtener_hallazgos_por_gravedad(GravedadEnum.BAJO),
        }
        
        for gravedad, hallazgos in hallazgos_por_gravedad.items():
            if hallazgos:
                print(f"\n{gravedad}:")
                print("-" * 70)
                for i, h in enumerate(hallazgos, 1):
                    print(f"{i}. {h.descripcion}")
                    if h.rol_afectado:
                        print(f"   Rol afectado: {h.rol_afectado.titulo}")
                    print()
        
        # Recomendaciones
        print(self.motor.obtener_recomendaciones())
        
        # Estructura de roles
        print("\nESTRUCTURA ACTUAL DE ROLES:")
        print("="*70)
        for rol in self.estructura.obtener_roles():
            supervisor = f" → {rol.reporta_a.titulo}" if rol.reporta_a else ""
            print(f"  {rol.titulo} (Nivel {rol.nivel}){supervisor}")
            if rol.funciones:
                for func in rol.funciones:
                    print(f"    • {func}")
        
        print("\n" + "="*70)
        self.pausar()
    
    def mostrar_base_legal(self) -> None:
        """Muestra la base legal y normativa."""
        self.limpiar_pantalla()
        
        print("\n╔════════════════════════════════════════════════════════════════════════╗")
        print("║                  BASE LEGAL Y NORMATIVA - AYUDA                        ║")
        print("╚════════════════════════════════════════════════════════════════════════╝\n")
        
        print("OPCIONES:")
        print("─" * 70)
        print("  1) Ver Resumen de Base Legal")
        print("  2) Ver Documentos Legales Completos")
        print("  0) Volver al menú principal")
        print("─" * 70)
        
        opción = input("\nSeleccione una opción (0-2): ").strip()
        
        self.limpiar_pantalla()
        
        if opción == "1":
            print(BaseLegal.obtener_resumen_base_legal())
        elif opción == "2":
            print(BaseLegal.mostrar_base_legal())
        elif opción == "0":
            return
        else:
            print("\n✗ Opción inválida.")
        
        self.pausar()
    
    def cargar_demo(self) -> None:
        """Carga una estructura de ejemplo para demostración."""
        print("\n" + "─"*70)
        print("CARGANDO DATOS DE DEMOSTRACIÓN...")
        print("─"*70 + "\n")
        
        # Crear estructura
        self.estructura = EstructuraOrganica(
            nombre="Departamento de Sistemas - Empresa XYZ",
            descripcion="Estructura típica de un área de TI en una empresa mediana"
        )
        
        # Crear roles
        director = Rol("Director de Sistemas de Información", "Líder máximo del área", nivel=1)
        director.agregar_función("Planificación estratégica de TI")
        director.agregar_función("Alineación con negocio")
        director.agregar_función("Gestión de riesgos TI")
        director.agregar_función("Gestión presupuestaria")
        self.estructura.agregar_rol(director)
        
        jefe_ops = Rol("Jefe de Operaciones", "Responsable de infraestructura", nivel=2)
        jefe_ops.agregar_función("Gestión de infraestructura")
        jefe_ops.agregar_función("Monitoreo de sistemas")
        jefe_ops.agregar_función("Disponibilidad de servicios")
        jefe_ops.establecer_supervisor(director)
        self.estructura.agregar_rol(jefe_ops)
        
        jefe_desarrollo = Rol("Jefe de Desarrollo", "Responsable de software", nivel=2)
        jefe_desarrollo.agregar_función("Gestión de proyectos de desarrollo")
        jefe_desarrollo.agregar_función("Control de calidad de software")
        jefe_desarrollo.agregar_función("Metodologías de desarrollo")
        jefe_desarrollo.establecer_supervisor(director)
        self.estructura.agregar_rol(jefe_desarrollo)
        
        jefe_seguridad = Rol("Jefe de Seguridad Informática", "Responsable de seguridad", nivel=2)
        jefe_seguridad.agregar_función("Gestión de seguridad informática")
        jefe_seguridad.agregar_función("Cumplimiento normativo")
        jefe_seguridad.agregar_función("Gestión de incidentes de seguridad")
        jefe_seguridad.establecer_supervisor(director)
        self.estructura.agregar_rol(jefe_seguridad)
        
        dba = Rol("Administrador de Bases de Datos", "DBA", nivel=3)
        dba.agregar_función("Gestión de bases de datos")
        dba.agregar_función("Backup y recuperación")
        dba.agregar_función("Optimización de rendimiento")
        dba.establecer_supervisor(jefe_ops)
        self.estructura.agregar_rol(dba)
        
        admin_sistemas = Rol("Administrador de Sistemas/Red", "Sysadmin", nivel=3)
        admin_sistemas.agregar_función("Administración de redes")
        admin_sistemas.agregar_función("Gestión de servidores")
        admin_sistemas.agregar_función("Configuración de sistemas")
        admin_sistemas.establecer_supervisor(jefe_ops)
        self.estructura.agregar_rol(admin_sistemas)
        
        print(f"✓ Estructura de demostración creada: {self.estructura.nombre}")
        print(f"✓ Roles cargados: {len(self.estructura.roles)}")
        print("\nAhora puede evaluar la estructura seleccionando la opción 'Evaluar Estructura'.")
        self.pausar()
    
    def ejecutar(self) -> None:
        """Ejecuta el programa principal."""
        try:
            while self.menú_principal():
                pass
            
            self.limpiar_pantalla()
            print("\n╔════════════════════════════════════════════════════════════════════════╗")
            print("║                                                                        ║")
            print("║              ¡Gracias por usar la herramienta de auditoría!           ║")
            print("║                                                                        ║")
            print("║                        FIN DEL PROGRAMA                               ║")
            print("║                                                                        ║")
            print("╚════════════════════════════════════════════════════════════════════════╝\n")
        
        except KeyboardInterrupt:
            print("\n\n✗ Programa interrumpido por el usuario.")
            sys.exit(1)
        except Exception as e:
            print(f"\n✗ Error inesperado: {e}")
            sys.exit(1)
