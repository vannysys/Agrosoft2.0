#!/usr/bin/env python
"""
Script de prueba para verificar la conexión con la API del SIPSA
"""

import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService

def test_sipsa_connection():
    """
    Prueba la conexión con el servicio SIPSA
    """
    print("🔍 Probando conexión con SIPSA...")
    
    sipsa = SipsaService()
    
    # Probar obtener precios actuales
    print("\n📊 Obteniendo precios actuales...")
    precios = sipsa.obtener_precios_actuales(limit=10)
    
    if precios:
        print(f"✅ Se obtuvieron {len(precios)} registros de precios")
        print("\n📋 Primeros 3 productos:")
        for i, precio in enumerate(precios[:3]):
            print(f"{i+1}. {precio['producto']} - ${precio['precio_mayorista']} ({precio['mercado']})")
    else:
        print("❌ No se pudieron obtener precios")
        return False
    
    # Probar precios de Corabastos específicamente
    print("\n🏪 Obteniendo precios de Corabastos...")
    precios_corabastos = sipsa.obtener_precios_corabastos()
    
    if precios_corabastos:
        print(f"✅ Se obtuvieron {len(precios_corabastos)} registros de Corabastos")
    else:
        print("⚠️ No se encontraron precios específicos de Corabastos")
    
    # Probar recomendaciones
    print("\n🌱 Generando recomendaciones...")
    recomendaciones = sipsa.obtener_productos_recomendados()
    
    if recomendaciones:
        print(f"✅ Se generaron {len(recomendaciones)} recomendaciones")
        print("\n🏆 Top 3 productos recomendados:")
        for i, rec in enumerate(recomendaciones[:3]):
            print(f"{i+1}. {rec['producto']} - ${rec['precio_actual']} - {rec['tendencia']}")
    else:
        print("❌ No se pudieron generar recomendaciones")
        return False
    
    # Probar estadísticas
    print("\n📈 Obteniendo estadísticas del mercado...")
    stats = sipsa.obtener_estadisticas_mercado()
    
    if stats:
        print("✅ Estadísticas obtenidas:")
        print(f"   - Total productos: {stats.get('total_productos', 'N/A')}")
        print(f"   - Precio promedio: ${stats.get('precio_promedio_general', 'N/A')}")
        print(f"   - Última actualización: {stats.get('fecha_ultima_actualizacion', 'N/A')}")
    else:
        print("⚠️ No se pudieron obtener estadísticas")
    
    print("\n🎉 ¡Prueba completada exitosamente!")
    return True

if __name__ == "__main__":
    try:
        success = test_sipsa_connection()
        if success:
            print("\n✅ El servicio SIPSA está funcionando correctamente")
            print("🚀 Puedes ejecutar el servidor Django con: python manage.py runserver")
        else:
            print("\n❌ Hay problemas con el servicio SIPSA")
            sys.exit(1)
    except Exception as e:
        print(f"\n💥 Error durante la prueba: {e}")
        sys.exit(1)
