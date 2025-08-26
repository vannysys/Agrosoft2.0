#!/usr/bin/env python
"""
Script para probar la API del clima con la key proporcionada
"""

import os
import sys
import requests
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def probar_api_clima():
    """
    Prueba la API de OpenWeatherMap con la key proporcionada
    """
    print("🌡️ PROBANDO API DE CLIMA REAL")
    print("=" * 50)
    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    print(f"🔑 API Key: {api_key[:10]}...{api_key[-5:]}")
    
    if not api_key:
        print("❌ No se encontró API key en .env")
        return False
    
    # Probar con municipios de la Sabana Occidental
    municipios = [
        'Facatativá',
        'Madrid', 
        'Mosquera',
        'El Rosal',
        'Subachoque',
        'Bojacá'
    ]
    
    print("\n🌍 PROBANDO CLIMA EN MUNICIPIOS:")
    print("-" * 40)
    
    resultados = {}
    
    for municipio in municipios:
        try:
            # URL para clima actual
            url = f"https://api.openweathermap.org/data/2.5/weather?q={municipio},CO&appid={api_key}&units=metric&lang=es"
            
            print(f"🔍 Consultando {municipio}...")
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                temperatura = round(data['main']['temp'], 1)
                sensacion = round(data['main']['feels_like'], 1)
                humedad = data['main']['humidity']
                descripcion = data['weather'][0]['description']
                
                resultados[municipio] = {
                    'temperatura': temperatura,
                    'sensacion': sensacion,
                    'humedad': humedad,
                    'descripcion': descripcion,
                    'status': 'success'
                }
                
                print(f"✅ {municipio}: {temperatura}°C ({descripcion})")
                
            else:
                print(f"❌ {municipio}: Error {response.status_code}")
                resultados[municipio] = {'status': 'error', 'code': response.status_code}
                
        except Exception as e:
            print(f"💥 {municipio}: Error - {str(e)[:50]}...")
            resultados[municipio] = {'status': 'exception', 'error': str(e)}
    
    return resultados

def mostrar_resumen_clima(resultados):
    """
    Muestra un resumen detallado del clima obtenido
    """
    print("\n\n📊 RESUMEN DETALLADO DEL CLIMA")
    print("=" * 50)
    
    exitosos = [m for m, r in resultados.items() if r.get('status') == 'success']
    
    if exitosos:
        print(f"✅ Municipios exitosos: {len(exitosos)}/{len(resultados)}")
        
        print("\n🌡️ TEMPERATURAS OBTENIDAS:")
        print("┌─────────────────┬─────────────┬─────────────┬──────────┬─────────────────────┐")
        print("│ Municipio       │ Temperatura │ Sensación   │ Humedad  │ Descripción         │")
        print("├─────────────────┼─────────────┼─────────────┼──────────┼─────────────────────┤")
        
        for municipio in exitosos:
            r = resultados[municipio]
            print(f"│ {municipio:<15} │ {r['temperatura']:>9.1f}°C │ {r['sensacion']:>9.1f}°C │ {r['humedad']:>6}%  │ {r['descripcion']:<19} │")
        
        print("└─────────────────┴─────────────┴─────────────┴──────────┴─────────────────────┘")
        
        # Estadísticas
        temps = [r['temperatura'] for r in resultados.values() if r.get('status') == 'success']
        if temps:
            temp_promedio = sum(temps) / len(temps)
            temp_min = min(temps)
            temp_max = max(temps)
            
            print(f"\n📈 ESTADÍSTICAS:")
            print(f"• Temperatura promedio: {temp_promedio:.1f}°C")
            print(f"• Temperatura mínima: {temp_min:.1f}°C")
            print(f"• Temperatura máxima: {temp_max:.1f}°C")
            print(f"• Rango: {temp_max - temp_min:.1f}°C")
    
    # Errores
    errores = [m for m, r in resultados.items() if r.get('status') != 'success']
    if errores:
        print(f"\n❌ Municipios con errores: {len(errores)}")
        for municipio in errores:
            r = resultados[municipio]
            if r.get('status') == 'error':
                print(f"• {municipio}: HTTP {r.get('code')}")
            else:
                print(f"• {municipio}: {r.get('error', 'Error desconocido')[:50]}...")

def probar_integracion_django():
    """
    Prueba la integración con Django
    """
    print("\n\n🔧 PROBANDO INTEGRACIÓN CON DJANGO")
    print("=" * 50)
    
    try:
        # Configurar Django
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')
        
        import django
        django.setup()
        
        from productores.views import obtener_clima_openweather
        
        print("✅ Django configurado correctamente")
        
        # Probar función de clima
        fecha = datetime.now()
        municipio = "Facatativá"
        
        print(f"🔍 Probando obtener_clima_openweather('{municipio}', {fecha.strftime('%Y-%m-%d')})...")
        
        temperatura = obtener_clima_openweather(municipio, fecha)
        
        if temperatura:
            print(f"✅ Temperatura obtenida: {temperatura}°C")
            print("🎉 ¡La integración con Django funciona perfectamente!")
            return True
        else:
            print("❌ No se pudo obtener temperatura")
            return False
            
    except Exception as e:
        print(f"💥 Error en integración Django: {e}")
        return False

def mostrar_instrucciones_uso():
    """
    Muestra instrucciones para usar el clima en la aplicación
    """
    print("\n\n📋 INSTRUCCIONES DE USO")
    print("=" * 40)
    
    print("🌐 CÓMO VER EL CLIMA EN LA APLICACIÓN:")
    print("1. Asegúrate de que el servidor esté corriendo:")
    print("   python manage.py runserver")
    print()
    print("2. Ve a: http://127.0.0.1:8000/")
    print()
    print("3. Selecciona cualquier municipio y fecha")
    print()
    print("4. Haz clic en 'Obtener Recomendaciones'")
    print()
    print("5. Observa la nueva columna '🌤️ Clima Actual'")
    print("   Ahora debería mostrar la temperatura real")
    print("   en lugar de 'N/A'")
    
    print("\n🔄 REINICIAR SERVIDOR:")
    print("Si el servidor ya estaba corriendo, reinícialo")
    print("para que cargue la nueva configuración:")
    print("• Ctrl+C para detener")
    print("• python manage.py runserver para reiniciar")

if __name__ == "__main__":
    print("🌡️ AGROSOFT - CONFIGURACIÓN DE CLIMA REAL")
    print("=" * 60)
    
    # Probar API directamente
    resultados = probar_api_clima()
    
    if resultados:
        mostrar_resumen_clima(resultados)
        
        # Probar integración con Django
        if probar_integracion_django():
            mostrar_instrucciones_uso()
            
            print("\n\n🎉 ¡CONFIGURACIÓN EXITOSA!")
            print("=" * 40)
            print("✅ API key configurada")
            print("✅ Clima real funcionando")
            print("✅ Integración Django OK")
            print("✅ Listo para usar en la aplicación")
        else:
            print("\n⚠️ Hay problemas con la integración Django")
    else:
        print("\n❌ No se pudieron obtener datos climáticos")
        print("Verifica la API key y la conexión a internet")
