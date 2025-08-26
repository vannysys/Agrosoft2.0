#!/usr/bin/env python
"""
Script para demostrar cómo los cambios de municipio y fecha afectan las recomendaciones
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

def comparar_municipios():
    """
    Compara recomendaciones entre diferentes municipios
    """
    print("🏘️ COMPARACIÓN POR MUNICIPIOS")
    print("=" * 50)
    
    sipsa = SipsaService()
    fecha_fija = datetime(2025, 9, 15)  # Fecha fija para comparar
    
    municipios = ['Facatativá', 'Madrid', 'Subachoque']
    
    for municipio in municipios:
        print(f"\n📍 {municipio.upper()}")
        print("-" * 30)
        
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha_fija)
        
        # Mostrar top 3
        for i, rec in enumerate(recomendaciones[:3], 1):
            factor = rec.get('municipio_factor', 1.0)
            estado = "🟢 Favorable" if factor > 1.05 else "🔴 Desafiante" if factor < 0.95 else "🟡 Neutral"
            print(f"{i}. {rec['producto']}: ${rec['precio_actual']} - {rec['tendencia']} - {estado}")

def comparar_fechas():
    """
    Compara recomendaciones entre diferentes fechas
    """
    print("\n\n📅 COMPARACIÓN POR FECHAS")
    print("=" * 50)
    
    sipsa = SipsaService()
    municipio_fijo = 'Facatativá'
    
    fechas = [
        datetime(2025, 3, 15),   # Marzo
        datetime(2025, 7, 15),   # Julio  
        datetime(2025, 11, 15),  # Noviembre
    ]
    
    for fecha in fechas:
        print(f"\n📆 {fecha.strftime('%B %Y').upper()}")
        print("-" * 30)
        
        recomendaciones = sipsa.obtener_productos_recomendados(municipio_fijo, fecha)
        
        # Mostrar top 3
        for i, rec in enumerate(recomendaciones[:3], 1):
            print(f"{i}. {rec['producto']}: ${rec['precio_actual']} - {rec['tendencia']} - {rec['rentabilidad_estimada']:.1f}%")

def demostrar_producto_especifico():
    """
    Muestra cómo un producto específico cambia según contexto
    """
    print("\n\n🥔 PAPA CRIOLLA EN DIFERENTES CONTEXTOS")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    contextos = [
        ('Facatativá', datetime(2025, 3, 15)),
        ('Subachoque', datetime(2025, 3, 15)),
        ('Facatativá', datetime(2025, 8, 15)),
        ('Subachoque', datetime(2025, 8, 15)),
    ]
    
    for municipio, fecha in contextos:
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha)
        
        # Buscar Papa Criolla
        papa_criolla = next((r for r in recomendaciones if 'PAPA CRIOLLA' in r['producto']), None)
        
        if papa_criolla:
            factor = papa_criolla.get('municipio_factor', 1.0)
            print(f"{municipio} - {fecha.strftime('%B')}: ${papa_criolla['precio_actual']} (Factor: {factor:.2f}x)")

if __name__ == "__main__":
    try:
        print("🧪 DEMOSTRANDO CAMBIOS DINÁMICOS EN AGROSOFT")
        print("=" * 60)
        
        comparar_municipios()
        comparar_fechas()
        demostrar_producto_especifico()
        
        print("\n\n✅ CONCLUSIÓN:")
        print("Los datos ahora cambian dinámicamente según:")
        print("• 🏘️ Municipio seleccionado (cada uno tiene ventajas para diferentes productos)")
        print("• 📅 Fecha de siembra (factores estacionales)")
        print("• 🌱 Combinación de ambos factores")
        print("\n🌐 Prueba en el navegador cambiando municipio y fecha para ver las diferencias!")
        
    except Exception as e:
        print(f"💥 Error durante la demostración: {e}")
        sys.exit(1)
