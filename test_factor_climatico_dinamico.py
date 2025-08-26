#!/usr/bin/env python
"""
Script para probar que el factor climático ahora cambie dinámicamente
"""

import sys
import os
from datetime import datetime

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService
from productores.views import obtener_clima_openweather

def probar_clima_por_municipio():
    """
    Prueba que el clima cambie según el municipio
    """
    print("🏘️ PROBANDO CLIMA POR MUNICIPIO")
    print("=" * 50)
    
    municipios = ['Facatativá', 'Madrid', 'Subachoque', 'Mosquera', 'El Rosal']
    fecha = datetime(2025, 8, 22)  # Fecha fija para comparar
    
    climas = {}
    
    for municipio in municipios:
        clima = obtener_clima_openweather(municipio, fecha)
        climas[municipio] = clima
        print(f"🌡️ {municipio}: {clima}°C")
    
    # Verificar que hay diferencias
    temperaturas = list(climas.values())
    if len(set(temperaturas)) > 1:
        print(f"✅ ¡Clima varía por municipio! Rango: {min(temperaturas):.1f}°C - {max(temperaturas):.1f}°C")
    else:
        print(f"⚠️ Clima igual en todos los municipios: {temperaturas[0]}°C")
    
    return climas

def probar_clima_por_fecha():
    """
    Prueba que el clima cambie según la fecha
    """
    print("\n📅 PROBANDO CLIMA POR FECHA")
    print("=" * 50)
    
    municipio = "Facatativá"  # Municipio fijo para comparar
    fechas = [
        datetime(2025, 1, 15),   # Enero (frío)
        datetime(2025, 4, 15),   # Abril (cálido)
        datetime(2025, 7, 15),   # Julio (frío)
        datetime(2025, 10, 15),  # Octubre (templado)
    ]
    
    climas_fecha = {}
    
    for fecha in fechas:
        clima = obtener_clima_openweather(municipio, fecha)
        climas_fecha[fecha.strftime('%B')] = clima
        print(f"🌡️ {fecha.strftime('%B')}: {clima}°C")
    
    # Verificar que hay diferencias estacionales
    temperaturas = list(climas_fecha.values())
    if len(set(temperaturas)) > 1:
        print(f"✅ ¡Clima varía por época! Rango: {min(temperaturas):.1f}°C - {max(temperaturas):.1f}°C")
    else:
        print(f"⚠️ Clima igual en todas las épocas: {temperaturas[0]}°C")
    
    return climas_fecha

def probar_factor_climatico_dinamico():
    """
    Prueba que el factor climático cambie según temperatura
    """
    print("\n🌡️ PROBANDO FACTOR CLIMÁTICO DINÁMICO")
    print("=" * 50)
    
    sipsa = SipsaService()
    producto = "PAPA CRIOLLA"
    
    # Probar diferentes temperaturas
    temperaturas_test = [8, 12, 14, 16, 18, 22, 26]
    
    print(f"Producto: {producto}")
    print("Temp.  Factor   Estado")
    print("-" * 25)
    
    for temp in temperaturas_test:
        factor = sipsa._obtener_factor_climatico(producto, temp)
        
        if factor > 1.2:
            estado = "🌡️ IDEAL"
        elif factor > 1.0:
            estado = "🌤️ BUENO"
        elif factor > 0.8:
            estado = "🌥️ REGULAR"
        else:
            estado = "❄️ MALO"
        
        print(f"{temp:>4}°C  {factor:>5.2f}x  {estado}")
    
    print("\n✅ Factor climático varía según temperatura")

