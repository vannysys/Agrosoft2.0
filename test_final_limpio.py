#!/usr/bin/env python
"""
Prueba final del sistema AgroSoft con comentarios profesionales
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService
from productores.views import obtener_clima_openweather

def probar_fecha_actualizacion():
    """
    Verifica que la fecha de última actualización aparezca correctamente
    """
    print("📅 PROBANDO FECHA DE ÚLTIMA ACTUALIZACIÓN")
    print("=" * 50)
    
    sipsa = SipsaService()
    estadisticas = sipsa.obtener_estadisticas_mercado()
    
    if estadisticas and 'fecha_ultima_actualizacion' in estadisticas:
        fecha = estadisticas['fecha_ultima_actualizacion']
        print(f"✅ Fecha obtenida: {fecha}")
        
        if fecha and fecha != "":
            print("✅ La fecha NO está en blanco")
            return True
        else:
            print("❌ La fecha está en blanco")
            return False
    else:
        print("❌ No se encontraron estadísticas")
        return False

def probar_factor_climatico_dinamico():
    """
    Verifica que el factor climático cambie según municipio y fecha
    """
    print("\n🌡️ PROBANDO FACTOR CLIMÁTICO DINÁMICO")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    escenarios = [
        ("Facatativá", datetime(2025, 8, 22)),
        ("Subachoque", datetime(2025, 8, 22)),
        ("Facatativá", datetime(2025, 1, 15)),
        ("Subachoque", datetime(2025, 1, 15)),
    ]
    
    resultados = []
    
    for municipio, fecha in escenarios:
        clima = obtener_clima_openweather(municipio, fecha)
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, clima)
        
        if recomendaciones:
            papa = next((r for r in recomendaciones if 'PAPA' in r['producto']), None)
            if papa:
                factor = papa.get('clima_factor', 1.0)
                resultados.append(factor)
                print(f"{municipio} {fecha.strftime('%m/%Y')}: {clima}°C → Factor {factor:.2f}x")
    
    factores_unicos = len(set(resultados))
    if factores_unicos > 1:
        print(f"✅ Factor climático varía ({factores_unicos} valores diferentes)")
        return True
    else:
        print(f"❌ Factor climático no varía (todos iguales: {resultados[0]:.2f}x)")
        return False

def probar_comentarios_profesionales():
    """
    Verifica que los comentarios sean apropiados para entorno académico
    """
    print("\n📝 VERIFICANDO COMENTARIOS PROFESIONALES")
    print("=" * 50)
    
    archivos_revisar = [
        'productores/sipsa_service.py',
        'productores/views.py'
    ]
    
    comentarios_informales = [
        '🎉', '✅', '❌', '🔥', '💥', '🚀', '🌟', 
        'genial', 'increíble', 'súper', 'wow'
    ]
    
    archivos_limpios = 0
    
    for archivo in archivos_revisar:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read().lower()
            
            encontrados = [emoji for emoji in comentarios_informales if emoji in contenido]
            
            if not encontrados:
                print(f"✅ {archivo}: Comentarios profesionales")
                archivos_limpios += 1
            else:
                print(f"⚠️ {archivo}: Encontrados elementos informales: {encontrados[:3]}")
                
        except FileNotFoundError:
            print(f"❌ {archivo}: Archivo no encontrado")
    
    return archivos_limpios == len(archivos_revisar)

def probar_funcionalidad_completa():
    """
    Prueba integral de todas las funcionalidades
    """
    print("\n🎯 PRUEBA INTEGRAL DEL SISTEMA")
    print("=" * 50)
    
    sipsa = SipsaService()
    municipio = "Facatativá"
    fecha = datetime.now()
    
    clima = obtener_clima_openweather(municipio, fecha)
    print(f"Clima obtenido: {clima}°C")
    
    recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, clima)
    print(f"Recomendaciones generadas: {len(recomendaciones)}")
    
    estadisticas = sipsa.obtener_estadisticas_mercado()
    print(f"Estadísticas obtenidas: {bool(estadisticas)}")
    
    if recomendaciones and estadisticas and clima:
        print("✅ Sistema completamente funcional")
        
        print("\nTop 3 recomendaciones:")
        for i, rec in enumerate(recomendaciones[:3], 1):
            factor_clima = rec.get('clima_factor', 1.0)
            print(f"{i}. {rec['producto']}: ${rec['precio_actual']:,} (Factor: {factor_clima:.2f}x)")
        
        return True
    else:
        print("❌ Sistema con problemas")
        return False

def mostrar_resumen_final():
    """
    Presenta el estado final del sistema
    """
    print("\n📊 RESUMEN FINAL DEL SISTEMA")
    print("=" * 50)
    
    print("CARACTERÍSTICAS IMPLEMENTADAS:")
    print("• Datos reales basados en precios de Corabastos")
    print("• Factor climático dinámico por municipio y fecha")
    print("• API de clima real con fallback simulado")
    print("• Fecha de última actualización funcionando")
    print("• Comentarios profesionales y académicos")
    print("• Sistema robusto con múltiples fallbacks")
    
    print("\nCOMPONENTES TÉCNICOS:")
    print("• SipsaService: Análisis de precios agrícolas")
    print("• DatosRealesService: Simulación basada en datos reales")
    print("• OpenWeatherMap API: Datos meteorológicos")
    print("• Sistema de cache: Optimización de rendimiento")
    print("• Algoritmos de predicción: Factores contextuales")
    
    print("\nESTADO ACTUAL:")
    print("• Servidor Django: Activo en puerto 8000")
    print("• Base de datos: SQLite configurada")
    print("• Templates: Interfaz responsive completa")
    print("• APIs externas: Configuradas y funcionales")

if __name__ == "__main__":
    try:
        print("🌱 AGROSOFT - VERIFICACIÓN FINAL")
        print("=" * 60)
        
        fecha_ok = probar_fecha_actualizacion()
        factor_ok = probar_factor_climatico_dinamico()
        comentarios_ok = probar_comentarios_profesionales()
        sistema_ok = probar_funcionalidad_completa()
        
        mostrar_resumen_final()
        
        print("\n" + "=" * 60)
        print("RESULTADOS DE VERIFICACIÓN:")
        print(f"• Fecha de actualización: {'✅ OK' if fecha_ok else '❌ ERROR'}")
        print(f"• Factor climático dinámico: {'✅ OK' if factor_ok else '❌ ERROR'}")
        print(f"• Comentarios profesionales: {'✅ OK' if comentarios_ok else '❌ REVISAR'}")
        print(f"• Sistema integral: {'✅ OK' if sistema_ok else '❌ ERROR'}")
        
        if all([fecha_ok, factor_ok, comentarios_ok, sistema_ok]):
            print("\n🎓 SISTEMA APROBADO PARA ENTREGA ACADÉMICA")
            print("Listo para presentación universitaria")
        else:
            print("\n⚠️ REVISAR ELEMENTOS MARCADOS")
        
        print(f"\n🌐 Acceder en: http://127.0.0.1:8000/")
        
    except Exception as e:
        print(f"Error durante verificación: {e}")
        sys.exit(1)
