from django.contrib import admin
from django.urls import path, include
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usuarios_views.home, name='inicio'),  # Página principal ahora apunta a usuarios home
    path('usuarios/', include('usuarios.urls')),  # Incluir URLs de usuarios
    # path('api/', include('usuarios.urls')),  # Incluir URLs de usuarios para la API
    path('recomendar/', include('productores.urls')),  # Incluir URLs de productores
    path('graficas/', include('graficas.urls')),  # Incluir URLs de gráficas
]
