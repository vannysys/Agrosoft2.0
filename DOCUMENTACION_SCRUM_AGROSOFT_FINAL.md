# **DOCUMENTACIÓN SCRUM - PROYECTO AGROSOFT**
## **Sistema de Recomendaciones Agrícolas para la Sabana Occidental**

---

## **1. INFORMACIÓN GENERAL DEL PROYECTO**

### **1.1 Datos del Proyecto**
- **Nombre del Proyecto:** AgroSoft - Sistema de Recomendaciones Agrícolas
- **Versión:** 1.0
- **Duración:** 2.5 semanas (3 Sprints: 2 de 1 semana + 1 de 2 días)
- **Metodología:** Scrum Framework
- **Fecha de Inicio:** Lunes 11 de Agosto de 2025
- **Fecha de Finalización:** Martes 26 de Agosto de 2025
- **Estado:** Completado y Desplegado en Hosting

### **1.2 Descripción del Proyecto**
AgroSoft es una plataforma web que proporciona recomendaciones inteligentes de cultivos para productores agrícolas de la Sabana Occidental de Cundinamarca. El sistema integra datos oficiales del SIPSA-DANE con análisis predictivos, considerando factores climáticos, municipales y estacionales para optimizar la rentabilidad de las decisiones de siembra.

### **1.3 Equipo Scrum**
- **Scrum Master:** Angel Barrios (RamaAngel)
- **Product Owner:** Profesor [Nombre del profesor]
- **Development Team:** 
  - Juan David Pinto (Frontend)
  - Anna (Frontend y Backend)
  - Juan Esteban (Backend/Panel Administrativo)
  - Jacks (Backend con Juan Esteban)

---

## **2. HISTORIAS DE USUARIO**

### **MÓDULO: AUTENTICACIÓN Y GESTIÓN DE USUARIOS**

| ID | Rol | Funcionalidad | Resultado | Criterio de aceptación | Contexto | Evento | Resultado esperado |
|----|-----|---------------|-----------|------------------------|----------|--------|-------------------|
| 1 | Como usuario del sistema (productor o administrador) | Necesito iniciar sesión en la plataforma | Con la finalidad de acceder de manera segura a mis funcionalidades | El sistema debe validar usuario y contraseña con autenticación básica | En caso de que las credenciales sean correctas | Cuando el usuario ingrese su usuario y contraseña | Se redirigirá al panel principal correspondiente a su rol |
| 2 | Como productor | Necesito registrarme | Con la finalidad de crear mi cuenta y acceder al sistema | El sistema debe permitir el registro ingresando nombre de usuario, correo electrónico y contraseña | En caso de que el productor sea nuevo y aún no tenga una cuenta | Cuando el usuario complete el formulario de registro | Se redirigirá al panel principal |
| 3 | Como usuario del sistema | Necesito recuperar mi contraseña | Con la finalidad de acceder cuando olvide mis credenciales | El sistema debe mostrar formulario de recuperación básico | En caso de que el usuario haya olvidado su contraseña | Cuando el usuario solicite recuperación de contraseña | Se mostrará formulario de recuperación |
| 4 | Como administrador | Necesito gestionar usuarios del sistema | Con la finalidad de administrar cuentas y permisos | El sistema debe mostrar panel "Gestionar Usuarios" con lista de usuarios registrados | En caso de que se requiera administrar usuarios del sistema | Cuando el administrador haga clic en "Gestionar Usuarios" | Se mostrará interfaz con lista de usuarios |
| 5 | Como usuario del sistema | Necesito cerrar sesión | Con la finalidad de salir de manera segura | El sistema debe cerrar la sesión correctamente | En caso de que el usuario termine su trabajo | Cuando el usuario seleccione cerrar sesión | Se redirigirá a la página de login |

### **MÓDULO: SISTEMA DE RECOMENDACIONES**

