#!/usr/bin/env python
"""
Script para probar la conexión con datos reales del SIPSA
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

def probar_datos_reales():
    """
    Prueba la conexión con datos reales del SIPSA
    """
    print("🔍 PROBANDO DATOS REALES DEL SIPSA")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    # Forzar uso de datos reales
    sipsa.use_real_data = True
    
    try:
        print("🔄 Intentando obtener datos reales...")
        precios = sipsa.obtener_precios_actuales(limit=20)
        
        if precios:
            print(f"✅ ¡Éxito! Se obtuvieron {len(precios)} registros reales")
            
            print("\n📊 PRIMEROS 5 PRODUCTOS REALES:")
            print("-" * 40)
            
            for i, precio in enumerate(precios[:5]):
                print(f"{i+1}. {precio['producto']}")
                print(f"   💰 Precio: ${precio['precio_mayorista']:,}")
                print(f"   🏪 Mercado: {precio['mercado']}")
                print(f"   📅 Fecha: {precio['fecha']}")
                print(f"   📦 Presentación: {precio['presentacion']}")
                print()
            
            # Probar recomendaciones con datos reales
            print("🎯 PROBANDO RECOMENDACIONES CON DATOS REALES:")
            print("-" * 50)
            
            recomendaciones = sipsa.obtener_productos_recomendados("Facatativá", datetime.now(), 18.5)
            
            if recomendaciones:
                print(f"✅ Se generaron {len(recomendaciones)} recomendaciones")
                
                print("\n🏆 TOP 3 RECOMENDACIONES:")
                for i, rec in enumerate(recomendaciones[:3], 1):
                    print(f"{i}. {rec['producto']}")
                    print(f"   💰 Precio: ${rec['precio_actual']:,}")
                    print(f"   📈 Tendencia: {rec['tendencia']}")
                    print(f"   ⭐ Rentabilidad: {rec['rentabilidad_estimada']:.1f}%")
                    print(f"   🏘️ Factor Municipal: {rec['municipio_factor']:.2f}x")
                    print(f"   🌡️ Factor Climático: {rec['clima_factor']:.2f}x")
                    print()
            else:
                print("❌ No se pudieron generar recomendaciones")
        else:
            print("❌ No se obtuvieron datos reales")
            
    except Exception as e:
        print(f"💥 Error al obtener datos reales: {e}")
        print("\n🔄 Probando fallback a datos simulados...")
        
        # Probar fallback
        sipsa.use_real_data = False
        precios_simulados = sipsa.obtener_precios_actuales(limit=5)
        
        if precios_simulados:
            print(f"✅ Fallback exitoso: {len(precios_simulados)} registros simulados")
            print("\n📊 DATOS SIMULADOS (FALLBACK):")
            for i, precio in enumerate(precios_simulados[:3]):
                print(f"{i+1}. {precio['producto']} - ${precio['precio_mayorista']:,}")
        else:
            print("❌ Falló también el fallback")

def probar_estructura_csv():
    """
    Prueba directa del CSV para entender su estructura
    """
    print("\n\n🔍 ANALIZANDO ESTRUCTURA DEL CSV")
    print("=" * 50)
    
    import requests
    import csv
    import io
    
    try:
        url = "https://www.datos.gov.co/api/views/wspg-shym/rows.csv?accessType=DOWNLOAD&api_foundry=true"
        print(f"📡 Descargando desde: {url}")
        
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Leer primeras líneas para entender estructura
        csv_data = response.text
        lines = csv_data.split('\n')
        
        print(f"✅ Descarga exitosa: {len(lines)} líneas")
        
        if len(lines) > 0:
            print(f"\n📋 ENCABEZADOS:")
            headers = lines[0].split(',')
            for i, header in enumerate(headers):
                print(f"  {i}: {header.strip()}")
            
            print(f"\n📄 PRIMERA FILA DE DATOS:")
            if len(lines) > 1:
                first_row = lines[1].split(',')
                for i, value in enumerate(first_row):
                    if i < len(headers):
                        print(f"  {headers[i].strip()}: {value.strip()}")
        
    except Exception as e:
        print(f"💥 Error analizando CSV: {e}")

def mostrar_configuracion():
    """
    Muestra la configuración actual del sistema
    """
    print("\n\n⚙️ CONFIGURACIÓN DEL SISTEMA")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    print(f"🔗 URL SIPSA: {sipsa.SIPSA_API_URL}")
    print(f"📊 Usar datos reales: {sipsa.use_real_data}")
    print(f"⏰ Duración cache: {sipsa.cache_duration} segundos")
    print(f"💾 Cache válido: {sipsa._is_cache_valid()}")
    
    if sipsa._cached_data:
        print(f"📈 Registros en cache: {len(sipsa._cached_data)}")
    else:
        print("📈 Cache vacío")

if __name__ == "__main__":
    try:
        print("🚀 PRUEBA COMPLETA DE DATOS REALES")
        print("=" * 60)
        
        mostrar_configuracion()
        probar_estructura_csv()
        probar_datos_reales()
        
        print("\n\n✅ RESUMEN:")
        print("• Sistema configurado para usar datos reales del SIPSA")
        print("• Fallback automático a datos simulados si falla")
        print("• Cache implementado para mejorar rendimiento")
        print("• Nueva columna de clima agregada")
        print("\n🌐 Prueba en el navegador para ver los datos reales!")
        
    except Exception as e:
        print(f"💥 Error durante la prueba: {e}")
        sys.exit(1)
