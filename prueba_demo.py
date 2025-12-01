#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SCRIPT DE PRUEBA Y DEMOSTRACIÓN
Demuestra la funcionalidad del sistema de auditoría sin interfaz interactiva.
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
        descripcion="Estructura bien configurada según estándares"
    )
    
    # Crear roles con funciones
    director = Rol("Director de Sistemas de Información", "", nivel=1)
    director.agregar_función("Planificación estratégica de TI")
    director.agregar_función("Alineación con negocio")
    director.agregar_función("Gestión de riesgos TI")
    estructura.agregar_rol(director)
    
    jefe_ops = Rol("Jefe de Operaciones/Infraestructura", "", nivel=2)
    jefe_ops.agregar_función("Gestión de infraestructura")
    jefe_ops.agregar_función("Monitoreo de sistemas")
    jefe_ops.agregar_función("Disponibilidad de servicios")
    jefe_ops.establecer_supervisor(director)
    estructura.agregar_rol(jefe_ops)
    
    jefe_dev = Rol("Jefe de Desarrollo/Software", "", nivel=2)
    jefe_dev.agregar_función("Gestión de proyectos de desarrollo")
    jefe_dev.agregar_función("Control de calidad de software")
    jefe_dev.agregar_función("Metodologías de desarrollo")
    jefe_dev.agregar_función("Gestión de cambios")
    jefe_dev.establecer_supervisor(director)
    estructura.agregar_rol(jefe_dev)
    
    jefe_seguridad = Rol("Jefe de Seguridad Informática", "", nivel=2)
    jefe_seguridad.agregar_función("Gestión de seguridad informática")
    jefe_seguridad.agregar_función("Cumplimiento normativo")
    jefe_seguridad.agregar_función("Gestión de incidentes de seguridad")
    jefe_seguridad.agregar_función("Auditoría interna de seguridad")
    jefe_seguridad.establecer_supervisor(director)
    estructura.agregar_rol(jefe_seguridad)
    
    dba = Rol("Administrador de Bases de Datos", "", nivel=3)
    dba.agregar_función("Gestión de bases de datos")
    dba.agregar_función("Backup y recuperación")
    dba.agregar_función("Optimización de rendimiento")
    dba.agregar_función("Seguridad de datos")
    dba.establecer_supervisor(jefe_ops)
    estructura.agregar_rol(dba)
    
    admin_sistemas = Rol("Administrador de Sistemas/Red", "", nivel=3)
    admin_sistemas.agregar_función("Administración de redes")
    admin_sistemas.agregar_función("Gestión de servidores")
    admin_sistemas.agregar_función("Configuración de sistemas")
    admin_sistemas.agregar_función("Recuperación ante desastres")
    admin_sistemas.establecer_supervisor(jefe_ops)
    estructura.agregar_rol(admin_sistemas)
    
    # Evaluar
    motor = MotorDeEvaluacion()
    cumplimiento, hallazgos = motor.evaluar_estructura(estructura)
    
    # Mostrar resultados
    print(estructura.generar_reporte())
    clasificación = motor.obtener_clasificación_cumplimiento(cumplimiento)
    print(f"CLASIFICACIÓN: {clasificación}\n")
    
    if hallazgos:
        print("HALLAZGOS IDENTIFICADOS:")
        print("-"*70)
        for h in hallazgos:
            print(f"  [{h.gravedad.value}] {h.descripcion}")
    else:
        print("✓ No hay hallazgos. Estructura cumple con estándares.\n")
    
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
    director = Rol("Director de Sistemas de Información", "", nivel=1)
    director.agregar_función("Planificación estratégica de TI")
    estructura.agregar_rol(director)
    
    # Nota: Falta Jefe de Operaciones, Jefe de Desarrollo, Jefe de Seguridad
    jefe_ops = Rol("Técnico de Sistemas", "Mal clasificado", nivel=3)
    jefe_ops.agregar_función("Operación básica")
    jefe_ops.establecer_supervisor(director)
    estructura.agregar_rol(jefe_ops)
    
    # Evaluar
    motor = MotorDeEvaluacion()
    cumplimiento, hallazgos = motor.evaluar_estructura(estructura)
    
    # Mostrar resultados
    print(estructura.generar_reporte())
    clasificación = motor.obtener_clasificación_cumplimiento(cumplimiento)
    print(f"CLASIFICACIÓN: {clasificación}\n")
    
    print("HALLAZGOS CRÍTICOS IDENTIFICADOS:")
    print("-"*70)
    hallazgos_críticos = estructura.obtener_hallazgos_por_gravedad(GravedadEnum.CRÍTICO)
    for i, h in enumerate(hallazgos_críticos, 1):
        print(f"{i}. {h.descripcion}")
        print(f"   → {h.obtener_recomendaciones()}\n")
    
    return cumplimiento, hallazgos


