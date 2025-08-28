from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Count, Sum, Q
from .forms import AgricultorRegistroForm, SolicitudRecomendacionForm
from .models import SolicitudRecomendacion, Usuario
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.hashers import make_password
import uuid
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.utils.safestring import mark_safe


# Función auxiliar para verificar si el usuario es admin
def es_admin(user):
    return user.is_authenticated and user.tipo == 'admin'

# Vista del dashboard administrativo
@login_required
@user_passes_test(es_admin)
def admin_dashboard(request):
    """Vista principal del panel administrativo"""
    # Estadísticas generales
    total_usuarios = Usuario.objects.count()
    total_agricultores = Usuario.objects.filter(tipo='agricultor').count()
    total_solicitudes = SolicitudRecomendacion.objects.count()
    solicitudes_pendientes = SolicitudRecomendacion.objects.filter(estado='pendiente').count()
    
    # Últimas solicitudes
    ultimas_solicitudes = SolicitudRecomendacion.objects.all().order_by('-fecha')[:5]
    
    # Solo 3 cultivos más populares
    cultivos_populares = (
        SolicitudRecomendacion.objects
        .values('cultivo_deseado')
        .annotate(total=Count('id'))
        .order_by('-total')[:3]   # 👈 límite de 3
    )
    
    context = {
        'total_usuarios': total_usuarios,
        'total_agricultores': total_agricultores,
        'total_solicitudes': total_solicitudes,
        'solicitudes_pendientes': solicitudes_pendientes,
        'ultimas_solicitudes': ultimas_solicitudes,
        'cultivos_populares': list(cultivos_populares),
    }
    return render(request, 'admin_dashboard.html', context)


# HU4 - Gestionar usuarios
@login_required
@user_passes_test(es_admin)
def gestionar_usuarios(request):
    """Vista para gestionar usuarios del sistema"""
    usuarios = Usuario.objects.all().order_by('-date_joined')
    
    if request.method == 'POST':
        if 'crear_usuario' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            tipo = request.POST.get('tipo')
            
            if Usuario.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe.')
            else:
                usuario = Usuario.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    tipo=tipo
                )
                messages.success(request, f'Usuario {username} creado exitosamente.')
                
        elif 'eliminar_usuario' in request.POST:
            usuario_id = request.POST.get('usuario_id')
            try:
                usuario = Usuario.objects.get(id=usuario_id)
                if usuario != request.user:
                    usuario.delete()
                    messages.success(request, 'Usuario eliminado exitosamente.')
                else:
                    messages.error(request, 'No puedes eliminar tu propio usuario.')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuario no encontrado.')
    
    context = {
        'usuarios': usuarios
    }
    return render(request, 'gestionar_usuarios.html', context)

# HU8 - Reporte de cultivos
@login_required
@user_passes_test(es_admin)
def reporte_cultivos(request):
    """Vista para generar reportes de cultivos"""
    cultivos = SolicitudRecomendacion.objects.all()
    
    # Filtros
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    agricultor = request.GET.get('agricultor')
    cultivo = request.GET.get('cultivo')
    
    if fecha_inicio:
        cultivos = cultivos.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        cultivos = cultivos.filter(fecha__lte=fecha_fin)
    if agricultor:
        cultivos = cultivos.filter(agricultor__username__icontains=agricultor)
    if cultivo:
        cultivos = cultivos.filter(cultivo_deseado__icontains=cultivo)
    
    # Estadísticas
    total_cultivos = cultivos.count()
    total_produccion = cultivos.aggregate(
        total=Sum('cantidad')
    )['total'] or 0
    
    context = {
        'cultivos': cultivos,
        'total_cultivos': total_cultivos,
        'total_produccion': total_produccion,
    }
    return render(request, 'reporte_cultivos.html', context)

