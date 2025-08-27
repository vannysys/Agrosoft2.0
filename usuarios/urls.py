from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('cambiar-contrasena/<str:token>/', views.cambiar_contrasena, name='cambiar_contrasena'),
    
    # API para datos del dashboard
    path('api/dashboard-data/', views.dashboard_data_api, name='dashboard_data_api'),
    
    # Nuevas URLs para funcionalidades administrativas
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/usuarios/', views.gestionar_usuarios, name='gestionar_usuarios'),
    path('admin/reporte-cultivos/', views.reporte_cultivos, name='reporte_cultivos'),
    path('admin/produccion-proyectada/', views.produccion_proyectada, name='produccion_proyectada'),
    path('reportes-graficos/', views.reportes_graficos, name='reportes_graficos'),
    
    path('', views.home, name='home'),
]
