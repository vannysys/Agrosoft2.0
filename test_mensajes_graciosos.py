#!/usr/bin/env python
"""
Prueba de mensajes graciosos para rentabilidades bajas
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrosoft.settings')

import django
django.setup()

from productores.sipsa_service import SipsaService
from productores.views import obtener_mensaje_gracioso

def buscar_escenarios_bajos():
    """
    Busca escenarios con rentabilidades bajas para probar mensajes
    """
    print("😄 BUSCANDO ESCENARIOS PARA MENSAJES GRACIOSOS")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Probar diferentes combinaciones para encontrar rentabilidades bajas
    municipios = ['Facatativá', 'Madrid', 'Mosquera', 'El Rosal', 'Subachoque', 'Bojacá', 'Funza']
    fechas = [
        datetime(2025, 7, 15),   # Época difícil (invierno)
        datetime(2025, 8, 15),   # Agosto (época regular)
        datetime(2025, 3, 15),   # Marzo (transición)
        datetime(2025, 6, 15),   # Junio (inicio lluvias)
    ]
    temperaturas = [8.0, 22.0, 25.0]  # Temperaturas extremas
    
    escenarios_bajos = []
    
    for municipio in municipios:
        for fecha in fechas:
            for temp in temperaturas:
                recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
                
                if recomendaciones:
                    max_rentabilidad = max(rec['rentabilidad_estimada'] for rec in recomendaciones)
                    
                    if max_rentabilidad < 50:  # Rentabilidad baja
                        escenarios_bajos.append({
                            'municipio': municipio,
                            'fecha': fecha,
                            'temp': temp,
                            'max_rent': max_rentabilidad,
                            'recomendaciones': recomendaciones[:3]  # Top 3
                        })
    
    # Mostrar escenarios encontrados
    print(f"📊 Encontrados {len(escenarios_bajos)} escenarios con rentabilidades bajas")
    
    if escenarios_bajos:
        print("\nEscenarios con rentabilidades < 50%:")
        print("-" * 60)
        
        for i, escenario in enumerate(escenarios_bajos[:5], 1):  # Mostrar solo 5
            print(f"\n{i}. {escenario['municipio']} - {escenario['fecha'].strftime('%d/%m/%Y')} - {escenario['temp']}°C")
            print(f"   Rentabilidad máxima: {escenario['max_rent']:.1f}%")
            
            # Mostrar top 3 productos
            for j, rec in enumerate(escenario['recomendaciones'], 1):
                print(f"   {j}. {rec['producto'][:15]}: {rec['rentabilidad_estimada']:.1f}%")
    
    return escenarios_bajos

def probar_mensajes_por_categoria():
    """
    Prueba los diferentes tipos de mensajes según el nivel de rentabilidad
    """
    print("\n\n😂 PROBANDO MENSAJES POR CATEGORÍA")
    print("=" * 60)
    
    # Simular diferentes niveles de rentabilidad
    niveles_test = [
        (10.0, "Muy Baja (0-20%)"),
        (25.0, "Baja (20-35%)"),
        (42.0, "Regular Baja (35-50%)"),
        (55.0, "Sin Mensaje (≥50%)")
    ]
    
    municipio = "Facatativá"
    fecha = datetime(2025, 7, 15)
    
    for rentabilidad, categoria in niveles_test:
        print(f"\n📊 {categoria} - Rentabilidad: {rentabilidad}%")
        print("-" * 50)
        
        mensaje = obtener_mensaje_gracioso(rentabilidad, municipio, fecha)
        
        if mensaje:
            print(f"💬 Mensaje: {mensaje}")
        else:
            print("🔇 Sin mensaje (rentabilidad suficiente)")

def probar_variedad_mensajes():
    """
    Prueba que haya variedad en los mensajes (no siempre el mismo)
    """
    print("\n\n🎲 PROBANDO VARIEDAD DE MENSAJES")
    print("=" * 60)
    
    municipio = "Subachoque"
    fecha = datetime(2025, 7, 15)
    rentabilidad = 15.0  # Muy baja para activar mensajes
    
    mensajes_generados = []
    
    print("Generando 10 mensajes para rentabilidad muy baja (15%):")
    print("-" * 50)
    
    for i in range(10):
        mensaje = obtener_mensaje_gracioso(rentabilidad, municipio, fecha)
        mensajes_generados.append(mensaje)
        print(f"{i+1:2d}. {mensaje}")
    
    # Verificar variedad
    mensajes_unicos = len(set(mensajes_generados))
    print(f"\n📊 Estadísticas:")
    print(f"• Total mensajes generados: {len(mensajes_generados)}")
    print(f"• Mensajes únicos: {mensajes_unicos}")
    print(f"• Variedad: {mensajes_unicos/len(mensajes_generados)*100:.1f}%")
    
    if mensajes_unicos >= 5:
        print("✅ Buena variedad de mensajes")
    else:
        print("⚠️ Poca variedad, considera agregar más mensajes")

def simular_escenario_completo():
    """
    Simula un escenario completo como aparecería en el navegador
    """
    print("\n\n🌐 SIMULACIÓN COMPLETA DEL NAVEGADOR")
    print("=" * 60)
    
    sipsa = SipsaService()
    
    # Buscar un escenario con rentabilidades bajas
    municipio = "El Rosal"
    fecha = datetime(2025, 7, 15)  # Época difícil
    temp = 8.0  # Temperatura muy baja
    
    print(f"📍 Municipio: {municipio}")
    print(f"📅 Fecha: {fecha.strftime('%d/%m/%Y')}")
    print(f"🌡️ Temperatura: {temp}°C")
    print("-" * 40)
    
    recomendaciones = sipsa.obtener_productos_recomendados(municipio, fecha, temp)
    
    if recomendaciones:
        max_rentabilidad = max(rec['rentabilidad_estimada'] for rec in recomendaciones)
        print(f"📊 Rentabilidad máxima: {max_rentabilidad:.1f}%")
        
        # Mostrar top 5 productos
        print("\n🏆 Top 5 Recomendaciones:")
        for i, rec in enumerate(recomendaciones[:5], 1):
            producto = rec['producto'][:15]
            rentabilidad = rec['rentabilidad_estimada']
            tendencia = rec['tendencia']
            
            if rentabilidad > 30:
                emoji = "🟠"
            elif rentabilidad > 15:
                emoji = "🔴"
            else:
                emoji = "❌"
            
            print(f"{i}. {emoji} {producto:<15} {rentabilidad:>6.1f}% ({tendencia})")
        
        # Generar mensaje gracioso si aplica
        if max_rentabilidad < 50:
            mensaje = obtener_mensaje_gracioso(max_rentabilidad, municipio, fecha)
            print(f"\n🚨 MENSAJE GRACIOSO ACTIVADO:")
            print(f"📢 {mensaje}")
            
            # Simular cómo se vería en HTML
            print(f"\n🌐 VISTA EN EL NAVEGADOR:")
            print("┌" + "─" * 58 + "┐")
            print("│ 🚨 ¡Alerta de Rentabilidad Baja! 🚨                   │")
            print("├" + "─" * 58 + "┤")
            print(f"│ {mensaje[:56]:<56} │")
            if len(mensaje) > 56:
                print(f"│ {mensaje[56:]:<56} │")
            print("├" + "─" * 58 + "┤")
            print("│ 💡 Consejo: Considera esperar una época más favorable │")
            print("└" + "─" * 58 + "┘")
        else:
            print(f"\n✅ Sin mensaje gracioso (rentabilidad {max_rentabilidad:.1f}% es aceptable)")

def mostrar_todos_los_mensajes():
    """
    Muestra todos los mensajes disponibles por categoría
    """
    print("\n\n📝 CATÁLOGO COMPLETO DE MENSAJES")
    print("=" * 60)
    
    print("🔴 MENSAJES MUY BAJOS (0-20%):")
    mensajes_muy_bajos = [
        "🐄 En {municipio} mejor compra ganado, las vacas no dependen del clima",
        "🚚 Considera un carrito de comidas en {municipio}, los tacos siempre venden",
        "🏠 Alquila tu terreno y vete de vacaciones, será más rentable",
        "🎣 Mejor dedícate a la pesca, los peces no leen el SIPSA",
        "🍕 Abre una pizzería, la gente siempre tiene hambre",
        "🚗 Uber en {municipio} puede ser más rentable que sembrar",
        "💻 Aprende programación, los bugs crecen más rápido que las plantas",
        "🎪 Monta un circo, será menos riesgoso que la agricultura"
    ]
    
    for i, mensaje in enumerate(mensajes_muy_bajos, 1):
        print(f"{i:2d}. {mensaje}")
    
    print(f"\n🟠 MENSAJES BAJOS (20-35%):")
    mensajes_bajos = [
        "🐔 Considera gallinas ponedoras, los huevos no tienen temporada baja",
        "🏪 Una tienda de barrio en {municipio} podría ser mejor opción",
        "🚜 Alquila tu tractor a otros, que ellos corran el riesgo",
        "🌻 Siembra girasoles para selfies, el turismo rural está de moda",
        "🍯 La apicultura podría ser más dulce que estos números",
        "🐟 Piscicultura: los peces no protestan por el clima",
        "🎯 Mejor invierte en un billar, siempre hay clientes",
        "🏋️ Abre un gimnasio rural, la gente necesita ejercitarse"
    ]
    
    for i, mensaje in enumerate(mensajes_bajos, 1):
        print(f"{i:2d}. {mensaje}")
    
    print(f"\n🟡 MENSAJES REGULARES BAJOS (35-50%):")
    mensajes_regulares = [
        "🤔 En {municipio} tal vez sea mejor esperar una época más favorable",
        "🌱 Considera cultivos de ciclo corto, menos riesgo y más rotación",
        "🏡 Huerta casera para autoconsumo y venta local podría funcionar",
        "🐰 Conejos: se reproducen rápido y no dependen tanto del clima",
        "🌿 Plantas aromáticas para restaurantes, nicho pequeño pero seguro",
        "🍄 Hongos comestibles: crecen en cualquier clima controlado",
        "🎨 Agro-turismo: que otros paguen por ver tu terreno",
        "📚 Estudia el mercado un poco más, estos números no convencen"
    ]
    
    for i, mensaje in enumerate(mensajes_regulares, 1):
        print(f"{i:2d}. {mensaje}")
    
    print(f"\n📊 TOTAL: {len(mensajes_muy_bajos + mensajes_bajos + mensajes_regulares)} mensajes únicos")

if __name__ == "__main__":
    try:
        print("😄 AGROSOFT - MENSAJES GRACIOSOS PARA RENTABILIDADES BAJAS")
        print("=" * 80)
        
        escenarios_bajos = buscar_escenarios_bajos()
        probar_mensajes_por_categoria()
        probar_variedad_mensajes()
        simular_escenario_completo()
        mostrar_todos_los_mensajes()
        
        print("\n" + "=" * 80)
        print("✅ SISTEMA DE MENSAJES GRACIOSOS IMPLEMENTADO")
        print("• 24 mensajes únicos en 3 categorías")
        print("• Activación automática cuando rentabilidad máxima < 50%")
        print("• Variedad aleatoria para evitar repetición")
        print("• Integrado en la interfaz web con estilo atractivo")
        print("• Mensajes divertidos pero informativos")
        
        print("\n🌐 Prueba en el navegador:")
        print("http://127.0.0.1:8000/")
        print("Selecciona El Rosal + Julio + temperaturas extremas para ver mensajes")
        
    except Exception as e:
        print(f"Error durante la prueba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