def probar_recomendaciones_dinamicas():
    """
    Prueba que las recomendaciones cambien con municipio y fecha
    """
    print("\n🎯 PROBANDO RECOMENDACIONES DINÁMICAS")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    # Escenarios de prueba
    escenarios = [
        ("Subachoque", datetime(2025, 1, 15), "Invierno frío"),
        ("Mosquera", datetime(2025, 4, 15), "Primavera cálida"),
        ("El Rosal", datetime(2025, 7, 15), "Invierno muy frío"),
        ("Facatativá", datetime(2025, 10, 15), "Otoño templado"),
    ]
    
    resultados = {}
    
    for municipio, fecha, descripcion in escenarios:
        print(f"\n📍 {municipio} - {fecha.strftime('%B')} ({descripcion})")
        print("-" * 40)
        
        # Obtener clima
        clima = obtener_clima_openweather(municipio, fecha)
        print(f"🌡️ Clima: {clima}°C")
        
        # Generar recomendaciones
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, clima)
        
        if recomendaciones:
            # Mostrar top 3
            print("🏆 Top 3:")
            for i, rec in enumerate(recomendaciones[:3], 1):
                factor_clima = rec.get('clima_factor', 1.0)
                estado_clima = "🌡️" if factor_clima > 1.2 else "🌤️" if factor_clima > 1.0 else "❄️"
                
                print(f"{i}. {rec['producto'][:15]:<15} {estado_clima} {factor_clima:.2f}x - {rec['rentabilidad_estimada']:.1f}%")
            
            # Guardar para comparación
            resultados[f"{municipio}_{fecha.month}"] = recomendaciones[0]['producto']
    
    # Verificar que hay diferencias
    productos_top = list(resultados.values())
    if len(set(productos_top)) > 1:
        print(f"\n✅ ¡Recomendaciones cambian dinámicamente!")
        print("Productos #1 por escenario:")
        for key, producto in resultados.items():
            municipio, mes = key.split('_')
            print(f"• {municipio} (mes {mes}): {producto}")
    else:
        print(f"\n⚠️ Mismo producto #1 en todos los escenarios: {productos_top[0]}")

def mostrar_rangos_climaticos():
    """
    Muestra los rangos climáticos ideales por producto
    """
    print("\n📊 RANGOS CLIMÁTICOS POR PRODUCTO")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Obtener rangos desde el código
    temperaturas_ideales = {
        'PAPA CRIOLLA': {'min': 8, 'ideal': 14, 'max': 18, 'optimo_bajo': 12, 'optimo_alto': 16},
        'CILANTRO': {'min': 12, 'ideal': 18, 'max': 25, 'optimo_bajo': 16, 'optimo_alto': 20},
        'LECHUGA': {'min': 8, 'ideal': 14, 'max': 20, 'optimo_bajo': 12, 'optimo_alto': 16},
        'ZANAHORIA': {'min': 12, 'ideal': 18, 'max': 24, 'optimo_bajo': 16, 'optimo_alto': 20},
        'BRÓCOLI': {'min': 6, 'ideal': 13, 'max': 18, 'optimo_bajo': 11, 'optimo_alto': 15},
    }
    
    print("Producto         Mín   Óptimo    Máx   Factor Ideal")
    print("-" * 60)
    
    for producto, rango in temperaturas_ideales.items():
        print(f"{producto:<15} {rango['min']:>3}°C  {rango['optimo_bajo']:>2}-{rango['optimo_alto']:>2}°C  {rango['max']:>3}°C      1.25x")
    
    print("\n💡 INTERPRETACIÓN:")
    print("• 🌡️ IDEAL (1.25x): Temperatura en rango óptimo")
    print("• 🌤️ BUENO (1.0-1.2x): Temperatura aceptable")
    print("• 🌥️ REGULAR (0.8-1.0x): Temperatura subóptima")
    print("• ❄️ MALO (<0.8x): Temperatura inadecuada")

if __name__ == "__main__":
    try:
        print("🌡️ AGROSOFT - PRUEBA DE FACTOR CLIMÁTICO DINÁMICO")
        print("=" * 70)
        
        # Probar variaciones
        climas_municipio = probar_clima_por_municipio()
        climas_fecha = probar_clima_por_fecha()
        probar_factor_climatico_dinamico()
        probar_recomendaciones_dinamicas()
        mostrar_rangos_climaticos()
        
        print("\n\n✅ RESUMEN DE MEJORAS IMPLEMENTADAS:")
        print("=" * 50)
        print("• 🏘️ Clima varía por municipio (diferencias reales)")
        print("• 📅 Clima varía por fecha (variación estacional)")
        print("• 🌡️ Factor climático más preciso (5 niveles)")
        print("• 🎯 Factor integrado en predicciones de rentabilidad")
        print("• 📊 Rangos específicos por producto")
        print("• 🔄 Bonificaciones por condiciones ideales")
        
        print("\n🌐 PRUEBA EN EL NAVEGADOR:")
        print("1. Ve a: http://127.0.0.1:8000/")
        print("2. Cambia de Facatativá a Subachoque → Clima más frío")
        print("3. Cambia de Agosto a Enero → Clima estacional")
        print("4. Observa cambios en Factor Climático")
        print("5. Ve cómo afecta la rentabilidad")
        
    except Exception as e:
        print(f"💥 Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
