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
            recomendaciones = sipsa_service.obtener_productos_recomendados(municipio)
            print("Datos de recomendaciones:", recomendaciones)
            
            # Filtrar por municipio si se especifica
            if municipio:
                print("Aplicando filtro de municipio:", municipio)
                # Los datos de precios no tienen municipio, pero generaremos tendencias específicas
                # basadas en el municipio seleccionado
                print("Generando tendencias específicas para municipio:", municipio)
            
            # Procesar datos para el gráfico de tendencias (usar precios filtrados)
            tendencias_data = self._procesar_tendencias(precios, municipio)
            print("Datos de tendencias procesados:", tendencias_data)
            
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
    
    def _procesar_tendencias(self, precios, municipio):
        """
        Procesa datos de precios para generar tendencias temporales específicas por municipio.
        Genera datos de evolución de precios por semana para los últimos 6 meses.
        """
        from datetime import datetime, timedelta
        import random
        
        sipsa_service = SipsaService()
        
        # Agrupar precios por producto y fecha
        productos_agrupados = {}
        
        for precio in precios:
            producto = precio['producto']
            fecha_str = precio['fecha']
            
            if producto not in productos_agrupados:
                productos_agrupados[producto] = {}
            
            try:
                fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
                # Aplicar factor de municipio al precio
                factor_municipio = sipsa_service._obtener_factor_municipio(municipio, producto)
                precio_ajustado = precio['precio_mayorista'] * factor_municipio
                productos_agrupados[producto][fecha_obj] = precio_ajustado
            except:
                continue
        
        # Generar datos de tendencias para los últimos 6 meses
        fecha_fin = datetime.now()
        fecha_inicio = fecha_fin - timedelta(days=180)  # 6 meses atrás
        
        # Crear semanas para el eje X
        semanas = []
        precios_promedio = []
        cantidad_productos = []
        
        # Procesar por semanas
        fecha_actual = fecha_inicio
        while fecha_actual <= fecha_fin:
            semana_fin = fecha_actual + timedelta(days=6)
            
            # Calcular precio promedio y cantidad de productos para esta semana
            precios_semana = []
            productos_semana = set()
            
            for producto, precios_por_fecha in productos_agrupados.items():
                for fecha, precio_valor in precios_por_fecha.items():
                    if fecha_actual <= fecha <= semana_fin:
                        precios_semana.append(precio_valor)
                        productos_semana.add(producto)
            
            if precios_semana:
                precio_promedio_semana = sum(precios_semana) / len(precios_semana)
                semanas.append(fecha_actual.strftime('%d/%m'))
                precios_promedio.append(round(precio_promedio_semana, 2))
                cantidad_productos.append(len(productos_semana))
            
            fecha_actual = semana_fin + timedelta(days=1)
        
        # Si no hay suficientes datos, generar datos específicos para el municipio
        if len(semanas) < 4:
            # Generar datos de muestra específicos para el municipio
            semanas = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6']
            
            # Base de precios ajustada por municipio con variaciones más pronunciadas
            base_precio = 2000
            if municipio:
                # Usar el municipio como semilla para consistencia
                semilla = hash(municipio) % 1000
                random.seed(semilla)
                
                # Generar tendencia única y distintiva para cada municipio
                precios_promedio = []
                
                # Determinar patrón de tendencia basado en el municipio
                patron_tendencia = semilla % 4  # 4 patrones diferentes
                
                if patron_tendencia == 0:
                    # Tendencia ascendente fuerte
                    for i in range(6):
                        precio = base_precio * (1.0 + (i * 0.15) + random.uniform(-0.05, 0.05))
                        precios_promedio.append(round(precio, 2))
                
                elif patron_tendencia == 1:
                    # Tendencia descendente
                    for i in range(6):
                        precio = base_precio * (1.2 - (i * 0.12) + random.uniform(-0.05, 0.05))
                        precios_promedio.append(round(precio, 2))
                
                elif patron_tendencia == 2:
                    # Tendencia estable con variaciones
                    for i in range(6):
                        precio = base_precio * (1.1 + random.uniform(-0.1, 0.1))
                        precios_promedio.append(round(precio, 2))
                
                else:
                    # Tendencia volátil
                    precio_actual = base_precio * random.uniform(0.9, 1.1)
                    precios_promedio.append(round(precio_actual, 2))
                    for i in range(1, 6):
                        variacion = random.uniform(-0.15, 0.15)
                        precio_actual = precio_actual * (1 + variacion)
                        precios_promedio.append(round(precio_actual, 2))
                
                # Cantidad de productos también específica por municipio
                base_cantidad = 10
                if "Facatativá" in municipio:
                    cantidad_productos = [base_cantidad + random.randint(-2, 4) for _ in range(6)]
                elif "Madrid" in municipio:
                    cantidad_productos = [base_cantidad + random.randint(-1, 3) for _ in range(6)]
                elif "Mosquera" in municipio:
                    cantidad_productos = [base_cantidad + random.randint(-3, 2) for _ in range(6)]
                elif "Funza" in municipio:
                    cantidad_productos = [base_cantidad + random.randint(0, 5) for _ in range(6)]
                else:
                    cantidad_productos = [base_cantidad + random.randint(-2, 3) for _ in range(6)]
            else:
                # Datos genéricos si no hay municipio
                precios_promedio = [1500, 1800, 1600, 2000, 2200, 2100]
                cantidad_productos = [8, 12, 10, 15, 18, 20]
        
        return {
            'semanas': semanas,
            'precios_promedio': precios_promedio,
            'cantidad_productos': cantidad_productos,
            'municipio': municipio if municipio else 'Todos los municipios'
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
            
            # Obtener parámetros de filtro
            municipio = request.GET.get('municipio', 'Facatativá')
            
            # Obtener recomendaciones con filtro de municipio
            recomendaciones = sipsa_service.obtener_productos_recomendados(municipio)
            
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
