#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HERRAMIENTA DE AUDITORÍA - ESTRUCTURA ORGANIZACIONAL DE TI
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║  Software para evaluación de la Estructura Orgánica del Área de       ║
║  Sistemas de Información (SI) en una Organización                    ║
║                                                                        ║
║  FUNCIONALIDAD:                                                       ║
║  • Ingreso de estructura organizacional (organigrama)                ║
║  • Ingreso de funciones y responsabilidades                          ║
║  • Comparación con estándares (ITIL, ISO 27001, COBIT)              ║
║  • Identificación de brechas (Gaps Analysis)                        ║
║  • Cálculo de cumplimiento (Compliance Score)                       ║
║  • Generación de reportes con hallazgos y recomendaciones           ║
║  • Consulta de base legal y normativa                               ║
║                                                                        ║
║  COMPONENTES:                                                        ║
║  1. modelos.py - Clases de datos (Rol, Hallazgo, Estructura)       ║
║  2. motor_evaluacion.py - Lógica de auditoría                      ║
║  3. base_legal.py - Documentación normativa                        ║
║  4. interfaz.py - Interfaz de usuario (menú)                       ║
║  5. main.py - Punto de entrada del programa (este archivo)         ║
║                                                                        ║
║  AUTOR: Sistema de Auditoría Informática                            ║
║  VERSIÓN: 1.0                                                        ║
║  LENGUAJE: Python 3.7+                                              ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
"""

from interfaz import InterfazUsuario


def main():
    """
    Función principal del programa.
    
    Inicializa la interfaz de usuario y comienza la ejecución.
    """
    interfaz = InterfazUsuario()
    interfaz.ejecutar()


if __name__ == "__main__":
    main()
