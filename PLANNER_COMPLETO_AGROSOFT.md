PLANNER COMPLETO - PROYECTO AGROSOFT
Sistema de Recomendaciones Agrícolas para la Sabana Occidental

═══════════════════════════════════════════════════════════════════════════════

INFORMACIÓN GENERAL

Proyecto: AgroSoft - Sistema de Recomendaciones Agrícolas
Inicio: Lunes 12 de Agosto de 2025
Finalización: Martes 26 de Agosto de 2025
Duración: 2.5 semanas (3 Sprints)
Metodología: Scrum Framework

EQUIPO SCRUM:
• Scrum Master: Angel Barrios (RamaAngel)
• Product Owner: Profesor [Nombre]
• Development Team: Juan David Pinto, Anna, Juan Esteban, Jacks

═══════════════════════════════════════════════════════════════════════════════

SPRINT 1: "FUNDACIÓN SEGURA"
Fechas: 12-16 Agosto 2025 (5 días)
Sprint Goal: "Establecer base sólida con autenticación y gestión de usuarios"

┌─────────────────────────────────────────────────────────────────────────────┐
│                    BACKLOG SPRINT 1: FUNDACIÓN SEGURA                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ TAREA                     │ ASIGNADO A       │ SP │ HORAS │ PRIORIDAD      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Login de Usuario          │ Juan David Pinto │ 8  │ 24h   │ 🔴 Crítica     │
│ Registro de Productores   │ Juan David Pinto │ 5  │ 16h   │ 🔴 Crítica     │
│ Recuperar Contraseña      │ Anna             │ 6  │ 20h   │ 🟡 Media       │
│ Administrar Usuarios      │ Juan Esteban     │ 5  │ 16h   │ 🟡 Media       │
│ Cerrar Sesión Segura      │ Anna + Jacks     │ 3  │ 10h   │ 🟢 Baja        │
│ Facilitación Scrum        │ Angel Barrios    │ - │ 15h   │ 🔴 Crítica     │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TOTAL: 27 SP / 101 HORAS                           │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA DETALLADO SPRINT 1:

📅 LUNES 12 AGOSTO 2025:
□ 09:00-11:00  Sprint Planning "Fundación Segura" (Angel facilita)
               - Definición Sprint Goal
               - Estimación con Planning Poker
               - Asignación de tareas del backlog
□ 11:30-13:00  Setup Inicial del Proyecto
               - Configuración Django framework
               - Estructura base de datos SQLite
               - Setup repositorio Git y ramas
□ 14:00-17:00  Configuración Entornos
               - Instalación dependencias
               - Configuración IDE para cada desarrollador
               - Primera sincronización del equipo

📅 MARTES 13 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-12:00  Desarrollo Paralelo Fase 1:
               - Juan David: Estructura login (HU-001)
               - Anna: Formulario recuperación (HU-003)
               - Juan Esteban: Modelos usuarios (HU-004)
               - Jacks: Apoyo en configuración
□ 13:00-17:00  Desarrollo Paralelo Fase 2:
               - Juan David: Validaciones login
               - Anna: Lógica recuperación contraseña
               - Juan Esteban: CRUD usuarios básico

📅 MIÉRCOLES 14 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-11:00  ⚠️ IMPEDIMENTO: Problemas con tokens JWT
               - Investigación de alternativas
               - Decisión técnica del equipo
□ 11:00-14:00  Sesión Resolución Problemas (todo el equipo)
               - Análisis de Django sessions
               - Implementación de solución alternativa
□ 14:00-17:00  Aplicación de Solución
               - Refactoring de autenticación
               - Testing de nueva implementación

📅 JUEVES 15 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-12:00  Finalización Funcionalidades:
               - Juan David: Registro usuarios (HU-002)
               - Anna + Jacks: Logout seguro (HU-005)
               - Juan Esteban: Panel gestión usuarios
□ 13:00-15:00  Testing Individual de Módulos
□ 15:00-17:00  Integración y Testing Conjunto