| ID | Rol | Funcionalidad | Resultado | Criterio de aceptación | Contexto | Evento | Resultado esperado |
|----|-----|---------------|-----------|------------------------|----------|--------|-------------------|
| 6 | Como productor agrícola | Necesito obtener recomendaciones de cultivos | Con la finalidad de tomar decisiones informadas de siembra | El sistema debe mostrar al menos 5 cultivos recomendados con rentabilidad estimada | En caso de que seleccione municipio y fecha de siembra | Cuando el productor consulte recomendaciones | Se mostrará lista priorizada de cultivos con rentabilidad |
| 7 | Como productor agrícola | Necesito ver la rentabilidad estimada | Con la finalidad de evaluar la viabilidad económica | El sistema debe calcular rentabilidad entre 0-100% considerando múltiples factores | En caso de que requiera análisis económico detallado | Cuando el sistema procese los datos | Se mostrará rentabilidad realista por cultivo |
| 8 | Como productor agrícola | Necesito que se consideren factores climáticos | Con la finalidad de obtener recomendaciones precisas | El sistema debe integrar datos climáticos en los cálculos | En caso de que las condiciones climáticas afecten la rentabilidad | Cuando el sistema analice las condiciones | Se ajustará la rentabilidad según factor climático |
| 9 | Como productor de la Sabana Occidental | Necesito seleccionar mi municipio específico | Con la finalidad de obtener recomendaciones para mi ubicación | El sistema debe incluir los 7 municipios soportados con factores específicos de cada uno | En caso de que el productor esté ubicado en cualquier municipio de la Sabana Occidental | Cuando seleccione su municipio del dropdown | Se mostrarán recomendaciones específicas del municipio seleccionado |
| 10 | Como productor agrícola | Necesito recibir mensajes informativos | Con la finalidad de entender alternativas cuando las condiciones no sean favorables | El sistema debe mostrar mensajes contextuales cuando rentabilidad < 50% | En caso de que las condiciones sean adversas para siembra | Cuando la rentabilidad máxima sea baja | Se mostrará mensaje gracioso con alternativas |
| 11 | Como productor agrícola | Necesito ver tendencias de precios | Con la finalidad de entender el comportamiento del mercado | El sistema debe mostrar tendencias de mercado por producto | En caso de que requiera información de mercado | Cuando consulte recomendaciones | Se mostrarán tendencias actualizadas por producto |

### **MÓDULO: REPORTES ADMINISTRATIVOS**

| ID | Rol | Funcionalidad | Resultado | Criterio de aceptación | Contexto | Evento | Resultado esperado |
|----|-----|---------------|-----------|------------------------|----------|--------|-------------------|
| 12 | Como administrador | Necesito generar reportes de cultivos | Con la finalidad de ver datos básicos de cultivos del sistema | El sistema debe mostrar módulo "Reporte de Cultivos" con información simple de cultivos | En caso de que requiera consultar cultivos del sistema | Cuando el administrador haga clic en "Reporte de Cultivos" | Se mostrará listado básico de cultivos disponibles |
| 13 | Como administrador | Necesito ver proyecciones de producción | Con la finalidad de consultar datos básicos de producción | El sistema debe mostrar módulo "Producción Proyectada" con datos simples | En caso de que requiera información básica de producción | Cuando el administrador haga clic en "Producción Proyectada" | Se mostrarán datos básicos de producción |
| 14 | Como administrador | Necesito acceder a reportes gráficos semanales | Con la finalidad de visualizar gráficas simples de línea por semana | El sistema debe mostrar gráficas de línea con datos semanales por producto | En caso de que requiera visualización semanal | Cuando el administrador haga clic en "Reportes Gráficos" | Se mostrarán gráficas de línea simples con semana vs producto |

### **MÓDULO: REPORTES PARA PRODUCTORES**

| ID | Rol | Funcionalidad | Resultado | Criterio de aceptación | Contexto | Evento | Resultado esperado |
|----|-----|---------------|-----------|------------------------|----------|--------|-------------------|
| 15 | Como productor agrícola | Necesito ver reportes semanales básicos | Con la finalidad de consultar información semanal simple | El sistema debe mostrar gráficas de línea básicas con datos semanales | En caso de que requiera consultar datos por semana | Cuando acceda a la sección de reportes | Se mostrarán gráficas de línea simples por semana |
| 16 | Como productor agrícola | Necesito visualizar gráficas de línea de productos | Con la finalidad de ver tendencias simples por producto | El sistema debe mostrar gráficas de línea con productos y semanas | En caso de que requiera ver datos de productos por semana | Cuando acceda a las gráficas | Se mostrarán gráficas de línea: eje X (semanas) vs eje Y (productos) |

---

## **3. SPRINT 1: AUTENTICACIÓN Y GESTIÓN DE USUARIOS**
### **Fechas: 11-15 Agosto 2025**

