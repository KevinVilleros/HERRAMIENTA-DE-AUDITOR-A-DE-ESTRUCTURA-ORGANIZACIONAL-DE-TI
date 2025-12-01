#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRIPT DE PRUEBA Y DEMOSTRACIÓN (Versión Simplificada)
Demuestra la funcionalidad sin caracteres especiales para compatibilidad con Windows.
"""

from modelos import EstructuraOrganica, Rol, GravedadEnum
from motor_evaluacion import MotorDeEvaluacion
from base_legal import BaseLegal


def prueba_1_estructura_completa():
    """Prueba 1: Estructura bien configurada (Cumplimiento Alto)."""
    print("\n" + "="*70)
    print("PRUEBA 1: ESTRUCTURA ORGANIZACIONAL COMPLETA Y CORRECTA")
    print("="*70 + "\n")
    
    # Crear estructura
    estructura = EstructuraOrganica(
        nombre="Departamento de TI - Empresa XYZ",
        descripcion="Estructura bien configurada segun estandares"
    )
    
    # Crear roles con funciones
    director = Rol("Director de Sistemas de Informacion", "", nivel=1)
    director.agregar_funcion("Planificacion estrategica de TI")
    director.agregar_funcion("Alineacion con negocio")
    director.agregar_funcion("Gestion de riesgos TI")
    estructura.agregar_rol(director)
    
    jefe_ops = Rol("Jefe de Operaciones/Infraestructura", "", nivel=2)
    jefe_ops.agregar_funcion("Gestion de infraestructura")
    jefe_ops.agregar_funcion("Monitoreo de sistemas")
    jefe_ops.agregar_funcion("Disponibilidad de servicios")
    jefe_ops.establecer_supervisor(director)
    estructura.agregar_rol(jefe_ops)
    
    jefe_dev = Rol("Jefe de Desarrollo/Software", "", nivel=2)
    jefe_dev.agregar_funcion("Gestion de proyectos de desarrollo")
    jefe_dev.agregar_funcion("Control de calidad de software")
    jefe_dev.agregar_funcion("Metodologias de desarrollo")
    jefe_dev.agregar_funcion("Gestion de cambios")
    jefe_dev.establecer_supervisor(director)
    estructura.agregar_rol(jefe_dev)
    
    jefe_seguridad = Rol("Jefe de Seguridad Informatica", "", nivel=2)
    jefe_seguridad.agregar_funcion("Gestion de seguridad informatica")
    jefe_seguridad.agregar_funcion("Cumplimiento normativo")
    jefe_seguridad.agregar_funcion("Gestion de incidentes de seguridad")
    jefe_seguridad.agregar_funcion("Auditoria interna de seguridad")
    jefe_seguridad.establecer_supervisor(director)
    estructura.agregar_rol(jefe_seguridad)
    
    dba = Rol("Administrador de Bases de Datos", "", nivel=3)
    dba.agregar_funcion("Gestion de bases de datos")
    dba.agregar_funcion("Backup y recuperacion")
    dba.agregar_funcion("Optimizacion de rendimiento")
    dba.agregar_funcion("Seguridad de datos")
    dba.establecer_supervisor(jefe_ops)
    estructura.agregar_rol(dba)
    
    admin_sistemas = Rol("Administrador de Sistemas/Red", "", nivel=3)
    admin_sistemas.agregar_funcion("Administracion de redes")
    admin_sistemas.agregar_funcion("Gestion de servidores")
    admin_sistemas.agregar_funcion("Configuracion de sistemas")
    admin_sistemas.agregar_funcion("Recuperacion ante desastres")
    admin_sistemas.establecer_supervisor(jefe_ops)
    estructura.agregar_rol(admin_sistemas)
    
    # Evaluar
    motor = MotorDeEvaluacion()
    cumplimiento, hallazgos = motor.evaluar_estructura(estructura)
    
    # Mostrar resultados
    print(estructura.generar_reporte())
    clasificacion = motor.obtener_clasificacion_cumplimiento(cumplimiento)
    print("CLASIFICACION: " + clasificacion + "\n")
    
    if hallazgos:
        print("HALLAZGOS IDENTIFICADOS:")
        print("-"*70)
        for h in hallazgos:
            print("  [" + h.gravedad.value + "] " + h.descripcion)
    else:
        print("[OK] No hay hallazgos. Estructura cumple con estandares.\n")
    
    return cumplimiento, hallazgos


def prueba_2_estructura_deficiente():
    """Prueba 2: Estructura incompleta con brechas (Cumplimiento Bajo)."""
    print("\n" + "="*70)
    print("PRUEBA 2: ESTRUCTURA INCOMPLETA CON BRECHAS")
    print("="*70 + "\n")
    
    # Crear estructura sin algunos roles
    estructura = EstructuraOrganica(
        nombre="Departamento de TI - Empresa ABC",
        descripcion="Estructura con roles faltantes y brechas"
    )
    
    # Solo agregar algunos roles
    director = Rol("Director de Sistemas de Informacion", "", nivel=1)
    director.agregar_funcion("Planificacion estrategica de TI")
    estructura.agregar_rol(director)
    
    # Nota: Falta Jefe de Operaciones, Jefe de Desarrollo, Jefe de Seguridad
    jefe_ops = Rol("Tecnico de Sistemas", "Mal clasificado", nivel=3)
    jefe_ops.agregar_funcion("Operacion basica")
    jefe_ops.establecer_supervisor(director)
    estructura.agregar_rol(jefe_ops)
    
    # Evaluar
    motor = MotorDeEvaluacion()
    cumplimiento, hallazgos = motor.evaluar_estructura(estructura)
    
    # Mostrar resultados
    print(estructura.generar_reporte())
    clasificacion = motor.obtener_clasificacion_cumplimiento(cumplimiento)
    print("CLASIFICACION: " + clasificacion + "\n")
    
    print("HALLAZGOS CRITICOS IDENTIFICADOS:")
    print("-"*70)
    hallazgos_criticos = estructura.obtener_hallazgos_por_gravedad(GravedadEnum.CRÍTICO)
    for i, h in enumerate(hallazgos_criticos, 1):
        print(str(i) + ". " + h.descripcion)
        print("   -> " + h.obtener_recomendaciones() + "\n")
    
    return cumplimiento, hallazgos


def prueba_3_segregacion_inadecuada():
    """Prueba 3: Segregacion de funciones inadecuada."""
    print("\n" + "="*70)
    print("PRUEBA 3: SEGREGACION DE FUNCIONES INADECUADA")
    print("="*70 + "\n")
    
    estructura = EstructuraOrganica(
        nombre="Departamento de TI - Empresa DEF",
        descripcion="Estructura con funciones incompatibles en un rol"
    )
    
    # Crear director
    director = Rol("Director de Sistemas de Informacion", "", nivel=1)
    director.agregar_funcion("Planificacion estrategica de TI")
    director.agregar_funcion("Alineacion con negocio")
    director.agregar_funcion("Gestion de riesgos TI")
    estructura.agregar_rol(director)
    
    # Crear un rol que viole segregacion de funciones
    rol_conflictivo = Rol("Administrador de Cambios", "", nivel=2)
    rol_conflictivo.agregar_funcion("Aprobacion de cambios")  # INCOMPATIBLE CON
    rol_conflictivo.agregar_funcion("Ejecucion de cambios")   # ESTA
    rol_conflictivo.establecer_supervisor(director)
    estructura.agregar_rol(rol_conflictivo)
    
    # Otros roles
    jefe_ops = Rol("Jefe de Operaciones/Infraestructura", "", nivel=2)
    jefe_ops.agregar_funcion("Gestion de infraestructura")
    jefe_ops.agregar_funcion("Monitoreo de sistemas")
    jefe_ops.establecer_supervisor(director)
    estructura.agregar_rol(jefe_ops)
    
    jefe_seguridad = Rol("Jefe de Seguridad Informatica", "", nivel=2)
    jefe_seguridad.agregar_funcion("Gestion de seguridad informatica")
    jefe_seguridad.agregar_funcion("Cumplimiento normativo")
    jefe_seguridad.establecer_supervisor(director)
    estructura.agregar_rol(jefe_seguridad)
    
    # Evaluar
    motor = MotorDeEvaluacion()
    cumplimiento, hallazgos = motor.evaluar_estructura(estructura)
    
    # Mostrar resultados
    print(estructura.generar_reporte())
    clasificacion = motor.obtener_clasificacion_cumplimiento(cumplimiento)
    print("CLASIFICACION: " + clasificacion + "\n")
    
    print("HALLAZGOS DE SEGREGACION:")
    print("-"*70)
    hallazgos_segregacion = [h for h in hallazgos if h.tipo.name == "SEGREGACIÓN_INADECUADA"]
    for i, h in enumerate(hallazgos_segregacion, 1):
        print(str(i) + ". " + h.descripcion)
        print("   Gravedad: " + h.gravedad.value)
        print("   Recomendacion: " + h.obtener_recomendaciones() + "\n")
    
    return cumplimiento, hallazgos


def main():
    """Ejecuta todas las pruebas."""
    print("\n")
    print("="*70)
    print("SCRIPT DE PRUEBA - HERRAMIENTA DE AUDITORIA".center(70))
    print("Estructura Organizacional de Sistemas de Informacion".center(70))
    print("="*70)
    
    # Ejecutar pruebas
    print("\nEjecutando pruebas...")
    cumpl_1, hall_1 = prueba_1_estructura_completa()
    cumpl_2, hall_2 = prueba_2_estructura_deficiente()
    cumpl_3, hall_3 = prueba_3_segregacion_inadecuada()
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS")
    print("="*70 + "\n")
    
    print("Prueba 1 - Estructura Completa:")
    print("  * Cumplimiento: " + str(round(cumpl_1, 2)) + "%")
    print("  * Hallazgos: " + str(len(hall_1)))
    estado1 = "[OK] APROBADA" if cumpl_1 >= 90 else "[!] REQUIERE MEJORAS"
    print("  * Estado: " + estado1 + "\n")
    
    print("Prueba 2 - Estructura Deficiente:")
    print("  * Cumplimiento: " + str(round(cumpl_2, 2)) + "%")
    print("  * Hallazgos: " + str(len(hall_2)))
    estado2 = "[OK] APROBADA" if cumpl_2 >= 90 else "[!] REQUIERE MEJORAS"
    print("  * Estado: " + estado2 + "\n")
    
    print("Prueba 3 - Segregacion Inadecuada:")
    print("  * Cumplimiento: " + str(round(cumpl_3, 2)) + "%")
    print("  * Hallazgos: " + str(len(hall_3)))
    estado3 = "[OK] APROBADA" if cumpl_3 >= 90 else "[!] REQUIERE MEJORAS"
    print("  * Estado: " + estado3 + "\n")
    
    print("="*70)
    print("\n[OK] Todas las pruebas completadas exitosamente.")
    print("\nPara usar la interfaz interactiva, ejecute: python main.py\n")


if __name__ == "__main__":
    main()