📅 VIERNES 16 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 10:00-12:00  Testing Final y Corrección de Bugs
□ 13:00-14:30  Sprint Review "Fundación Segura" (Angel facilita)
               - Demo de autenticación completa
               - Validación con Product Owner
□ 15:00-16:00  Sprint Retrospective (Angel facilita)
               - Análisis de impedimentos
               - Mejoras para Sprint 2

═══════════════════════════════════════════════════════════════════════════════

SPRINT 2: "INTELIGENCIA AGRÍCOLA"
Fechas: 19-23 Agosto 2025 (5 días)
Sprint Goal: "Desarrollar el cerebro del sistema con recomendaciones inteligentes"

┌─────────────────────────────────────────────────────────────────────────────┐
│                 BACKLOG SPRINT 2: INTELIGENCIA AGRÍCOLA                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ TAREA                     │ ASIGNADO A       │ SP │ HORAS │ PRIORIDAD      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Motor Recomendaciones     │ Angel Barrios    │ 13 │ 40h   │ 🔴 Crítica     │
│ Algoritmo Rentabilidad    │ Angel Barrios    │ 8  │ 24h   │ 🔴 Crítica     │
│ Integración Clima         │ Angel + Anna     │ 10 │ 28h   │ 🔴 Crítica     │
│ Configurar Municipios     │ Angel Barrios    │ 5  │ 16h   │ 🟡 Media       │
│ Mensajes Contextuales     │ Angel Barrios    │ 5  │ 12h   │ 🟡 Media       │
│ Tendencias de Mercado     │ Anna             │ 8  │ 24h   │ 🔴 Crítica     │
│ Apoyo General Testing     │ Juan David       │ - │ 12h   │ 🟢 Baja        │
│ Apoyo Backend            │ Juan Esteban     │ - │ 14h   │ 🟢 Baja        │
│ Apoyo Testing            │ Jacks            │ - │ 10h   │ 🟢 Baja        │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TOTAL: 49 SP / 180 HORAS                           │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA DETALLADO SPRINT 2:

📅 LUNES 19 AGOSTO 2025:
□ 09:00-11:00  Sprint Planning "Inteligencia Agrícola" (Angel facilita)
□ 11:30-13:00  Investigación Técnica:
               - Angel: Análisis datos SIPSA-DANE
               - Anna: Investigación APIs climáticas
□ 14:00-17:00  Inicio Desarrollo Core:
               - Angel: Estructura motor recomendaciones
               - Anna: Setup integración APIs
               - Otros: Apoyo en investigación

📅 MARTES 20 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-11:00  Angel: Algoritmos rentabilidad básicos
□ 11:00-12:00  ⚠️ IMPEDIMENTO: API clima no responde
               - Análisis de alternativas
               - Decisión de fallbacks
□ 14:00-17:00  Desarrollo con Contingencias:
               - Angel: Continuación algoritmos
               - Anna: Implementación fallbacks clima
               - Equipo: Apoyo en troubleshooting

📅 MIÉRCOLES 21 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-11:00  ⚠️ IMPEDIMENTO: API SIPSA-DANE inconsistente
□ 11:00-17:00  Implementación Datos Híbridos:
               - Angel: Servicio híbrido datos reales + simulados
               - Anna: Integración tendencias con fallback
               - Equipo: Testing de soluciones

📅 JUEVES 22 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-12:00  Trabajo Colaborativo:
               - Angel + Anna: Factor climático (pair programming)
               - Juan David: Testing frontend
               - Juan Esteban: Validación backend
               - Jacks: Testing integración
□ 13:00-17:00  Finalización Funcionalidades:
               - Angel: Municipios + Mensajes contextuales
               - Anna: Tendencias mercado finales
               - Equipo: Testing conjunto

📅 VIERNES 23 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 10:00-12:00  Testing Final Motor Recomendaciones
□ 13:00-15:00  Sprint Review "Inteligencia Agrícola" (Angel facilita)
□ 15:30-17:00  Sprint Retrospective (Angel facilita)

═══════════════════════════════════════════════════════════════════════════════

