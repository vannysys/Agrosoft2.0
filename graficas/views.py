from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from datetime import datetime, timedelta
from productores.sipsa_service import SipsaService

@method_decorator(csrf_exempt, name='dispatch')
class GraficasDataView(View):
    """
    Vista para proporcionar datos para gráficas basados en información del SIPSA
    """
    
    def get(self, request):
        try:
            sipsa_service = SipsaService()
            
            # Obtener parámetros de filtro
            municipio = request.GET.get('municipio', '')
            producto = request.GET.get('producto', '')
            
            # Obtener precios actuales del SIPSA
            precios = sipsa_service.obtener_precios_actuales()
            print("Datos de precios obtenidos:", len(precios), "registros")
            
            # Obtener recomendaciones para el gráfico de tendencias
            recomendaciones = sipsa_service.obtener_productos_recomendados()
            print("Datos de recomendaciones:", recomendaciones)
            
            # Procesar datos para el gráfico de tendencias
            tendencias_data = self._procesar_tendencias(recomendaciones, municipio)
            print("Datos de tendencias procesados:", tendencias_data)
            
            # Filtrar por municipio si se especifica
            if municipio:
                print("Aplicando filtro de municipio:", municipio)
                precios = [p for p in precios if p.get('municipio', '').upper() == municipio.upper()]
                print("Datos de precios después de aplicar filtro de municipio:", len(precios), "registros")
            
            # Filtrar por producto si se especifica
            if producto:
                print("Aplicando filtro de producto:", producto)
                precios = [p for p in precios if p.get('producto', '').upper() == producto.upper()]
                print("Datos de precios después de aplicar filtro de producto:", len(precios), "registros")
            
            # Procesar datos para gráficas
            datos_graficas = self._procesar_datos_para_graficas(precios)
            
            # Agregar información de tendencias a los datos gráficos
            datos_graficas['tendencias'] = tendencias_data
            print("Datos gráficos procesados:", datos_graficas)
            
            # Agregar información de filtros aplicados
            datos_graficas['filtros_aplicados'] = {
                'municipio': municipio,
                'producto': producto,
                'total_resultados': len(precios)
            }
            
            return JsonResponse(datos_graficas)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def _procesar_tendencias(self, recomendaciones, municipio):
        """
        Procesa las recomendaciones para generar datos de tendencias.
        """
        semanas = []
        cantidades = []
        
        # Simular datos de tendencias basados en recomendaciones
        for i, recomendacion in enumerate(recomendaciones[:5]):  # Tomar las primeras 5 recomendaciones
            semanas.append(f"Semana {i+1}")
            cantidades.append(recomendacion.get('rentabilidad_estimada', 0))
        
        return {
            'semanas': semanas,
            'cantidades': cantidades
        }
    
    def _procesar_datos_para_graficas(self, precios):
        """
        Procesa los datos del SIPSA para generar información para gráficas lineales
        """
        # Agrupar precios por producto y fecha
        productos_agrupados = {}
        
        for precio in precios:
            producto = precio['producto']
            fecha = precio['fecha']
            
            if producto not in productos_agrupados:
                productos_agrupados[producto] = {}
            
            productos_agrupados[producto][fecha] = precio['precio_mayorista']
        
        # Preparar datos para gráficas lineales
        graficas_data = {
            'precios_tendencia': self._generar_grafica_tendencias(productos_agrupados),
            'productos_top': self._generar_top_productos(productos_agrupados),
            'evolucion_precios': self._generar_evolucion_precios(productos_agrupados),
            'comparativa_municipios': self._generar_comparativa_municipios(),
            'estadisticas_mercado': self._generar_estadisticas_mercado(precios)
        }
        
        return graficas_data
    
    def _generar_grafica_tendencias(self, productos_agrupados):
        """
        Genera datos para gráfica de tendencias de precios
        """
        tendencias = {}
        
        for producto, precios_por_fecha in productos_agrupados.items():
            if len(precios_por_fecha) >= 2:
                fechas = sorted(precios_por_fecha.keys())
                precios = [precios_por_fecha[fecha] for fecha in fechas]
                
                # Calcular tendencia (último precio vs precio anterior)
                if len(precios) >= 2:
                    ultimo_precio = precios[0]
                    precio_anterior = precios[1]
                    
                    if ultimo_precio > precio_anterior:
                        tendencia = "subiendo"
                    elif ultimo_precio < precio_anterior:
                        tendencia = "bajando"
                    else:
                        tendencia = "estable"
                    
                    variacion = ((ultimo_precio - precio_anterior) / precio_anterior) * 100
                    
                    tendencias[producto] = {
                        'tendencia': tendencia,
                        'variacion_porcentaje': round(variacion, 2),
                        'ultimo_precio': ultimo_precio,
                        'fecha_ultimo': fechas[0]
                    }
        
        return tendencias
    
    def _generar_top_productos(self, productos_agrupados):
        """
        Genera datos para top productos por rentabilidad
        """
        top_productos = []
        
        for producto, precios_por_fecha in productos_agrupados.items():
            if precios_por_fecha:
                fechas = sorted(precios_por_fecha.keys(), reverse=True)
                ultimo_precio = precios_por_fecha[fechas[0]] if fechas else 0
                
                # Simular rentabilidad basada en el precio (esto podría mejorarse)
                rentabilidad_estimada = min(100, max(0, (ultimo_precio / 100) * 2))
                
                top_productos.append({
                    'producto': producto,
                    'precio_actual': ultimo_precio,
                    'rentabilidad_estimada': round(rentabilidad_estimada, 1),
                    'tendencia': self._obtener_tendencia_producto(precios_por_fecha)
                })
        
        # Ordenar por rentabilidad descendente
        top_productos.sort(key=lambda x: x['rentabilidad_estimada'], reverse=True)
        
        return top_productos[:10]  # Top 10 productos
    
    def _generar_evolucion_precios(self, productos_agrupados):
        """
        Genera datos para gráfica de evolución de precios
        """
        evolucion = {}
        
        for producto, precios_por_fecha in productos_agrupados.items():
            fechas = sorted(precios_por_fecha.keys())
            precios = [precios_por_fecha[fecha] for fecha in fechas]
            
            evolucion[producto] = {
                'fechas': fechas,
                'precios': precios,
                'precio_promedio': round(sum(precios) / len(precios), 2) if precios else 0
            }
        
        return evolucion
    
    def _generar_comparativa_municipios(self):
        """
        Genera datos para comparativa entre municipios (simulado)
        """
        # Esto podría mejorarse con datos reales de diferentes municipios
        municipios = ['Facatativá', 'Madrid', 'Mosquera', 'Funza']
        comparativa = {}
        
        sipsa_service = SipsaService()
        
        for municipio in municipios:
            # Simular precios por municipio usando el factor de municipio del servicio
            precios_simulados = []
            for producto in ['PAPA CRIOLLA', 'PAPA PASTUSA', 'ZANAHORIA']:
                factor_municipio = sipsa_service._obtener_factor_municipio(municipio, producto)
                precio_base = 2000  # Precio base simulado
                precio_ajustado = int(precio_base * factor_municipio)
                precios_simulados.append(precio_ajustado)
            
            comparativa[municipio] = {
                'precio_promedio': round(sum(precios_simulados) / len(precios_simulados), 2),
                'productos': len(precios_simulados)
            }
        
        return comparativa
    
    def _generar_estadisticas_mercado(self, precios):
        """
        Genera estadísticas generales del mercado
        """
        if not precios:
            return {}
        
        precios_validos = [p['precio_mayorista'] for p in precios if p['precio_mayorista']]
        productos_unicos = set(p['producto'] for p in precios)
        
        if not precios_validos:
            return {}
        
        return {
            'total_productos': len(productos_unicos),
            'precio_promedio': round(sum(precios_validos) / len(precios_validos), 2),
            'precio_minimo': min(precios_validos),
            'precio_maximo': max(precios_validos),
            'total_registros': len(precios),
            'fecha_actualizacion': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
    
    def _obtener_tendencia_producto(self, precios_por_fecha):
        """
        Determina la tendencia de un producto basado en sus precios históricos
        """
        if len(precios_por_fecha) < 2:
            return "estable"
        
        fechas = sorted(precios_por_fecha.keys())
        precios = [precios_por_fecha[fecha] for fecha in fechas]
        
        # Últimos 3 precios para determinar tendencia
        if len(precios) >= 3:
            ultimos_precios = precios[:3]
            if ultimos_precios[0] > ultimos_precios[1] > ultimos_precios[2]:
                return "bajando"
            elif ultimos_precios[0] < ultimos_precios[1] < ultimos_precios[2]:
                return "subiendo"
        
        return "estable"


# Vista adicional para datos específicos de recomendaciones
@method_decorator(csrf_exempt, name='dispatch')
class GraficasRecomendacionesView(View):
    """
    Vista para datos de gráficas específicas de recomendaciones
    """
    
    def get(self, request):
        try:
            sipsa_service = SipsaService()
            
            # Obtener recomendaciones (simulando parámetros)
            recomendaciones = sipsa_service.obtener_productos_recomendados()
            
            datos_recomendaciones = {
                'recomendaciones': recomendaciones,
                'top_recomendados': self._procesar_top_recomendados(recomendaciones),
                'rentabilidades': self._procesar_rentabilidades(recomendaciones)
            }
            
            return JsonResponse(datos_recomendaciones)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def _procesar_top_recomendados(self, recomendaciones):
        """Procesa las mejores recomendaciones"""
        if not recomendaciones:
            return []
        
        return recomendaciones[:5]  # Top 5 recomendaciones
    
    def _procesar_rentabilidades(self, recomendaciones):
        """Procesa datos de rentabilidad para gráficas"""
        if not recomendaciones:
            return {}
        
        rentabilidades = [rec['rentabilidad_estimada'] for rec in recomendaciones]
        
        return {
            'promedio': round(sum(rentabilidades) / len(rentabilidades), 2),
            'maxima': max(rentabilidades),
            'minima': min(rentabilidades),
            'total': len(rentabilidades)
        }