### **3.1 PLANIFICACIÓN DEL SPRINT 1**

#### **Sprint Planning Meeting**
- **Duración:** 3 horas
- **Fecha:** Lunes 11 de Agosto de 2025
- **Facilitador:** Angel Barrios (Scrum Master)
- **Participantes:** Todo el equipo Scrum

#### **Sprint Goal**
*"Implementar un sistema completo de autenticación y gestión de usuarios que permita el acceso seguro a la plataforma AgroSoft"*

#### **Sprint Backlog**
| Historia | Responsable | Estimación | Prioridad |
|----------|-------------|------------|-----------|
| HU-001: Login básico | Juan David Pinto | 8 pts | Alta |
| HU-002: Registro de usuarios | Juan David Pinto | 5 pts | Alta |
| HU-003: Recuperación de contraseña | Anna | 6 pts | Media |
| HU-004: Gestión de usuarios | Juan Esteban | 5 pts | Media |
| HU-005: Logout seguro | Anna | 3 pts | Baja |

**Total Sprint Backlog:** 27 Story Points

### **3.2 EJECUCIÓN DEL SPRINT 1**

#### **Daily Standups**
**Formato:** 15 minutos diarios a las 9:00 AM
**Facilitador:** Angel Barrios

**Lunes 12 Nov:** Configuración inicial del proyecto
**Martes 13 Nov:** Desarrollo de login y registro
**Miércoles 14 Nov:** **IMPEDIMENTO:** Problemas con tokens de autenticación
**Jueves 15 Nov:** Resolución de problemas de autenticación
**Viernes 16 Nov:** Finalización y testing

#### **Impedimentos Identificados**
- **Impedimento Principal:** Problemas con la implementación del token de autenticación
- **Descripción:** Dificultades para generar y validar tokens correctamente
- **Impacto:** Retraso de 1 día en HU-001 y HU-003
- **Resolución:** Cambio a autenticación básica de Django

### **3.3 REVISIÓN Y RETROSPECTIVA SPRINT 1**

#### **Sprint Review**
- **Duración:** 1.5 horas
- **Fecha:** Viernes 15 de Agosto de 2025

**Funcionalidades Demostradas:**
- ✅ Sistema de login funcional
- ✅ Registro de usuarios completo
- ✅ Recuperación de contraseñas básica
- ✅ Panel de gestión de usuarios
- ✅ Logout seguro implementado

#### **Sprint Retrospective**
**¿Qué funcionó bien?**
- Comunicación efectiva del equipo
- Resolución rápida de impedimentos

**¿Qué no funcionó?**
- Subestimación de complejidad del token de autenticación
- Falta de investigación previa

**¿Qué mejorar?**
- Investigar APIs antes del siguiente Sprint
- Mejor estimación de complejidad técnica

---

## **4. SPRINT 2: SISTEMA DE RECOMENDACIONES**
### **Fechas: 18-22 Agosto 2025**

### **4.1 PLANIFICACIÓN DEL SPRINT 2**

#### **Sprint Goal**
*"Desarrollar el motor de recomendaciones inteligente integrando datos climáticos y de mercado para proporcionar análisis de rentabilidad precisos"*

#### **Sprint Backlog**
| Historia | Responsable | Estimación | Prioridad |
|----------|-------------|------------|-----------|
| HU-006: Recomendaciones básicas | Angel Barrios | 13 pts | Alta |
| HU-007: Cálculo de rentabilidad | Angel Barrios | 8 pts | Alta |
| HU-008: Factor climático | Angel Barrios | 10 pts | Alta |
| HU-009: Municipios de la Sabana | Angel Barrios | 5 pts | Media |
| HU-010: Mensajes contextuales | Angel Barrios | 5 pts | Media |
| HU-011: Tendencias de mercado | Anna | 8 pts | Alta |

**Total Sprint Backlog:** 49 Story Points

### **4.2 EJECUCIÓN DEL SPRINT 2**

#### **Impedimentos Críticos del Sprint 2**

**Lunes 19 Nov:** Inicio desarrollo recomendaciones
**Martes 20 Nov:** **IMPEDIMENTO:** API del clima no responde
**Miércoles 21 Nov:** **IMPEDIMENTO:** Problemas con API SIPSA-DANE
**Jueves 22 Nov:** Implementación de datos simulados
**Viernes 23 Nov:** Finalización con datos híbridos