# HU5 - Reportes gráficos
@login_required
def reportes_graficos(request):
    """Vista para mostrar reportes gráficos"""
    # Datos para gráficos
    cultivos_data = SolicitudRecomendacion.objects.values('cultivo_deseado').annotate(
        total=Count('id'),
        cantidad_total=Sum('cantidad')
    ).order_by('-total')[:10]
    
    # Datos mensuales
    meses = []
    produccion_mensual = []
    for i in range(12):
        mes = datetime.now().replace(month=i+1, day=1)
        meses.append(mes.strftime('%B'))
        produccion = SolicitudRecomendacion.objects.filter(
            fecha__month=i+1,
            fecha__year=datetime.now().year
        ).aggregate(total=Sum('cantidad'))['total'] or 0
        produccion_mensual.append(float(produccion))
    
    # Viabilidad de cultivos
    viabilidad_data = SolicitudRecomendacion.objects.values('viabilidad').annotate(
        total=Count('id')
    )
    
    context = {
        'cultivos_data': list(cultivos_data),
        'meses': meses,
        'produccion_mensual': produccion_mensual,
        'viabilidad_data': list(viabilidad_data),
    }
    return render(request, 'reportes_graficos.html', context)

# HU6 - Producción proyectada
@login_required
@user_passes_test(es_admin)
def produccion_proyectada(request):
    """Vista para calcular producción proyectada"""
    producto_seleccionado = request.GET.get('producto')
    hectareas = request.GET.get('hectareas', 1)

    cultivos_activos = SolicitudRecomendacion.objects.filter(
        estado='procesada'
    ).select_related('agricultor')

    proyecciones = []
    for cultivo in cultivos_activos:
        if cultivo.cantidad and cultivo.precio_estimado:
            ingreso_proyectado = float(cultivo.cantidad) * float(cultivo.precio_estimado)
            proyecciones.append({
                'producto': cultivo,
                'produccion_total': cultivo.cantidad,
                'precio_unidad': cultivo.precio_estimado,
                'ingreso_proyectado': ingreso_proyectado,
                'rendimiento_estimado': cultivo.cantidad * 0.9
            })

    # 🔎 Filtrar si hay producto seleccionado
    if producto_seleccionado:
        proyecciones = [p for p in proyecciones if p['producto'].cultivo_deseado == producto_seleccionado]

    # 📑 Paginación
    from django.core.paginator import Paginator
    paginator = Paginator(proyecciones, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 📊 Datos para gráfico
    labels = [p['producto'].cultivo_deseado for p in proyecciones]
    ingresos = [p['ingreso_proyectado'] for p in proyecciones]
    cantidades = [p['produccion_total'] for p in proyecciones]
    colores = ["rgba(75, 192, 192, 0.8)" for _ in proyecciones]  # color fijo, puedes randomizar si quieres

    datos_grafico = {
        'labels': mark_safe(json.dumps(labels)),
        'ingresos': mark_safe(json.dumps(ingresos)),
        'cantidades': mark_safe(json.dumps(cantidades)),
        'colores': mark_safe(json.dumps(colores)),
    }

    context = {
        'productos_disponibles': cultivos_activos,
        'producto_seleccionado': producto_seleccionado,
        'cantidad_hectareas': hectareas,
        'proyecciones': page_obj,
        'page_obj': page_obj,
        'total_proyectado': sum(p['ingreso_proyectado'] for p in proyecciones),
        'total_cultivos': len(proyecciones),
        'rendimiento_promedio': sum(p['rendimiento_estimado'] for p in proyecciones) / len(proyecciones) if proyecciones else 0,
        'datos_grafico': datos_grafico,
    }
    return render(request, 'produccion_proyectada.html', context)

# Resto de las vistas originales...
def registro(request):
    """Vista para el registro de nuevos agricultores"""
    if request.method == 'POST':
        form = AgricultorRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.tipo = 'agricultor'
            usuario.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = AgricultorRegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    """Vista para el login de usuarios"""
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            error = 'Usuario o contraseña incorrectos.'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    return redirect('home')

def recuperar_contrasena(request):
    """Vista para solicitar recuperación de contraseña por email"""
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            # Buscar por username o email
            usuario = Usuario.objects.filter(
                Q(username=username) | Q(email=username)
            ).first()
            
            if not usuario:
                raise Usuario.DoesNotExist
            
            # Generar token y fecha de expiración
            token = str(uuid.uuid4())
            expires_at = timezone.now() + timedelta(hours=24)
            
            # Guardar token en la base de datos
            usuario.reset_token = token
            usuario.reset_token_expires = expires_at
            usuario.save()
            
            # Construir URL de reseteo
            reset_url = request.build_absolute_uri(
                reverse('cambiar_contrasena', args=[token])
            )
            
            # Renderizar template de email
            email_html = render_to_string('email_recuperacion.html', {
                'usuario': usuario,
                'reset_url': reset_url
            })
            
            # Enviar email
            send_mail(
                'Recuperación de Contraseña - AgroSoft',
                f'Hola {usuario.username},\n\nPara restablecer tu contraseña, visita: {reset_url}\n\nEste enlace expira en 24 horas.',
                settings.DEFAULT_FROM_EMAIL,
                [usuario.email],
                fail_silently=False,
                html_message=email_html
            )
            
            messages.success(request, 'Se ha enviado un email con instrucciones para restablecer tu contraseña.')
            return redirect('login')
            
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
    
    return render(request, 'recuperar_contrasena.html')

def cambiar_contrasena(request, token):
    """Vista para cambiar la contraseña con token"""
    try:
        usuario = Usuario.objects.get(reset_token=token)
        
        # Verificar si el token es válido
        if not usuario.is_reset_token_valid():
            messages.error(request, 'El enlace de recuperación ha expirado o es inválido.')
            return redirect('recuperar_contrasena')
            
    except Usuario.DoesNotExist:
        messages.error(request, 'El enlace de recuperación es inválido.')
        return redirect('recuperar_contrasena')
    
    if request.method == 'POST':
        nueva_contrasena = request.POST.get('nueva_contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')
        
        if nueva_contrasena != confirmar_contrasena:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'cambiar_contrasena.html', {'token': token})
        
        if len(nueva_contrasena) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return render(request, 'cambiar_contrasena.html', {'token': token})
        
        # ✅ Actualizar contraseña de manera segura
        print(f"DEBUG: Cambiando contraseña para usuario {usuario.username}")
        usuario.set_password(nueva_contrasena)
        usuario.reset_token = None
        usuario.reset_token_expires = None
        usuario.save()
        print(f"DEBUG: Contraseña cambiada exitosamente para usuario {usuario.username}")
        
        messages.success(request, 'Contraseña actualizada exitosamente. Ahora puedes iniciar sesión.')
        return redirect('login')
    
    return render(request, 'cambiar_contrasena.html', {'token': token})

