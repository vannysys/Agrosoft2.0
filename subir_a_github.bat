@echo off
echo ========================================
echo 🚀 SUBIENDO TRABAJO A RAMA ANGEL
echo ========================================

echo.
echo 📁 Navegando al directorio del proyecto...
cd /d "C:\Users\jbang\OneDrive\Desktop\agrosoft"

echo.
echo 📊 Verificando estado actual...
git status

echo.
echo 🌿 Verificando rama actual...
git branch

echo.
echo 🔄 Cambiando a RamaAngel...
git checkout RamaAngel
if errorlevel 1 (
    echo ⚠️ Rama no existe, creándola...
    git checkout -b RamaAngel
)

echo.
echo ➕ Agregando todos los archivos...
git add .

echo.
echo 📝 Haciendo commit...
git commit -m "🚀 Sistema AgroSoft completo - RamaAngel

✨ Implementaciones principales:
- Sistema de rentabilidad realista (0-100%%) con distribución inteligente
- Factor climático integrado en cálculos de rentabilidad  
- Municipio de Funza agregado (7mo municipio Sabana Occidental)
- 24 mensajes graciosos para rentabilidades bajas (<50%%)
- Penalización por tendencia de mercado bajando (-25%%)
- Fecha de actualización corregida (siempre actual)

🎯 Características técnicas:
- Curva de saturación logarítmica para rentabilidades realistas
- Factores municipales específicos por producto
- Variabilidad climática con temperaturas ideales
- Sistema de mensajes aleatorios (60%% variedad)
- UI mejorada con alertas coloridas y gradientes

📊 Resultados obtenidos:
- Promedio rentabilidad: ~80%% (sector agrícola realista)
- Rango completo: 0-100%% sin desbordes
- 7 municipios: Facatativá, Madrid, Mosquera, El Rosal, Subachoque, Bojacá, Funza
- Integración completa: Municipal + Climático + Estacional + Tendencia

🧪 Testing completo:
- 5 scripts de prueba implementados
- Verificación de todos los factores
- Validación de mensajes graciosos
- Confirmación de fechas actuales"

echo.
echo 🚀 Subiendo a GitHub...
git push -u origin RamaAngel

echo.
echo ========================================
echo ✅ ¡PROCESO COMPLETADO!
echo ========================================
echo.
echo 🌐 Tu trabajo está ahora en GitHub en la rama RamaAngel
echo 💡 Puedes crear un Pull Request desde la interfaz web
echo 📱 URL: https://github.com/tu-usuario/tu-repo/tree/RamaAngel
echo.
pause