def prueba_3_segregacion_inadecuada():
    """Prueba 3: Segregación de funciones inadecuada."""
    print("\n" + "="*70)
    print("PRUEBA 3: SEGREGACIÓN DE FUNCIONES INADECUADA")
    print("="*70 + "\n")
    
    estructura = EstructuraOrganica(
        nombre="Departamento de TI - Empresa DEF",
        descripcion="Estructura con funciones incompatibles en un rol"
    )
    
    # Crear director
    director = Rol("Director de Sistemas de Información", "", nivel=1)
    director.agregar_función("Planificación estratégica de TI")
    director.agregar_función("Alineación con negocio")
    director.agregar_función("Gestión de riesgos TI")
    estructura.agregar_rol(director)
    
    # Crear un rol que viole segregación de funciones
    rol_conflictivo = Rol("Administrador de Cambios", "", nivel=2)
    rol_conflictivo.agregar_función("Aprobación de cambios")  # INCOMPATIBLE CON
    rol_conflictivo.agregar_función("Ejecución de cambios")   # ESTA
    rol_conflictivo.establecer_supervisor(director)
    estructura.agregar_rol(rol_conflictivo)
    
    # Otros roles
    jefe_ops = Rol("Jefe de Operaciones/Infraestructura", "", nivel=2)
    jefe_ops.agregar_función("Gestión de infraestructura")
    jefe_ops.agregar_función("Monitoreo de sistemas")
    jefe_ops.establecer_supervisor(director)
    estructura.agregar_rol(jefe_ops)
    
    jefe_seguridad = Rol("Jefe de Seguridad Informática", "", nivel=2)
    jefe_seguridad.agregar_función("Gestión de seguridad informática")
    jefe_seguridad.agregar_función("Cumplimiento normativo")
    jefe_seguridad.establecer_supervisor(director)
    estructura.agregar_rol(jefe_seguridad)
    
    # Evaluar
    motor = MotorDeEvaluacion()
    cumplimiento, hallazgos = motor.evaluar_estructura(estructura)
    
    # Mostrar resultados
    print(estructura.generar_reporte())
    clasificación = motor.obtener_clasificación_cumplimiento(cumplimiento)
    print(f"CLASIFICACIÓN: {clasificación}\n")
    
    print("HALLAZGOS DE SEGREGACIÓN:")
    print("-"*70)
    hallazgos_segregación = [h for h in hallazgos if h.tipo.name == "SEGREGACIÓN_INADECUADA"]
    for i, h in enumerate(hallazgos_segregación, 1):
        print(f"{i}. {h.descripcion}")
        print(f"   Gravedad: {h.gravedad.value}")
        print(f"   Recomendación: {h.obtener_recomendaciones()}\n")
    
    return cumplimiento, hallazgos


def mostrar_resumen_base_legal():
    """Muestra un resumen de la base legal."""
    print("\n" + "="*70)
    print("RESUMEN DE BASE LEGAL Y NORMATIVA")
    print("="*70)
    print(BaseLegal.obtener_resumen_base_legal())


def main():
    """Ejecuta todas las pruebas."""
    print("\n")
    print("="*70)
    print("SCRIPT DE PRUEBA - HERRAMIENTA DE AUDITORÍA".center(70))
    print("Estructura Organizacional de Sistemas de Información".center(70))
    print("="*70)
    
    # Ejecutar pruebas
    cumpl_1, hall_1 = prueba_1_estructura_completa()
    cumpl_2, hall_2 = prueba_2_estructura_deficiente()
    cumpl_3, hall_3 = prueba_3_segregacion_inadecuada()
    mostrar_resumen_base_legal()
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS")
    print("="*70 + "\n")
    
    print("Prueba 1 - Estructura Completa:")
    print(f"  • Cumplimiento: {cumpl_1:.2f}%")
    print(f"  • Hallazgos: {len(hall_1)}")
    print(f"  • Estado: {'✓ APROBADA' if cumpl_1 >= 90 else '✗ REQUIERE MEJORAS'}\n")
    
    print("Prueba 2 - Estructura Deficiente:")
    print(f"  • Cumplimiento: {cumpl_2:.2f}%")
    print(f"  • Hallazgos: {len(hall_2)}")
    print(f"  • Estado: {'✓ APROBADA' if cumpl_2 >= 90 else '✗ REQUIERE MEJORAS'}\n")
    
    print("Prueba 3 - Segregación Inadecuada:")
    print(f"  • Cumplimiento: {cumpl_3:.2f}%")
    print(f"  • Hallazgos: {len(hall_3)}")
    print(f"  • Estado: {'✓ APROBADA' if cumpl_3 >= 90 else '✗ REQUIERE MEJORAS'}\n")
    
    print("="*70)
    print("\n✓ Todas las pruebas completadas exitosamente.")
    print("\nPara usar la interfaz interactiva, ejecute: python main.py\n")


if __name__ == "__main__":
    main()