SPRINT 3: "VISUALIZACIÓN Y DESPLIEGUE"
Fechas: 26-27 Agosto 2025 (2 días)
Sprint Goal: "Completar sistema con reportes visuales y poner en producción"

┌─────────────────────────────────────────────────────────────────────────────┐
│              BACKLOG SPRINT 3: VISUALIZACIÓN Y DESPLIEGUE                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ TAREA                     │ ASIGNADO A       │ SP │ HORAS │ PRIORIDAD      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Panel Reporte Cultivos    │ Juan Esteban     │ 6  │ 10h   │ 🔴 Crítica     │
│ Panel Producción          │ Juan Esteban     │ 6  │ 10h   │ 🔴 Crítica     │
│ Panel Reportes Gráficos   │ Juan Esteban+Jacks│ 8  │ 18h   │ 🔴 Crítica     │
│ Reportes Semanales        │ Juan David Pinto │ 5  │ 12h   │ 🟡 Media       │
│ Gráficas de Productos     │ Anna             │ 5  │ 12h   │ 🟡 Media       │
│ Configuración Hosting     │ Juan Esteban     │ 3  │ 6h    │ 🔴 Crítica     │
│ Despliegue Final          │ Todo el equipo   │ 2  │ 8h    │ 🔴 Crítica     │
│ Facilitación Scrum        │ Angel Barrios    │ - │ 8h    │ 🔴 Crítica     │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TOTAL: 35 SP / 84 HORAS                            │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA DETALLADO SPRINT 3:

📅 LUNES 26 AGOSTO 2025:
□ 09:00-10:00  Sprint Planning "Visualización y Despliegue" (Angel facilita)
□ 10:30-12:00  Desarrollo Intensivo Reportes:
               - Juan Esteban: Panel cultivos (HU-012)
               - Jacks: Apoyo en panel cultivos
               - Juan David: Reportes semanales (HU-015)
               - Anna: Gráficas productos (HU-016)
□ 13:00-14:00  ⚠️ IMPEDIMENTO: Chart.js configuración
□ 14:00-15:30  Resolución Chart.js:
               - Jacks + Anna: Colaboración en gráficas
               - Juan David: Apoyo en debugging
□ 15:30-16:30  ⚠️ IMPEDIMENTO: Conflictos CSS panel admin
□ 16:30-18:00  Reorganización CSS:
               - Juan David: Liderazgo en CSS
               - Juan Esteban: Ajustes panel admin
               - Anna: Validación frontend

📅 MARTES 27 AGOSTO 2025:
□ 09:00-09:15  Daily Standup Final (Angel facilita)
□ 09:30-10:30  ⚠️ IMPEDIMENTO: Errores configuración hosting
□ 10:30-11:30  Resolución Hosting:
               - Juan Esteban: Configuración servidor
               - Jacks: Apoyo en deployment
               - Angel: Supervisión técnica
□ 11:30-13:00  Despliegue Final Exitoso:
               - Todo el equipo: Validación funcionalidades
               - Testing en producción
               - Verificación de URLs y accesos
□ 14:00-15:30  Sprint Review Final (Angel facilita)
               - Demo completa del sistema
               - Validación con stakeholders
□ 16:00-17:00  Sprint Retrospective Final (Angel facilita)
               - Lecciones aprendidas del proyecto
               - Celebración del éxito

═══════════════════════════════════════════════════════════════════════════════

ASIGNACIÓN DETALLADA DE TAREAS

ANGEL BARRIOS (Scrum Master + Backend Principal):
Sprint 1: 15h - Facilitación Scrum Master
• Daily Standups: 5 sesiones × 0.5h = 2.5h
• Sprint Planning: 2h
• Sprint Review: 1.5h
• Sprint Retrospective: 1h
• Resolución impedimentos tokens: 6h
• Coordinación equipo: 2h

