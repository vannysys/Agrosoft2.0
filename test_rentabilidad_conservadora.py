#!/usr/bin/env python
"""
Prueba del sistema de rentabilidad conservador y realista
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService

def probar_rentabilidad_conservadora():
    """
    Prueba que las rentabilidades ahora sean más conservadoras y realistas
    """
    print("💰 SISTEMA DE RENTABILIDAD CONSERVADOR")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Probar diferentes escenarios
    escenarios = [
        ("Facatativá", datetime(2025, 8, 22), 16.0, "Condiciones actuales"),
        ("Subachoque", datetime(2025, 1, 15), 12.0, "Invierno frío"),
        ("Mosquera", datetime(2025, 7, 15), 18.0, "Época difícil"),
        ("Madrid", datetime(2025, 4, 15), 20.0, "Primavera cálida"),
    ]
    
    for municipio, fecha, temp, descripcion in escenarios:
        print(f"\n📍 {municipio.upper()} - {descripcion}")
        print(f"🌡️ Temperatura: {temp}°C | 📅 Fecha: {fecha.strftime('%d/%m/%Y')}")
        print("-" * 60)
        
        recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
        
        if recomendaciones:
            print("Producto         Precio   Rentab.  Tendencia  F.Mun  F.Clim  Estado")
            print("-" * 70)
            
            rentabilidades = []
            productos_excelentes = 0
            
            for i, rec in enumerate(recomendaciones[:8], 1):
                producto = rec['producto'][:12]
                precio = rec['precio_actual']
                rentabilidad = rec['rentabilidad_estimada']
                tendencia = rec['tendencia']
                factor_mun = rec['municipio_factor']
                factor_clima = rec.get('clima_factor', 1.0)
                
                rentabilidades.append(rentabilidad)
                
                # Clasificar estado
                if rentabilidad > 60:
                    estado = "🟢 EXCELENTE"
                    productos_excelentes += 1
                elif rentabilidad > 35:
                    estado = "🟡 BUENA"
                elif rentabilidad > 15:
                    estado = "🟠 REGULAR"
                elif rentabilidad > 0:
                    estado = "🔴 BAJA"
                else:
                    estado = "❌ PÉRDIDA"
                
                # Indicadores de factores
                ind_mun = "🟢" if factor_mun > 1.05 else "🔴" if factor_mun < 0.95 else "🟡"
                ind_clima = "🟢" if factor_clima > 1.1 else "🔴" if factor_clima < 0.9 else "🟡"
                
                print(f"{producto:<15} ${precio:>6,} {rentabilidad:>6.1f}%  {tendencia:<8} {factor_mun:.2f}{ind_mun} {factor_clima:.2f}{ind_clima} {estado}")
            
            # Estadísticas del escenario
            if rentabilidades:
                print(f"\n📊 Estadísticas:")
                print(f"• Promedio: {sum(rentabilidades)/len(rentabilidades):.1f}%")
                print(f"• Rango: {min(rentabilidades):.1f}% - {max(rentabilidades):.1f}%")
                print(f"• Productos excelentes (>60%): {productos_excelentes}/{len(rentabilidades)}")
                
                # Verificar realismo
                productos_sobre_80 = len([r for r in rentabilidades if r > 80])
                if productos_sobre_80 <= 2:
                    print("✅ Distribución realista de rentabilidades")
                else:
                    print(f"⚠️ Demasiados productos sobre 80%: {productos_sobre_80}")

def probar_penalizacion_tendencia():
    """
    Prueba específica de penalización por tendencia bajando
    """
    print("\n\n📉 PRUEBA DE PENALIZACIÓN POR TENDENCIA")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Obtener recomendaciones
    recomendaciones = sipsa.obtener_productos_recomendados("Facatativá", datetime.now(), 16.0)
    
    # Filtrar por tendencias
    productos_subiendo = [r for r in recomendaciones if r['tendencia'] == 'Subiendo']
    productos_bajando = [r for r in recomendaciones if r['tendencia'] == 'Bajando']
    productos_estable = [r for r in recomendaciones if r['tendencia'] == 'Estable']
    
    print("TENDENCIA        Cantidad  Rentab.Promedio  Rentab.Máxima")
    print("-" * 55)
    
    for nombre, productos in [("Subiendo", productos_subiendo), 
                             ("Estable", productos_estable),
                             ("Bajando", productos_bajando)]:
        if productos:
            rentabilidades = [p['rentabilidad_estimada'] for p in productos]
            promedio = sum(rentabilidades) / len(rentabilidades)
            maximo = max(rentabilidades)
            
            print(f"{nombre:<12} {len(productos):>8}  {promedio:>12.1f}%  {maximo:>11.1f}%")
    
    # Verificar que productos bajando tengan menor rentabilidad
    if productos_bajando and productos_subiendo:
        rent_bajando = sum(p['rentabilidad_estimada'] for p in productos_bajando) / len(productos_bajando)
        rent_subiendo = sum(p['rentabilidad_estimada'] for p in productos_subiendo) / len(productos_subiendo)
        
        if rent_bajando < rent_subiendo:
            print(f"\n✅ Penalización funcionando: Bajando ({rent_bajando:.1f}%) < Subiendo ({rent_subiendo:.1f}%)")
        else:
            print(f"\n❌ Penalización no funciona: Bajando ({rent_bajando:.1f}%) >= Subiendo ({rent_subiendo:.1f}%)")

def mostrar_distribucion_realista():
    """
    Muestra la distribución esperada vs actual de rentabilidades
    """
    print("\n\n📊 DISTRIBUCIÓN DE RENTABILIDADES")
    print("=" * 50)
    
    sipsa = SipsaService()
    
    # Obtener muestra grande de diferentes escenarios
    todas_rentabilidades = []
    
    municipios = ["Facatativá", "Subachoque", "Madrid", "Mosquera"]
    fechas = [datetime(2025, 1, 15), datetime(2025, 4, 15), datetime(2025, 7, 15), datetime(2025, 10, 15)]
    
    for municipio in municipios:
        for fecha in fechas:
            recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, 15.0)
            for rec in recomendaciones:
                todas_rentabilidades.append(rec['rentabilidad_estimada'])
    
    # Clasificar por rangos
    rangos = {
        "Excelente (>60%)": len([r for r in todas_rentabilidades if r > 60]),
        "Buena (35-60%)": len([r for r in todas_rentabilidades if 35 <= r <= 60]),
        "Regular (15-35%)": len([r for r in todas_rentabilidades if 15 <= r < 35]),
        "Baja (0-15%)": len([r for r in todas_rentabilidades if 0 <= r < 15]),
        "Pérdida (<0%)": len([r for r in todas_rentabilidades if r < 0])
    }
    
    total = len(todas_rentabilidades)
    
    print("Rango              Cantidad  Porcentaje  Esperado")
    print("-" * 50)
    
    esperados = {"Excelente (>60%)": "5-15%", "Buena (35-60%)": "20-30%", 
                "Regular (15-35%)": "40-50%", "Baja (0-15%)": "15-25%", "Pérdida (<0%)": "5-10%"}
    
    for rango, cantidad in rangos.items():
        porcentaje = (cantidad / total) * 100 if total > 0 else 0
        esperado = esperados.get(rango, "N/A")
        
        print(f"{rango:<18} {cantidad:>7}  {porcentaje:>8.1f}%  {esperado}")
    
    print(f"\nTotal productos analizados: {total}")
    print(f"Rentabilidad promedio general: {sum(todas_rentabilidades)/len(todas_rentabilidades):.1f}%")
    print(f"Rentabilidad máxima encontrada: {max(todas_rentabilidades):.1f}%")

if __name__ == "__main__":
    try:
        print("💰 AGROSOFT - RENTABILIDAD CONSERVADORA Y REALISTA")
        print("=" * 80)
        
        probar_rentabilidad_conservadora()
        probar_penalizacion_tendencia()
        mostrar_distribucion_realista()
        
        print("\n" + "=" * 80)
        print("✅ SISTEMA CONSERVADOR IMPLEMENTADO")
        print("• Máximo teórico: 85% (más realista)")
        print("• Penalización por tendencia bajando: -30%")
        print("• Penalización por factores bajos: -15% a -25%")
        print("• Costos aumentados significativamente")
        print("• Rendimientos reducidos")
        print("• Solo 3-4 productos deberían estar cerca del máximo")
        
        print("\n🌐 Prueba en el navegador:")
        print("http://127.0.0.1:8000/")
        print("Ahora deberías ver rentabilidades más realistas y variadas")
        
    except Exception as e:
        print(f"Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
