PLANNER PROYECTO AGROSOFT
Sistema de Recomendaciones Agrícolas - Sabana Occidental

═══════════════════════════════════════════════════════════════════════════════

INFORMACIÓN GENERAL

Proyecto: AgroSoft - Sistema de Recomendaciones Agrícolas
Duración: 2.5 semanas (11 Agosto - 26 Agosto 2025)
Metodología: Scrum Framework
Equipo: 5 desarrolladores

Scrum Master: Angel Barrios (RamaAngel)
Product Owner: Profesor [Nombre]
Development Team: Juan David Pinto, Anna, Juan Esteban, Jacks

═══════════════════════════════════════════════════════════════════════════════

SPRINT 1: AUTENTICACIÓN Y GESTIÓN DE USUARIOS
Fechas: 11-15 Agosto 2025 (5 días)
Sprint Goal: "Implementar sistema completo de autenticación y gestión de usuarios"

┌─────────────────────────────────────────────────────────────────────────────┐
│                           SPRINT 1 BACKLOG                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ HU-001 │ Login básico              │ Juan David Pinto │ 8 pts  │ Alta     │
│ HU-002 │ Registro de usuarios      │ Juan David Pinto │ 5 pts  │ Alta     │
│ HU-003 │ Recuperación contraseña   │ Anna             │ 6 pts  │ Media    │
│ HU-004 │ Gestión de usuarios       │ Juan Esteban     │ 5 pts  │ Media    │
│ HU-005 │ Logout seguro             │ Anna             │ 3 pts  │ Baja     │
├─────────────────────────────────────────────────────────────────────────────┤
│                              TOTAL: 27 STORY POINTS                         │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA SPRINT 1:

Lunes 11 Agosto:
□ 9:00 AM - Sprint Planning (3 horas)
□ 1:00 PM - Configuración inicial del proyecto
□ 3:00 PM - Setup de entorno de desarrollo

Martes 12 Agosto:
□ 9:00 AM - Daily Standup (15 min)
□ 9:30 AM - Desarrollo login y registro (Juan David)
□ 9:30 AM - Inicio recuperación contraseña (Anna)
□ 9:30 AM - Setup gestión usuarios (Juan Esteban)

Miércoles 13 Agosto:
□ 9:00 AM - Daily Standup (15 min)
⚠️ IMPEDIMENTO: Problemas con tokens de autenticación
□ 10:00 AM - Sesión de resolución de problemas (todo el equipo)
□ 2:00 PM - Implementación de solución alternativa

Jueves 14 Agosto:
□ 9:00 AM - Daily Standup (15 min)
□ 9:30 AM - Resolución final de autenticación
□ 2:00 PM - Testing de funcionalidades
□ 4:00 PM - Integración de módulos

Viernes 15 Agosto:
□ 9:00 AM - Daily Standup (15 min)
□ 10:00 AM - Testing final y corrección de bugs
□ 2:00 PM - Sprint Review (1.5 horas)
□ 4:00 PM - Sprint Retrospective (1 hora)

IMPEDIMENTOS SPRINT 1:
⚠️ Problemas con tokens JWT → Solución: Django sessions
⚠️ Complejidad subestimada → Solución: Investigación adicional

═══════════════════════════════════════════════════════════════════════════════

SPRINT 2: SISTEMA DE RECOMENDACIONES
Fechas: 18-22 Agosto 2025 (5 días)
Sprint Goal: "Desarrollar motor de recomendaciones con análisis multifactorial"

┌─────────────────────────────────────────────────────────────────────────────┐
│                           SPRINT 2 BACKLOG                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ HU-006 │ Recomendaciones básicas   │ Angel Barrios    │ 13 pts │ Alta     │
│ HU-007 │ Cálculo rentabilidad      │ Angel Barrios    │ 8 pts  │ Alta     │
│ HU-008 │ Factor climático          │ Angel Barrios    │ 10 pts │ Alta     │
│ HU-009 │ Municipios Sabana         │ Angel Barrios    │ 5 pts  │ Media    │
│ HU-010 │ Mensajes contextuales     │ Angel Barrios    │ 5 pts  │ Media    │
│ HU-011 │ Tendencias mercado        │ Anna             │ 8 pts  │ Alta     │
├─────────────────────────────────────────────────────────────────────────────┤
│                              TOTAL: 49 STORY POINTS                         │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA SPRINT 2:

Lunes 18 Agosto:
□ 9:00 AM - Sprint Planning (3 horas)
□ 1:00 PM - Inicio desarrollo recomendaciones básicas
□ 3:00 PM - Investigación APIs climáticas

Martes 19 Agosto:
□ 9:00 AM - Daily Standup (15 min)
□ 9:30 AM - Desarrollo cálculos de rentabilidad
⚠️ IMPEDIMENTO: API del clima no responde
□ 11:00 AM - Sesión de troubleshooting APIs