Sprint 2: 112h - Desarrollo Core + Facilitación
• Motor Recomendaciones (HU-006): 40h
• Algoritmo Rentabilidad (HU-007): 24h
• Factor Climático con Anna (HU-008): 8h
• Municipios Sabana (HU-009): 16h
• Mensajes Contextuales (HU-010): 12h
• Facilitación Scrum: 12h

Sprint 3: 8h - Facilitación Final
• Sprint Planning: 1h
• Daily Standup: 0.5h
• Sprint Review: 1.5h
• Sprint Retrospective: 1h
• Supervisión despliegue: 4h

TOTAL ANGEL: 135 HORAS

JUAN DAVID PINTO (Frontend Especializado):
Sprint 1: 40h - Frontend Autenticación
• Login de Usuario (HU-001): 24h
• Registro de Productores (HU-002): 16h

Sprint 2: 12h - Apoyo y Testing
• Testing frontend: 8h
• Validación interfaces: 4h

Sprint 3: 18h - Reportes y CSS
• Reportes Semanales (HU-015): 12h
• Resolución conflictos CSS: 4h
• Apoyo en despliegue: 2h

TOTAL JUAN DAVID: 70 HORAS

ANNA (Frontend/Backend Versátil):
Sprint 1: 24h - Autenticación Avanzada
• Recuperar Contraseña (HU-003): 20h
• Cerrar Sesión con Jacks (HU-005): 4h

Sprint 2: 30h - Colaboración Técnica
• Factor Climático con Angel (HU-008): 18h
• Tendencias de Mercado (HU-011): 12h

Sprint 3: 16h - Gráficas y Apoyo
• Gráficas de Productos (HU-016): 12h
• Apoyo resolución Chart.js: 4h

TOTAL ANNA: 70 HORAS

JUAN ESTEBAN (Backend/Panel Admin):
Sprint 1: 18h - Gestión y Setup
• Administrar Usuarios (HU-004): 16h
• Apoyo setup inicial: 2h

Sprint 2: 14h - Apoyo Backend
• Apoyo en backend: 10h
• Testing integración: 4h

Sprint 3: 38h - Panel Admin y Hosting
• Panel Reporte Cultivos (HU-012): 10h
• Panel Producción (HU-013): 10h
• Panel Reportes Gráficos (HU-014): 12h
• Configuración Hosting: 6h

TOTAL JUAN ESTEBAN: 70 HORAS

JACKS (Backend de Apoyo):
Sprint 1: 14h - Apoyo y Testing
• Cerrar Sesión con Anna (HU-005): 6h
• Apoyo configuración: 8h

Sprint 2: 10h - Testing Backend
• Apoyo testing: 6h
• Validación funcionalidades: 4h

Sprint 3: 32h - Panel Admin
• Panel Reportes Gráficos con Juan Esteban: 18h
• Apoyo en otros paneles: 10h
• Apoyo en despliegue: 4h

TOTAL JACKS: 56 HORAS

═══════════════════════════════════════════════════════════════════════════════

RESUMEN EJECUTIVO DEL PLANNER

DISTRIBUCIÓN FINAL DE HORAS:
• Angel Barrios: 135h (33%) - Scrum Master + Core Backend
• Juan David Pinto: 70h (17%) - Frontend Especializado
• Anna: 70h (17%) - Frontend/Backend Versátil
• Juan Esteban: 70h (17%) - Backend/Panel Admin
• Jacks: 56h (14%) - Backend de Apoyo

TOTAL PROYECTO: 401 HORAS HOMBRE

IMPEDIMENTOS GESTIONADOS:
• Sprint 1: Tokens JWT → Django sessions
• Sprint 2: APIs externas → Datos híbridos
• Sprint 3: Chart.js + CSS + Hosting → Colaboración

CEREMONIAS SCRUM FACILITADAS:
• 3 Sprint Planning sessions
• 13 Daily Standups
• 3 Sprint Reviews
• 3 Sprint Retrospectives

RESULTADO: ✓ PROYECTO COMPLETADO EXITOSAMENTE
DESPLIEGUE: ✓ SISTEMA OPERATIVO EN HOSTING
FECHA ENTREGA: 27 de Agosto de 2025