**Impedimento 1: API Climática**
- **Problema:** Servicio de clima inestable, timeouts frecuentes
- **Resolución:** Datos climáticos simulados basados en promedios

**Impedimento 2: API SIPSA-DANE**
- **Problema:** Estructura de datos inconsistente
- **Resolución:** Servicio híbrido con datos reales + simulación

### **4.3 REVISIÓN Y RETROSPECTIVA SPRINT 2**

#### **Sprint Review**
- **Fecha:** Viernes 22 de Agosto de 2025

**Funcionalidades Demostradas:**
- ✅ Motor de recomendaciones funcional
- ✅ Cálculos de rentabilidad (0-100%)
- ✅ Factor climático integrado
- ✅ 7 municipios de la Sabana Occidental agregados
- ✅ 24 mensajes contextuales
- ✅ Tendencias de mercado

#### **Sprint Retrospective**
**¿Qué funcionó bien?**
- Adaptación ante problemas con APIs
- Soluciones creativas con datos híbridos

**¿Qué no funcionó?**
- Dependencia de servicios externos no confiables
- Subestimación del riesgo de APIs

**¿Qué mejorar?**
- Diseñar con fallbacks desde el inicio
- Validar APIs antes del Sprint

---

## **5. SPRINT 3: REPORTES Y PANEL ADMINISTRATIVO**
### **Fechas: 25-26 Agosto 2025**

### **5.1 PLANIFICACIÓN DEL SPRINT 3**

#### **Sprint Goal**
*"Completar el sistema con reportes visuales y panel administrativo, preparando la aplicación para despliegue en producción"*

#### **Sprint Backlog**
| Historia | Responsable | Estimación | Prioridad |
|----------|-------------|------------|-----------|
| HU-012: Reporte de cultivos | Juan Esteban & Jacks | 6 pts | Alta |
| HU-013: Producción proyectada | Juan Esteban & Jacks | 6 pts | Alta |
| HU-014: Reportes gráficos | Juan Esteban & Jacks | 8 pts | Alta |
| HU-015: Reportes semanales | Juan David Pinto | 5 pts | Media |
| HU-016: Gráficas de productos | Anna | 5 pts | Media |
| Despliegue en hosting | Todo el equipo | 5 pts | Alta |

**Total Sprint Backlog:** 35 Story Points

### **5.2 EJECUCIÓN DEL SPRINT 3**

#### **Daily Standups con Impedimentos Menores**
- **Lunes 26 Nov:** Desarrollo de reportes básicos
- **Martes 27 Nov:** **IMPEDIMENTO:** Problemas con Chart.js y configuración de gráficas
- **Miércoles 28 Nov:** **IMPEDIMENTO:** Conflictos de CSS en el panel administrativo
- **Jueves 29 Nov:** **IMPEDIMENTO:** Errores de configuración en el hosting
- **Viernes 30 Nov:** Resolución final y despliegue exitoso

#### **Impedimentos Identificados Sprint 3**

**Impedimento 1: Configuración de Chart.js**
- **Problema:** Dificultades para configurar las gráficas de línea correctamente
- **Impacto:** Retraso de medio día en HU-014 y HU-016
- **Resolución:** Jacks y Anna colaboraron para simplificar la implementación

**Impedimento 2: Conflictos de CSS**
- **Problema:** Estilos del panel administrativo conflictaban con el frontend principal
- **Impacto:** Problemas de visualización en diferentes navegadores
- **Resolución:** Juan David Pinto ayudó a reorganizar los estilos CSS

**Impedimento 3: Configuración de Hosting**
- **Problema:** Errores de configuración inicial en el servidor de hosting
- **Impacto:** Retraso de 4 horas en el despliegue final
- **Resolución:** Juan Esteban resolvió problemas de configuración del servidor

### **5.3 REVISIÓN Y RETROSPECTIVA SPRINT 3**

#### **Sprint Review**
- **Fecha:** Martes 26 de Agosto de 2025

**Funcionalidades Demostradas:**
- ✅ Panel administrativo con 4 módulos
- ✅ Reportes gráficos semanales simples
- ✅ Gráficas de línea básicas
- ✅ Sistema desplegado en hosting
- ✅ Aplicación completamente operativa

#### **Sprint Retrospective Final**
**¿Qué funcionó bien?**
- Colaboración efectiva para resolver impedimentos menores
- Uso exitoso de tecnologías conocidas (Chart.js, CSS)
- Resolución rápida de problemas de hosting
- Apoyo mutuo entre desarrolladores frontend y backend

