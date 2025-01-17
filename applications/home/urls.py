from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('colores', views.PruebaListView.as_view(), name='color'),
    path('titulos', views.ModeloPruebaListView.as_view(), name='titulo'),
    path('agregar', views.PruebaCreateView.as_view(), name='agregar'),
    path('resumen', 
         views.ResumenView.as_view(), 
         name='resumen'
    ),
]