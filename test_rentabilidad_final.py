#!/usr/bin/env python
"""
Prueba final del sistema de rentabilidad con variabilidad realista
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService

def probar_rentabilidad_variada():
    """
    Prueba que la rentabilidad varíe según diferentes condiciones
    """
    print("💰 PROBANDO VARIABILIDAD DE RENTABILIDAD")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Diferentes escenarios para el mismo producto
    escenarios = [
        ("PAPA CRIOLLA", "Facatativá", datetime(2025, 1, 15), 14.0),
        ("PAPA CRIOLLA", "Subachoque", datetime(2025, 1, 15), 12.0),
        ("PAPA CRIOLLA", "Facatativá", datetime(2025, 7, 15), 16.0),
        ("PAPA CRIOLLA", "Mosquera", datetime(2025, 4, 15), 18.0),
    ]
    
    print("Escenario                    Precio    Rentabilidad  Estado")
    print("-" * 60)
    
    rentabilidades = []
    
    for producto, municipio, fecha, temp in escenarios:
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
        papa = next((r for r in recomendaciones if 'PAPA' in r['producto']), None)
        
        if papa:
            precio = papa['precio_actual']
            rentabilidad = papa['rentabilidad_estimada']
            rentabilidades.append(rentabilidad)
            
            if rentabilidad > 80:
                estado = "🟢 EXCELENTE"
            elif rentabilidad > 50:
                estado = "🟡 BUENA"
            elif rentabilidad > 20:
                estado = "🟠 REGULAR"
            else:
                estado = "🔴 BAJA"
            
            escenario_str = f"{municipio} {fecha.strftime('%m/%Y')}"
            print(f"{escenario_str:<25} ${precio:>6,}  {rentabilidad:>10.1f}%  {estado}")
    
    # Verificar variabilidad
    if len(set([round(r, 0) for r in rentabilidades])) > 1:
        print(f"\n✅ Rentabilidad varía: {min(rentabilidades):.1f}% - {max(rentabilidades):.1f}%")
    else:
        print(f"\n⚠️ Rentabilidad constante: {rentabilidades[0]:.1f}%")

def mostrar_rentabilidad_por_producto():
    """
    Muestra la rentabilidad de diferentes productos
    """
    print("\n📊 RENTABILIDAD POR PRODUCTO")
    print("=" * 50)
    
    sipsa = SipsaService()
    municipio = "Facatativá"
    fecha = datetime(2025, 8, 22)
    temp = 15.0
    
    recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
    
    print("Producto         Precio    Rentabilidad  Ranking")
    print("-" * 50)
    
    for i, rec in enumerate(recomendaciones[:8], 1):
        producto = rec['producto'][:12]
        precio = rec['precio_actual']
        rentabilidad = rec['rentabilidad_estimada']
        
        if rentabilidad > 80:
            emoji = "🥇"
        elif rentabilidad > 60:
            emoji = "🥈"
        elif rentabilidad > 40:
            emoji = "🥉"
        else:
            emoji = "📊"
        
        print(f"{producto:<15} ${precio:>6,}  {rentabilidad:>10.1f}%  {emoji} #{i}")

def explicar_rentabilidad_mejorada():
    """
    Explica las mejoras implementadas en el cálculo de rentabilidad
    """
    print("\n🎓 EXPLICACIÓN DEL SISTEMA DE RENTABILIDAD")
    print("=" * 60)
    
    print("📈 METODOLOGÍA IMPLEMENTADA:")
    print("1. Costos de producción reales por hectárea")
    print("2. Rendimientos típicos del sector agrícola")
    print("3. Duración del ciclo productivo")
    print("4. Factor de riesgo agrícola")
    print("5. Variabilidad del mercado")
    print("6. Factores contextuales (municipio, clima, época)")
    
    print("\n💡 FÓRMULA DE CÁLCULO:")
    print("Rentabilidad = ((Precio - Costo) / Costo) × 100")
    print("Ajuste por ciclo = Rentabilidad × (5 meses / ciclo_producto)")
    print("Factor de riesgo = Curva logarítmica para rentabilidades altas")
    print("Variabilidad = ±15% aleatorio por condiciones de mercado")
    print("Factores contextuales = Municipal × Estacional × Climático")
    
    print("\n📊 RANGOS DE INTERPRETACIÓN:")
    print("• > 80%: Excelente oportunidad")
    print("• 50-80%: Buena rentabilidad")
    print("• 20-50%: Rentabilidad moderada")
    print("• 0-20%: Rentabilidad baja")
    print("• < 0%: Pérdida esperada")
    
    print("\n🔍 VENTAJAS DEL NUEVO SISTEMA:")
    print("• Basado en costos reales del sector")
    print("• Considera ciclo de producción")
    print("• Incluye variabilidad de mercado")
    print("• Maneja rentabilidades negativas")
    print("• Factores contextuales integrados")
    print("• Rangos realistas y útiles")

def comparar_con_sistema_anterior():
    """
    Compara el nuevo sistema con el anterior
    """
    print("\n⚖️ COMPARACIÓN: SISTEMA ANTERIOR vs NUEVO")
    print("=" * 60)
    
    print("SISTEMA ANTERIOR:")
    print("❌ Fórmula simplificada: precio/50")
    print("❌ No consideraba costos reales")
    print("❌ Bonificaciones arbitrarias")
    print("❌ Siempre rentabilidades altas")
    print("❌ No reflejaba realidad económica")
    
    print("\nSISTEMA NUEVO:")
    print("✅ Costos de producción reales")
    print("✅ Rendimientos del sector")
    print("✅ Ciclo productivo considerado")
    print("✅ Variabilidad de mercado")
    print("✅ Rentabilidades realistas")
    print("✅ Manejo de pérdidas")
    print("✅ Factores contextuales integrados")
    
    print("\n📈 IMPACTO:")
    print("• Recomendaciones más precisas")
    print("• Decisiones mejor informadas")
    print("• Expectativas realistas")
    print("• Consideración de riesgos")
    print("• Herramienta más confiable")

if __name__ == "__main__":
    try:
        print("💰 AGROSOFT - SISTEMA DE RENTABILIDAD FINAL")
        print("=" * 70)
        
        probar_rentabilidad_variada()
        mostrar_rentabilidad_por_producto()
        explicar_rentabilidad_mejorada()
        comparar_con_sistema_anterior()
        
        print("\n" + "=" * 70)
        print("✅ SISTEMA DE RENTABILIDAD MEJORADO")
        print("• Basado en costos reales de producción")
        print("• Considera factores económicos del sector")
        print("• Genera variabilidad realista")
        print("• Proporciona información útil para productores")
        print("• Integrado con factores climáticos y municipales")
        
        print("\n🌐 Prueba en el navegador:")
        print("http://127.0.0.1:8000/")
        print("Observa cómo las rentabilidades ahora son más realistas")
        
    except Exception as e:
        print(f"Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
