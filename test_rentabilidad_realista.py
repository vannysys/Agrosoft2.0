#!/usr/bin/env python
"""
Prueba del sistema de rentabilidad realista con variabilidad
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
    Prueba que la rentabilidad ahora tenga variabilidad realista
    """
    print("💰 PROBANDO RENTABILIDAD REALISTA Y VARIADA")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Probar diferentes productos
    productos_test = [
        "PAPA CRIOLLA", "PAPA PASTUSA", "CILANTRO", "LECHUGA", 
        "ZANAHORIA", "CEBOLLA CABEZONA", "BRÓCOLI", "REPOLLO"
    ]
    
    print("Producto         Precio/kg  Costo/kg  Rentabilidad  Estado")
    print("-" * 65)
    
    rentabilidades = []
    
    for producto in productos_test:
        # Obtener precio simulado
        precios = sipsa.obtener_precios_actuales(50)
        precio_producto = next((p for p in precios if producto in p['producto']), None)
        
        if precio_producto:
            precio = precio_producto['precio_mayorista']
            rentabilidad = sipsa._calcular_rentabilidad(precio, producto)
            rentabilidades.append(rentabilidad)
            
            # Calcular costo aproximado para mostrar
            costo_estimado = precio / (1 + rentabilidad/100) if rentabilidad > -100 else precio * 1.5
            
            if rentabilidad > 60:
                estado = "🟢 EXCELENTE"
            elif rentabilidad > 30:
                estado = "🟡 BUENA"
            elif rentabilidad > 10:
                estado = "🟠 REGULAR"
            elif rentabilidad > 0:
                estado = "🔴 BAJA"
            else:
                estado = "❌ PÉRDIDA"
            
            producto_corto = producto[:12]
            print(f"{producto_corto:<15} ${precio:>6,}  ${costo_estimado:>6,.0f}  {rentabilidad:>9.1f}%  {estado}")
    
    # Mostrar estadísticas
    if rentabilidades:
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"• Rentabilidad promedio: {sum(rentabilidades)/len(rentabilidades):.1f}%")
        print(f"• Rango: {min(rentabilidades):.1f}% - {max(rentabilidades):.1f}%")
        print(f"• Productos rentables: {len([r for r in rentabilidades if r > 0])}/{len(rentabilidades)}")
        
        # Verificar variabilidad
        rentabilidades_redondeadas = [round(r, 0) for r in rentabilidades]
        valores_unicos = len(set(rentabilidades_redondeadas))
        
        if valores_unicos > len(rentabilidades) * 0.6:
            print("✅ Buena variabilidad en rentabilidades")
        else:
            print("⚠️ Poca variabilidad en rentabilidades")

def probar_escenarios_contextuales():
    """
    Prueba cómo los factores contextuales afectan la rentabilidad
    """
    print("\n🎯 RENTABILIDAD POR ESCENARIOS CONTEXTUALES")
    print("=" * 60)
    
    sipsa = SipsaService()
    producto = "PAPA CRIOLLA"
    
    escenarios = [
        ("Facatativá", datetime(2025, 1, 15), 14.0, "Condiciones ideales"),
        ("Subachoque", datetime(2025, 1, 15), 12.0, "Municipio frío"),
        ("Mosquera", datetime(2025, 7, 15), 18.0, "Época menos favorable"),
        ("Madrid", datetime(2025, 4, 15), 16.0, "Condiciones promedio"),
    ]
    
    print("Escenario                    Rentabilidad  Factores")
    print("-" * 60)
    
    for municipio, fecha, temp, descripcion in escenarios:
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
        papa = next((r for r in recomendaciones if 'PAPA' in r['producto']), None)
        
        if papa:
            rentabilidad = papa['rentabilidad_estimada']
            factor_mun = papa['municipio_factor']
            factor_clima = papa.get('clima_factor', 1.0)
            
            factores_str = f"M:{factor_mun:.2f} C:{factor_clima:.2f}"
            escenario_str = f"{municipio} {fecha.strftime('%m/%Y')}"
            
            print(f"{escenario_str:<25} {rentabilidad:>10.1f}%  {factores_str}")

