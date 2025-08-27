from django.urls import path
from . import views

urlpatterns = [
    path('', views.recomendar_productos, name='recomendar_productos'),
    path('api/precios/', views.api_precios_sipsa, name='api_precios_sipsa'),  # API endpoint
]
