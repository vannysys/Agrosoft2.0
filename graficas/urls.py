from django.urls import path
from .views import GraficasDataView, GraficasRecomendacionesView

urlpatterns = [
    path('api/graficas/datos/', GraficasDataView.as_view(), name='graficas_datos'),
    path('api/graficas/recomendaciones/', GraficasRecomendacionesView.as_view(), name='graficas_recomendaciones'),
]