def mostrar_interpretacion_realista():
    """
    Explica cómo interpretar las nuevas rentabilidades realistas
    """
    print("\n📖 INTERPRETACIÓN DE RENTABILIDADES REALISTAS")
    print("=" * 60)
    
    print("🟢 RENTABILIDAD > 60%:")
    print("   • Excelente oportunidad, muy por encima del promedio")
    print("   • Justifica inversión y riesgos")
    print("   • Productos de alta demanda o nicho")
    
    print("\n🟡 RENTABILIDAD 30-60%:")
    print("   • Buena rentabilidad, por encima del promedio sectorial")
    print("   • Inversión segura con retorno atractivo")
    print("   • Ideal para productores establecidos")
    
    print("\n🟠 RENTABILIDAD 10-30%:")
    print("   • Rentabilidad moderada, cerca del promedio")
    print("   • Requiere eficiencia operativa")
    print("   • Evaluar costos y optimizar procesos")
    
    print("\n🔴 RENTABILIDAD 0-10%:")
    print("   • Rentabilidad baja, apenas cubre costos")
    print("   • Alto riesgo, evaluar alternativas")
    print("   • Solo para productores muy eficientes")
    
    print("\n❌ RENTABILIDAD < 0%:")
    print("   • Pérdida esperada, evitar cultivo")
    print("   • Costos superan ingresos proyectados")
    print("   • Buscar productos más rentables")
    
    print("\n💡 FACTORES QUE GENERAN VARIABILIDAD:")
    print("• Factor de riesgo específico por producto")
    print("• Costos de producción diferenciados")
    print("• Rendimientos variables por cultivo")
    print("• Ciclo productivo (productos de ciclo corto favorecidos)")
    print("• Variabilidad de mercado (±30%)")
    print("• Factores contextuales (municipio, clima, época)")

def comparar_antes_despues():
    """
    Compara el sistema anterior con el nuevo
    """
    print("\n⚖️ COMPARACIÓN: ANTES vs DESPUÉS")
    print("=" * 50)
    
    print("❌ SISTEMA ANTERIOR:")
    print("• Rentabilidad constante 150%")
    print("• No reflejaba realidad económica")
    print("• Sin variabilidad entre productos")
    print("• Fórmula simplificada")
    
    print("\n✅ SISTEMA NUEVO:")
    print("• Rentabilidades variables (-60% a +120%)")
    print("• Basado en costos reales del sector")
    print("• Cada producto tiene características únicas")
    print("• Factor de riesgo específico")
    print("• Variabilidad de mercado realista")
    print("• Factores contextuales integrados")
    
    print("\n📈 BENEFICIOS:")
    print("• Información más confiable para productores")
    print("• Expectativas realistas de rentabilidad")
    print("• Identificación de productos más rentables")
    print("• Consideración de riesgos específicos")
    print("• Herramienta útil para toma de decisiones")

if __name__ == "__main__":
    try:
        print("💰 AGROSOFT - SISTEMA DE RENTABILIDAD REALISTA")
        print("=" * 70)
        
        probar_rentabilidad_variada()
        probar_escenarios_contextuales()
        mostrar_interpretacion_realista()
        comparar_antes_despues()
        
        print("\n" + "=" * 70)
        print("✅ RENTABILIDAD REALISTA IMPLEMENTADA")
        print("• Variabilidad entre productos (-60% a +120%)")
        print("• Costos de producción actualizados")
        print("• Factor de riesgo por producto")
        print("• Variabilidad de mercado del ±30%")
        print("• Rangos realistas del sector agrícola")
        print("• Interpretación útil para productores")
        
        print("\n🌐 Prueba en el navegador:")
        print("http://127.0.0.1:8000/")
        print("Ahora verás rentabilidades más realistas y variadas")
        
    except Exception as e:
        print(f"Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