def productos(request):
    """Vista para mostrar productos agrícolas disponibles"""
    # Datos de ejemplo de productos agrícolas
    productos_data = [
        {
            'nombre': 'Maíz',
            'descripcion': 'Cultivo de maíz amarillo para consumo humano y animal.',
            'precio_kg': 1200,
            'temporada': 'Todo el año',
            'rendimiento': 'Alto (8-10 ton/ha)'
        },
        {
            'nombre': 'Frijol',
            'descripcion': 'Frijol rojo de alta calidad para exportación.',
            'precio_kg': 2800,
            'temporada': 'Enero - Marzo',
            'rendimiento': 'Medio (4-6 ton/ha)'
        },
        {
            'nombre': 'Arroz',
            'descripcion': 'Arroz blanco premium para consumo nacional.',
            'precio_kg': 1800,
            'temporada': 'Abril - Junio',
            'rendimiento': 'Alto (6-8 ton/ha)'
        },
        {
            'nombre': 'Café',
            'descripcion': 'Café arábica de alta montaña.',
            'precio_kg': 8500,
            'temporada': 'Octubre - Diciembre',
            'rendimiento': 'Bajo (1-2 ton/ha)'
        },
        {
            'nombre': 'Plátano',
            'descripcion': 'Plátano hartón para exportación.',
            'precio_kg': 950,
            'temporada': 'Todo el año',
            'rendimiento': 'Muy alto (15-20 ton/ha)'
        },
        {
            'nombre': 'Aguacate',
            'descripcion': 'Aguacate hass para mercado internacional.',
            'precio_kg': 4200,
            'temporada': 'Marzo - Mayo',
            'rendimiento': 'Medio (3-5 ton/ha)'
        }
    ]
    
    context = {
        'titulo': 'Productos Agrícolas Disponibles',
        'descripcion': 'Catálogo de cultivos recomendados para la Sabana de Occidente',
        'productos': productos_data
    }
    return render(request, 'productos.html', context)