**¿Qué no funcionó?**
- Falta de testing previo de Chart.js en diferentes navegadores
- Conflictos de CSS no previstos en la planificación
- Configuración de hosting más compleja de lo esperado

**¿Qué mejorar para futuros proyectos?**
- Realizar pruebas de compatibilidad de librerías desde el inicio
- Establecer convenciones de CSS más estrictas
- Documentar configuraciones de despliegue paso a paso

**Lecciones Aprendidas del Proyecto Completo:**
- Importancia de validar servicios externos antes de depender de ellos
- Valor de implementar fallbacks y soluciones resilientes
- Efectividad de la comunicación diaria en Daily Standups
- Beneficio de la colaboración entre frontend y backend
- Necesidad de testing continuo durante el desarrollo

---

## **6. DISTRIBUCIÓN FINAL DEL TRABAJO**

### **Angel Barrios (RamaAngel) - Scrum Master/Backend**
- Facilitación de ceremonias Scrum
- Motor de recomendaciones completo
- Cálculos de rentabilidad (0-100%)
- Factor climático y 7 municipios de la Sabana Occidental (Funza, Madrid, Mosquera, Bojacá, Facatativá, Subachoque, El Rosal)
- 24 mensajes contextuales graciosos

### **Juan David Pinto - Frontend**
- Sistema de autenticación (login/registro)
- Interfaces de usuario principales
- Reportes semanales para productores
- Diseño responsive

### **Anna - Frontend y Backend**
- Recuperación de contraseñas
- Logout seguro
- Tendencias de mercado
- Gráficas de productos
- Apoyo en backend

### **Juan Esteban - Backend/Panel Administrativo**
- Gestión de usuarios
- Panel administrativo con 4 módulos:
  - 🔵 Gestionar Usuarios
  - 🟢 Reporte de Cultivos  
  - 🔵 Producción Proyectada
  - 🟡 Reportes Gráficos

### **Jacks - Backend (con Juan Esteban)**
- Colaboración en panel administrativo
- Reportes gráficos semanales
- Gráficas de línea simples
- Apoyo en funcionalidades de backend

---

## **7. MÉTRICAS FINALES DEL PROYECTO**

### **7.1 Cumplimiento por Sprint**
- **Sprint 1:** 5/5 historias (100%) - Con impedimentos de tokens
- **Sprint 2:** 6/6 historias (100%) - Con impedimentos de APIs  
- **Sprint 3:** 6/6 historias (100%) - Sin impedimentos

### **7.2 Total del Proyecto**
- **Historias Completadas:** 17/17 (100%)
- **Story Points Entregados:** 111 puntos
- **Sprints Exitosos:** 3/3
- **Despliegue:** ✅ Completado exitosamente

### **7.3 Impedimentos y Resoluciones**
- **Sprint 1:** Tokens de autenticación → Solución: Django sessions
- **Sprint 2:** APIs externas inestables → Solución: Datos híbridos
- **Sprint 3:** Chart.js, CSS y hosting → Solución: Colaboración del equipo

---

## **8. CONCLUSIONES**

El proyecto AgroSoft fue completado exitosamente en 2.5 semanas utilizando metodología Scrum. Iniciado el lunes 11 de agosto de 2025, el equipo liderado por Angel Barrios como Scrum Master logró entregar un sistema completo y funcional desplegado en hosting el 26 de agosto de 2025.

La colaboración efectiva entre Juan David Pinto (Frontend), Anna (Frontend/Backend), Juan Esteban (Backend/Panel Admin) y Jacks (Backend), junto con la facilitación de Angel Barrios, resultó en un producto de alta calidad que satisface las necesidades de los productores agrícolas.

**Proyecto:** ✅ **COMPLETADO EXITOSAMENTE**  
**Despliegue:** ✅ **OPERATIVO EN HOSTING**  
**Equipo:** ✅ **OBJETIVOS CUMPLIDOS AL 100%**

---

**Equipo de Desarrollo:**
- **Scrum Master:** Angel Barrios (RamaAngel)
- **Desarrolladores:** Juan David Pinto, Anna, Juan Esteban, Jacks

**Fecha de Finalización:** 26 de Agosto de 2025
**Estado:** Proyecto Completado y Desplegado