Miércoles 20 Agosto:
□ 9:00 AM - Daily Standup (15 min)
⚠️ IMPEDIMENTO: Problemas con API SIPSA-DANE
□ 10:00 AM - Análisis de alternativas para datos
□ 2:00 PM - Implementación de datos simulados

Jueves 21 Agosto:
□ 9:00 AM - Daily Standup (15 min)
□ 9:30 AM - Desarrollo de fallbacks y datos híbridos
□ 2:00 PM - Implementación municipios y mensajes
□ 4:00 PM - Testing de recomendaciones

Viernes 22 Agosto:
□ 9:00 AM - Daily Standup (15 min)
□ 10:00 AM - Finalización con datos híbridos
□ 2:00 PM - Sprint Review (2 horas)
□ 4:30 PM - Sprint Retrospective (1.5 horas)

IMPEDIMENTOS SPRINT 2:
⚠️ API Climática inestable → Solución: Datos simulados
⚠️ API SIPSA-DANE inconsistente → Solución: Servicio híbrido
⚠️ Integración de APIs → Solución: Fallbacks automáticos

═══════════════════════════════════════════════════════════════════════════════

SPRINT 3: REPORTES Y PANEL ADMINISTRATIVO
Fechas: 25-26 Agosto 2025 (2 días)
Sprint Goal: "Completar sistema con reportes y desplegar en producción"

┌─────────────────────────────────────────────────────────────────────────────┐
│                           SPRINT 3 BACKLOG                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ HU-012 │ Reporte cultivos         │ Juan Esteban+Jacks │ 6 pts │ Alta     │
│ HU-013 │ Producción proyectada    │ Juan Esteban+Jacks │ 6 pts │ Alta     │
│ HU-014 │ Reportes gráficos        │ Juan Esteban+Jacks │ 8 pts │ Alta     │
│ HU-015 │ Reportes semanales       │ Juan David Pinto   │ 5 pts │ Media    │
│ HU-016 │ Gráficas productos       │ Anna               │ 5 pts │ Media    │
│ DEPLOY │ Despliegue hosting       │ Todo el equipo     │ 5 pts │ Alta     │
├─────────────────────────────────────────────────────────────────────────────┤
│                              TOTAL: 35 STORY POINTS                         │
└─────────────────────────────────────────────────────────────────────────────┘

CRONOGRAMA SPRINT 3:

Lunes 25 Agosto:
□ 9:00 AM - Sprint Planning (2 horas)
□ 11:30 AM - Desarrollo reportes básicos
⚠️ IMPEDIMENTO: Problemas con Chart.js
□ 2:00 PM - Resolución Chart.js (Jacks + Anna)
⚠️ IMPEDIMENTO: Conflictos CSS panel admin
□ 4:00 PM - Reorganización CSS (Juan David apoyo)

Martes 26 Agosto:
□ 9:00 AM - Daily Standup (15 min)
⚠️ IMPEDIMENTO: Errores configuración hosting
□ 9:30 AM - Resolución hosting (Juan Esteban)
□ 11:00 AM - Despliegue final exitoso
□ 1:00 PM - Testing final en producción
□ 3:00 PM - Sprint Review (2 horas)
□ 5:30 PM - Sprint Retrospective (1 hora)

IMPEDIMENTOS SPRINT 3:
⚠️ Chart.js configuración → Solución: Colaboración Jacks+Anna
⚠️ Conflictos CSS → Solución: Juan David reorganizó estilos
⚠️ Hosting configuración → Solución: Juan Esteban resolvió servidor

═══════════════════════════════════════════════════════════════════════════════

RESUMEN EJECUTIVO DEL PLANNER

MÉTRICAS FINALES:
• Total Story Points: 111 puntos
• Sprints Completados: 3/3 (100%)
• Historias Completadas: 17/17 (100%)
• Impedimentos Resueltos: 9/9 (100%)
• Despliegue: ✓ Exitoso

DISTRIBUCIÓN DE TRABAJO:
• Angel Barrios: 31 pts (28%) - Scrum Master + Backend
• Juan David Pinto: 18 pts (16%) - Frontend
• Anna: 24 pts (22%) - Frontend/Backend
• Juan Esteban: 20 pts (18%) - Backend/Admin
• Jacks: 18 pts (16%) - Backend

LECCIONES APRENDIDAS:
✓ Estimación con Planning Poker efectiva
✓ Ajustes por impedimentos necesarios
✓ Colaboración clave para resolución de problemas
✓ Fallbacks esenciales para APIs externas

PROYECTO COMPLETADO EXITOSAMENTE
Fecha: 26 de Agosto de 2025
Estado: Desplegado y Operativo
