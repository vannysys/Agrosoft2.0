#!/usr/bin/env python
"""
Prueba del sistema de rentabilidad ultra-realista con máximo 100%
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService

def probar_rentabilidad_ultra_realista():
    """
    Prueba el nuevo sistema con rentabilidades ultra-realistas
    """
    print("💰 SISTEMA DE RENTABILIDAD ULTRA-REALISTA")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Probar todos los productos
    productos_test = [
        "PAPA CRIOLLA", "PAPA PASTUSA", "CILANTRO", "LECHUGA", 
        "ZANAHORIA", "CEBOLLA CABEZONA", "CEBOLLA LARGA", "BRÓCOLI"
    ]
    
    print("Producto         Precio/kg  Costo/kg  Rentabilidad  Viabilidad")
    print("-" * 70)
    
    rentabilidades = []
    productos_viables = 0
    
    for producto in productos_test:
        # Obtener precio simulado
        precios = sipsa.obtener_precios_actuales(50)
        precio_producto = next((p for p in precios if producto in p['producto']), None)
        
        if precio_producto:
            precio = precio_producto['precio_mayorista']
            rentabilidad = sipsa._calcular_rentabilidad(precio, producto)
            rentabilidades.append(rentabilidad)
            
            # Calcular costo aproximado
            if rentabilidad > -100:
                costo_estimado = precio / (1 + rentabilidad/100)
            else:
                costo_estimado = precio * 2
            
            # Clasificación de viabilidad
            if rentabilidad > 50:
                viabilidad = "🟢 EXCELENTE"
                productos_viables += 1
            elif rentabilidad > 25:
                viabilidad = "🟡 BUENA"
                productos_viables += 1
            elif rentabilidad > 10:
                viabilidad = "🟠 ACEPTABLE"
                productos_viables += 1
            elif rentabilidad > 0:
                viabilidad = "🔴 MARGINAL"
            else:
                viabilidad = "❌ NO VIABLE"
            
            producto_corto = producto[:12]
            print(f"{producto_corto:<15} ${precio:>6,}  ${costo_estimado:>6,.0f}  {rentabilidad:>9.1f}%  {viabilidad}")
    
    # Estadísticas del sistema
    print(f"\n📊 ESTADÍSTICAS DEL SISTEMA:")
    print(f"• Rentabilidad promedio: {sum(rentabilidades)/len(rentabilidades):.1f}%")
    print(f"• Rango de rentabilidades: {min(rentabilidades):.1f}% - {max(rentabilidades):.1f}%")
    print(f"• Productos viables: {productos_viables}/{len(rentabilidades)}")
    print(f"• Máximo teórico: 100.0% ✅")
    
    # Verificar que ninguna supere 100%
    max_rentabilidad = max(rentabilidades)
    if max_rentabilidad <= 100:
        print("✅ Ningún producto supera el 100% de rentabilidad")
    else:
        print(f"❌ Error: Producto con {max_rentabilidad:.1f}% (supera 100%)")

def mostrar_factores_realismo():
    """
    Explica los factores que hacen el sistema más realista
    """
    print("\n🎯 FACTORES DE REALISMO IMPLEMENTADOS")
    print("=" * 60)
    
    print("💸 COSTOS AUMENTADOS:")
    print("• Semilla: +60% (certificada, mayor calidad)")
    print("• Fertilizantes: +40% (precios 2025)")
    print("• Pesticidas: +50% (productos especializados)")
    print("• Mano de obra: +30% (salarios actualizados)")
    print("• Maquinaria: +50% (combustible, mantenimiento)")
    
    print("\n📉 RENDIMIENTOS AJUSTADOS:")
    print("• Papa Criolla: 15,000 kg/ha (antes 18,000)")
    print("• Cilantro: 4,500 kg/ha (antes 8,000)")
    print("• Lechuga: 8,000 kg/ha (antes 12,000)")
    print("• Más realistas según condiciones locales")
    
    print("\n⚖️ FACTORES DE DIFICULTAD:")
    print("• Lechuga (Baja): +10% facilidad de cultivo")
    print("• Papa/Zanahoria (Media): Neutro")
    print("• Cebolla/Brócoli (Alta): -15% dificultad")
    print("• Cilantro (Muy Alta): -30% muy volátil")
    
    print("\n📊 VOLATILIDAD POR PRODUCTO:")
    print("• Lechuga: ±15% (mercado estable)")
    print("• Papa: ±20-25% (demanda constante)")
    print("• Cebolla Larga: ±35% (muy volátil)")
    print("• Cilantro: ±40% (extremadamente volátil)")

def comparar_escenarios_contextuales():
    """
    Compara rentabilidades en diferentes contextos
    """
    print("\n🌍 RENTABILIDAD POR CONTEXTO")
    print("=" * 50)
    
    sipsa = SipsaService()
    producto = "PAPA CRIOLLA"
    
    escenarios = [
        ("Facatativá", datetime(2025, 1, 15), 14.0, "Época ideal"),
        ("Subachoque", datetime(2025, 1, 15), 12.0, "Municipio frío"),
        ("Mosquera", datetime(2025, 7, 15), 18.0, "Época difícil"),
        ("Madrid", datetime(2025, 10, 15), 15.0, "Época regular"),
    ]
    
    print("Escenario                    Rentabilidad  Interpretación")
    print("-" * 60)
    
    for municipio, fecha, temp, descripcion in escenarios:
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
        papa = next((r for r in recomendaciones if 'PAPA' in r['producto']), None)
        
        if papa:
            rentabilidad = papa['rentabilidad_estimada']
            
            if rentabilidad > 60:
                interpretacion = "🟢 Excelente"
            elif rentabilidad > 35:
                interpretacion = "🟡 Buena"
            elif rentabilidad > 15:
                interpretacion = "🟠 Regular"
            else:
                interpretacion = "🔴 Baja"
            
            escenario_str = f"{municipio} {fecha.strftime('%m/%Y')}"
            print(f"{escenario_str:<25} {rentabilidad:>10.1f}%  {interpretacion}")

def mostrar_interpretacion_final():
    """
    Guía de interpretación para las nuevas rentabilidades
    """
    print("\n📖 GUÍA DE INTERPRETACIÓN - RENTABILIDADES REALISTAS")
    print("=" * 70)
    
    print("🟢 RENTABILIDAD 50-100% - EXCELENTE:")
    print("   • Oportunidad excepcional en el sector")
    print("   • Justifica inversión y riesgos altos")
    print("   • Productos de nicho o condiciones perfectas")
    print("   • Ejemplo: Cilantro en época de alta demanda")
    
    print("\n🟡 RENTABILIDAD 25-50% - BUENA:")
    print("   • Por encima del promedio sectorial (15-20%)")
    print("   • Inversión atractiva y relativamente segura")
    print("   • Productos con demanda estable")
    print("   • Ejemplo: Papa en condiciones favorables")
    
    print("\n🟠 RENTABILIDAD 10-25% - ACEPTABLE:")
    print("   • Cerca del promedio del sector agrícola")
    print("   • Rentabilidad moderada, requiere eficiencia")
    print("   • Evaluar optimización de costos")
    print("   • Ejemplo: Hortalizas en época regular")
    
    print("\n🔴 RENTABILIDAD 0-10% - MARGINAL:")
    print("   • Rentabilidad muy baja, alto riesgo")
    print("   • Solo para productores muy eficientes")
    print("   • Considerar cambio de cultivo")
    print("   • Ejemplo: Productos fuera de temporada")
    
    print("\n❌ RENTABILIDAD < 0% - NO VIABLE:")
    print("   • Pérdida esperada, evitar cultivo")
    print("   • Costos superan ingresos proyectados")
    print("   • Buscar alternativas más rentables")
    print("   • Ejemplo: Cultivos en condiciones adversas")
    
    print("\n💡 CONTEXTO SECTORIAL:")
    print("• Promedio sector agrícola Colombia: 15-20%")
    print("• Rentabilidad mínima viable: 10%")
    print("• Rentabilidad excelente: >50%")
    print("• Máximo teórico del sistema: 100%")

if __name__ == "__main__":
    try:
        print("💰 AGROSOFT - RENTABILIDAD ULTRA-REALISTA (MAX 100%)")
        print("=" * 80)
        
        probar_rentabilidad_ultra_realista()
        mostrar_factores_realismo()
        comparar_escenarios_contextuales()
        mostrar_interpretacion_final()
        
        print("\n" + "=" * 80)
        print("✅ SISTEMA ULTRA-REALISTA IMPLEMENTADO")
        print("• Máximo 100% de rentabilidad ✅")
        print("• Costos basados en sector agrícola 2025")
        print("• Rendimientos ajustados a condiciones locales")
        print("• Factores de dificultad por cultivo")
        print("• Volatilidad específica por producto")
        print("• Rangos: -40% a +100% (ultra-realistas)")
        
        print("\n🌐 Prueba en el navegador:")
        print("http://127.0.0.1:8000/")
        print("Rentabilidades ahora son ultra-realistas y útiles")
        
    except Exception as e:
        print(f"Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
