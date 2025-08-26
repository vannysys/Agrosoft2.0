PLANNER DETALLADO - PROYECTO AGROSOFT
Sistema de Recomendaciones Agrícolas para la Sabana Occidental

═══════════════════════════════════════════════════════════════════════════════

INFORMACIÓN GENERAL DEL PROYECTO

Proyecto: AgroSoft - Sistema de Recomendaciones Agrícolas
Duración: 2.5 semanas (11-26 Agosto 2025)
Metodología: Scrum Framework
Total Story Points: 111 puntos
Total Horas: 422 horas hombre

EQUIPO SCRUM:
• Scrum Master: Angel Barrios (RamaAngel)
• Product Owner: Profesor [Nombre]
• Development Team: Juan David Pinto, Anna, Juan Esteban, Jacks

═══════════════════════════════════════════════════════════════════════════════

SPRINT 1: AUTENTICACIÓN Y GESTIÓN DE USUARIOS
Fechas: 11-15 Agosto 2025 (5 días laborables)
Sprint Goal: "Implementar sistema completo de autenticación y gestión de usuarios"

┌─────────────────────────────────────────────────────────────────────────────┐
│                           SPRINT 1 BACKLOG                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ ID    │ Historia                  │ Responsable      │ SP  │ Horas │ Prior │
├─────────────────────────────────────────────────────────────────────────────┤
│ HU-001│ Login básico              │ Juan David Pinto │ 8   │ 36    │ Alta  │
│ HU-002│ Registro de usuarios      │ Juan David Pinto │ 5   │ 20    │ Alta  │
│ HU-003│ Recuperación contraseña   │ Anna             │ 6   │ 28    │ Media │
│ HU-004│ Gestión de usuarios       │ Juan Esteban     │ 5   │ 20    │ Media │
│ HU-005│ Logout seguro             │ Anna             │ 3   │ 12    │ Baja  │
│ SM    │ Facilitación Scrum        │ Angel Barrios    │ -   │ 25    │ Alta  │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TOTAL: 27 SP / 141 HORAS                           │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA DETALLADO SPRINT 1:

LUNES 11 AGOSTO 2025:
□ 09:00-12:00  Sprint Planning Meeting (Angel facilita)
               - Refinamiento Product Backlog
               - Estimación con Planning Poker
               - Definición Sprint Goal
               - Asignación de historias
□ 13:00-15:00  Setup inicial proyecto
               - Configuración Django
               - Estructura base de datos
               - Setup repositorio Git
□ 15:00-17:00  Configuración entornos desarrollo

MARTES 12 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-12:00  Desarrollo paralelo:
               - Juan David: Login básico (HU-001)
               - Anna: Recuperación contraseña (HU-003)
               - Juan Esteban: Gestión usuarios (HU-004)
□ 13:00-17:00  Continuación desarrollo
               - Juan David: Registro usuarios (HU-002)
               - Anna: Logout seguro (HU-005)

MIÉRCOLES 13 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-11:00  ⚠️ IMPEDIMENTO: Problemas tokens JWT
□ 11:00-14:00  Sesión resolución problemas (todo el equipo)
               - Investigación alternativas
               - Decisión: Django sessions
□ 14:00-17:00  Implementación solución alternativa

JUEVES 14 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-12:00  Resolución final autenticación
□ 13:00-15:00  Testing funcionalidades individuales
□ 15:00-17:00  Integración módulos y testing conjunto

VIERNES 15 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 10:00-13:00  Testing final y corrección bugs
□ 14:00-15:30  Sprint Review (Angel facilita)
               - Demo de funcionalidades
               - Feedback stakeholders
□ 16:00-17:00  Sprint Retrospective (Angel facilita)

═══════════════════════════════════════════════════════════════════════════════

SPRINT 2: SISTEMA DE RECOMENDACIONES
Fechas: 18-22 Agosto 2025 (5 días laborables)
Sprint Goal: "Desarrollar motor de recomendaciones con análisis multifactorial"

┌─────────────────────────────────────────────────────────────────────────────┐
│                           SPRINT 2 BACKLOG                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ ID    │ Historia                  │ Responsable      │ SP  │ Horas │ Prior │
├─────────────────────────────────────────────────────────────────────────────┤
│ HU-006│ Recomendaciones básicas   │ Angel Barrios    │ 13  │ 45    │ Alta  │
│ HU-007│ Cálculo rentabilidad      │ Angel Barrios    │ 8   │ 28    │ Alta  │
│ HU-008│ Factor climático          │ Angel + Anna     │ 10  │ 35    │ Alta  │
│ HU-009│ Municipios Sabana         │ Angel Barrios    │ 5   │ 18    │ Media │
│ HU-010│ Mensajes contextuales     │ Angel Barrios    │ 5   │ 15    │ Media │
│ HU-011│ Tendencias mercado        │ Anna + Angel     │ 8   │ 30    │ Alta  │
│ SM    │ Facilitación Scrum        │ Angel Barrios    │ -   │ 25    │ Alta  │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TOTAL: 49 SP / 196 HORAS                           │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA DETALLADO SPRINT 2:

LUNES 18 AGOSTO 2025:
□ 09:00-12:00  Sprint Planning Meeting (Angel facilita)
□ 13:00-17:00  Inicio desarrollo:
               - Angel: Recomendaciones básicas (HU-006)
               - Anna: Investigación API mercado (HU-011)

MARTES 19 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-11:00  Angel: Cálculos rentabilidad (HU-007)
□ 11:00-12:00  ⚠️ IMPEDIMENTO: API clima no responde
□ 14:00-17:00  Troubleshooting APIs externas

MIÉRCOLES 20 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-11:00  ⚠️ IMPEDIMENTO: API SIPSA-DANE inconsistente
□ 11:00-17:00  Análisis alternativas y datos simulados

JUEVES 21 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-12:00  Trabajo colaborativo:
               - Angel + Anna: Factor climático (HU-008)
               - Pair programming para APIs
□ 13:00-17:00  Desarrollo paralelo:
               - Angel: Municipios + Mensajes (HU-009, HU-010)
               - Anna: Tendencias mercado (HU-011)

VIERNES 22 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 10:00-13:00  Finalización y testing conjunto
□ 14:00-16:00  Sprint Review (Angel facilita)
□ 16:30-18:00  Sprint Retrospective (Angel facilita)

═══════════════════════════════════════════════════════════════════════════════

SPRINT 3: REPORTES Y PANEL ADMINISTRATIVO
Fechas: 25-26 Agosto 2025 (2 días laborables)
Sprint Goal: "Completar sistema con reportes y desplegar en producción"

┌─────────────────────────────────────────────────────────────────────────────┐
│                           SPRINT 3 BACKLOG                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ ID    │ Historia                  │ Responsable      │ SP  │ Horas │ Prior │
├─────────────────────────────────────────────────────────────────────────────┤
│ HU-012│ Reporte cultivos         │ Juan Esteban+Jacks│ 6   │ 20    │ Alta  │
│ HU-013│ Producción proyectada    │ Juan Esteban+Jacks│ 6   │ 20    │ Alta  │
│ HU-014│ Reportes gráficos        │ Juan Esteban+Jacks│ 8   │ 28    │ Alta  │
│ HU-015│ Reportes semanales       │ Juan David Pinto  │ 5   │ 16    │ Media │
│ HU-016│ Gráficas productos       │ Anna              │ 5   │ 16    │ Media │
│ DEPLOY│ Despliegue hosting       │ Todo el equipo    │ 5   │ 24    │ Alta  │
│ SM    │ Facilitación Scrum       │ Angel Barrios     │ -   │ 12    │ Alta  │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TOTAL: 35 SP / 136 HORAS                           │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA DETALLADO SPRINT 3:

LUNES 25 AGOSTO 2025:
□ 09:00-11:00  Sprint Planning (Angel facilita)
□ 11:30-13:00  Desarrollo reportes básicos
□ 13:00-14:00  ⚠️ IMPEDIMENTO: Chart.js configuración
□ 14:00-16:00  Resolución Chart.js (Jacks + Anna colaboran)
□ 16:00-17:00  ⚠️ IMPEDIMENTO: Conflictos CSS
□ 17:00-18:00  Reorganización CSS (Juan David apoyo)

MARTES 26 AGOSTO 2025:
□ 09:00-09:15  Daily Standup (Angel facilita)
□ 09:30-10:30  ⚠️ IMPEDIMENTO: Hosting configuración
□ 10:30-11:00  Resolución hosting (Juan Esteban)
□ 11:00-13:00  Despliegue final exitoso
□ 14:00-15:00  Testing en producción
□ 15:00-17:00  Sprint Review Final (Angel facilita)
□ 17:30-18:30  Sprint Retrospective Final (Angel facilita)

═══════════════════════════════════════════════════════════════════════════════

RESUMEN EJECUTIVO DEL PLANNER

MÉTRICAS FINALES:
✓ Total Story Points: 111 puntos completados
✓ Total Horas: 422 horas hombre
✓ Sprints Completados: 3/3 (100%)
✓ Historias Completadas: 17/17 (100%)
✓ Impedimentos Resueltos: 9/9 (100%)
✓ Despliegue: Exitoso en hosting

DISTRIBUCIÓN EQUILIBRADA:
• Angel Barrios: 166h (39%) - Scrum Master + Backend Principal
• Anna: 96h (23%) - Frontend/Backend + Apoyo Técnico
• Juan David: 72h (17%) - Frontend Especializado
• Juan Esteban: 54h (13%) - Backend/Panel Admin
• Jacks: 34h (8%) - Backend de Apoyo

COLABORACIÓN CLAVE:
• Angel + Anna: Factor climático y tendencias (Sprint 2)
• Juan Esteban + Jacks: Panel administrativo (Sprint 3)
• Juan David: Apoyo CSS y frontend (Sprint 3)

PROYECTO COMPLETADO EXITOSAMENTE
Fecha de Entrega: 26 de Agosto de 2025
Estado: Desplegado y Operativo en Hosting
