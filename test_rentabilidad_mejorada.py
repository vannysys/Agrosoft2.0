#!/usr/bin/env python
"""
Prueba del sistema de rentabilidad mejorado con costos reales
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService

def explicar_nueva_rentabilidad():
    """
    Explica cómo funciona el nuevo sistema de rentabilidad
    """
    print("💰 NUEVO SISTEMA DE RENTABILIDAD REALISTA")
    print("=" * 60)
    
    print("📊 METODOLOGÍA:")
    print("• Costos de producción reales por hectárea")
    print("• Rendimientos típicos por cultivo")
    print("• Ciclo de producción considerado")
    print("• Margen bruto = (Precio - Costo) / Costo * 100")
    print("• Ajuste por duración del ciclo")
    
    print("\n💸 COMPONENTES DE COSTO:")
    print("• Semilla/Plántulas")
    print("• Fertilizantes y enmiendas")
    print("• Pesticidas y fungicidas")
    print("• Mano de obra")
    print("• Maquinaria y equipos")
    print("• Otros gastos operativos")

def mostrar_costos_por_producto():
    """
    Muestra los costos de producción por producto
    """
    print("\n📋 COSTOS DE PRODUCCIÓN POR HECTÁREA")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Ejemplos de costos para productos principales
    ejemplos = [
        ("PAPA CRIOLLA", 2800, "18,000 kg/ha", "5 meses"),
        ("CILANTRO", 4800, "8,000 kg/ha", "2 meses"),
        ("LECHUGA", 900, "12,000 kg/ha", "3 meses"),
        ("ZANAHORIA", 1400, "25,000 kg/ha", "4 meses"),
    ]
    
    print("Producto         Precio/kg  Rendimiento   Ciclo    Rentabilidad")
    print("-" * 60)
    
    for producto, precio, rendimiento, ciclo in ejemplos:
        rentabilidad = sipsa._calcular_rentabilidad(precio, producto)
        estado = "✅ VIABLE" if rentabilidad > 20 else "⚠️ RIESGO" if rentabilidad > 0 else "❌ PÉRDIDA"
        
        print(f"{producto:<15} ${precio:>5,}    {rendimiento:<12} {ciclo:<8} {rentabilidad:>6.1f}% {estado}")

def probar_escenarios_rentabilidad():
    """
    Prueba diferentes escenarios de rentabilidad
    """
    print("\n🎯 ESCENARIOS DE RENTABILIDAD")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    escenarios = [
        ("PAPA CRIOLLA", "Facatativá", datetime(2025, 1, 15), 14.0, "Condiciones ideales"),
        ("PAPA CRIOLLA", "Mosquera", datetime(2025, 7, 15), 16.0, "Condiciones regulares"),
        ("CILANTRO", "Subachoque", datetime(2025, 4, 15), 18.0, "Época favorable"),
        ("LECHUGA", "Madrid", datetime(2025, 10, 15), 12.0, "Clima fresco"),
    ]
    
    for producto, municipio, fecha, temp, descripcion in escenarios:
        print(f"\n📍 {producto} en {municipio} ({descripcion})")
        print("-" * 40)
        
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
        
        producto_encontrado = next((r for r in recomendaciones if producto in r['producto']), None)
        
        if producto_encontrado:
            rentabilidad = producto_encontrado['rentabilidad_estimada']
            precio = producto_encontrado['precio_actual']
            
            # Calcular rentabilidad base para comparar
            rentabilidad_base = sipsa._calcular_rentabilidad(precio, producto)
            
            print(f"Precio actual: ${precio:,}/kg")
            print(f"Rentabilidad base: {rentabilidad_base:.1f}%")
            print(f"Rentabilidad ajustada: {rentabilidad:.1f}%")
            
            if rentabilidad > 50:
                print("🟢 MUY RENTABLE - Excelente oportunidad")
            elif rentabilidad > 20:
                print("🟡 RENTABLE - Buena opción")
            elif rentabilidad > 0:
                print("🟠 MARGINAL - Evaluar riesgos")
            else:
                print("🔴 NO RENTABLE - Evitar")

def comparar_rentabilidad_anterior():
    """
    Compara la nueva rentabilidad con la anterior
    """
    print("\n📊 COMPARACIÓN: ANTES vs DESPUÉS")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    productos_test = ["PAPA CRIOLLA", "CILANTRO", "LECHUGA", "ZANAHORIA"]
    precios_test = [2800, 4800, 900, 1400]
    
    print("Producto         Precio    Antes    Después   Diferencia")
    print("-" * 55)
    
    for producto, precio in zip(productos_test, precios_test):
        # Rentabilidad anterior (simplificada)
        rent_anterior = min(precio / 50, 100)
        if precio > 3000:
            rent_anterior *= 1.2
        elif precio > 2000:
            rent_anterior *= 1.1
        rent_anterior = min(rent_anterior, 100)
        
        # Rentabilidad nueva (realista)
        rent_nueva = sipsa._calcular_rentabilidad(precio, producto)
        
        diferencia = rent_nueva - rent_anterior
        simbolo = "📈" if diferencia > 0 else "📉" if diferencia < 0 else "➡️"
        
        print(f"{producto:<15} ${precio:>5,}  {rent_anterior:>6.1f}%  {rent_nueva:>7.1f}%  {simbolo} {diferencia:>+6.1f}%")

def mostrar_interpretacion_rentabilidad():
    """
    Explica cómo interpretar los nuevos valores de rentabilidad
    """
    print("\n📖 INTERPRETACIÓN DE RENTABILIDAD")
    print("=" * 50)
    
    print("🟢 RENTABILIDAD > 50%:")
    print("   • Excelente oportunidad de inversión")
    print("   • Margen alto que compensa riesgos")
    print("   • Recomendado para productores experimentados")
    
    print("\n🟡 RENTABILIDAD 20-50%:")
    print("   • Buena rentabilidad, inversión segura")
    print("   • Margen adecuado para sostenibilidad")
    print("   • Ideal para productores establecidos")
    
    print("\n🟠 RENTABILIDAD 0-20%:")
    print("   • Rentabilidad marginal, evaluar riesgos")
    print("   • Considerar eficiencias operativas")
    print("   • Solo para productores con experiencia")
    
    print("\n🔴 RENTABILIDAD < 0%:")
    print("   • Pérdida esperada, evitar cultivo")
    print("   • Costos superan ingresos proyectados")
    print("   • Buscar alternativas más rentables")
    
    print("\n💡 FACTORES QUE AFECTAN:")
    print("• Precio de venta en el mercado")
    print("• Costos de insumos y mano de obra")
    print("• Rendimiento por hectárea")
    print("• Duración del ciclo productivo")
    print("• Condiciones climáticas")
    print("• Ventajas del municipio")
    print("• Época de siembra")

if __name__ == "__main__":
    try:
        print("💰 AGROSOFT - SISTEMA DE RENTABILIDAD MEJORADO")
        print("=" * 70)
        
        explicar_nueva_rentabilidad()
        mostrar_costos_por_producto()
        probar_escenarios_rentabilidad()
        comparar_rentabilidad_anterior()
        mostrar_interpretacion_rentabilidad()
        
        print("\n" + "=" * 70)
        print("✅ MEJORAS IMPLEMENTADAS:")
        print("• Costos de producción reales por cultivo")
        print("• Rendimientos basados en datos del sector")
        print("• Consideración del ciclo productivo")
        print("• Manejo de rentabilidades negativas")
        print("• Rangos realistas (-50% a +200%)")
        print("• Interpretación clara para productores")
        
        print("\n🌐 Prueba en el navegador para ver los cambios:")
        print("http://127.0.0.1:8000/")
        
    except Exception as e:
        print(f"Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