@login_required
def dashboard_data_api(request):
    """API endpoint para obtener datos del dashboard en tiempo real"""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'No autenticado'}, status=401)
    
    # Obtener las solicitudes del agricultor
    solicitudes = SolicitudRecomendacion.objects.filter(agricultor=request.user)
    
    # Datos para producción por cultivo y clima
    produccion_por_cultivo = solicitudes.values('cultivo_deseado').annotate(
        total_cantidad=Sum('cantidad')
    ).order_by('-total_cantidad')[:10]
    
    produccion_labels = [item['cultivo_deseado'] or 'Sin especificar' for item in produccion_por_cultivo]
    produccion_data = [float(item['total_cantidad'] or 0) for item in produccion_por_cultivo]
    
    # Datos para viabilidad
    viabilidad_data = solicitudes.values('viabilidad').annotate(
        total=Count('id')
    )
    
    viabilidad_labels = [item['viabilidad'] or 'pendiente' for item in viabilidad_data]
    viabilidad_values = [item['total'] for item in viabilidad_data]
    
    # Estadísticas generales
    total_cultivos = solicitudes.count()
    total_produccion = sum(produccion_data)
    ingresos_totales = sum(float(s.ingreso_proyectado or 0) for s in solicitudes)
    
    response_data = {
        'produccionPorCultivo': {
            'labels': produccion_labels,
            'data': produccion_data
        },
        'viabilidadData': {
            'labels': viabilidad_labels,
            'data': viabilidad_values
        },
        'estadisticas': {
            'total_cultivos': total_cultivos,
            'total_produccion': total_produccion,
            'ingresos_totales': ingresos_totales
        }
    }
    
    return JsonResponse(response_data)

def home(request):
    """Vista principal - Muestra dashboard si está autenticado, sino página de presentación"""
    if request.user.is_authenticated:
        # Obtener las solicitudes de recomendaciones del agricultor
        solicitudes = SolicitudRecomendacion.objects.filter(agricultor=request.user)

        # Calcular datos para el dashboard
        if solicitudes.exists():
            cultivo = solicitudes.first().cultivo_deseado
            cantidad = sum(solicitud.cantidad for solicitud in solicitudes)
            fecha_siembra = solicitudes.first().fecha_cultivo
            fecha_cosecha = solicitudes.first().fecha_cosecha
            dias = (fecha_cosecha - fecha_siembra).days if fecha_cosecha else 0
            viabilidad = solicitudes.first().viabilidad
            clima = solicitudes.first().clima_recomendacion
            solicitudes_recientes = solicitudes.order_by('-fecha')[:5]
        else:
            cultivo = cantidad = fecha_siembra = fecha_cosecha = dias = viabilidad = clima = None
            solicitudes_recientes = []

        context = {
            'cultivo': cultivo,
            'cantidad': cantidad,
            'fecha_siembra': fecha_siembra,
            'fecha_cosecha': fecha_cosecha,
            'dias': dias,
            'viabilidad': viabilidad,
            'clima': clima,
            'solicitudes_recientes': solicitudes_recientes
        }
        return render(request, "dashboard.html", context)
    else:
        # Página de presentación para usuarios no autenticados
        context = {
            'titulo': 'AgroSoft - Sistema Inteligente de Recomendaciones Agrícolas',
            'descripcion': 'Transforma tu agricultura con inteligencia artificial y datos en tiempo real'
        }
        return render(request, "home.html", context)

@login_required
def dashboard(request):
    """Vista del dashboard para agricultores"""
    solicitudes = SolicitudRecomendacion.objects.filter(agricultor=request.user)
    context = {'solicitudes': solicitudes}
    return render(request, 'dashboard.html', context)