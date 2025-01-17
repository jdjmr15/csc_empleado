from django.urls import path, include

from . import views 

app_name = 'departamento_app'

urlpatterns = [
    path('crear/', views.RegistrarDepartamentoView.as_view(), name='crear_departamento'),
    path('', views.DepartamentoListView.as_view(), name='listar_departamento'),
]