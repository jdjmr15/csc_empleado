
from django.contrib import admin
from django.urls import path


from . import views

app_name = 'empleado_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar', views.ListAllEmpleados.as_view(), name='lista_empleados'),
    path('areas/<area>', views.ListAreaEmpleados.as_view(), name='empleados_areas'),
    path('buscar/', views.ListEmpleadoByWord.as_view(), name='empleados_words'),
    path('habilidades/', views.ListEmpleadoHabilidades.as_view(), name='empleados_habilidades'),
    path('detalle/<pk>/', views.EmpleadoVistaDetalle.as_view(), name='empleado_detalle'),
    path('crear/', views.EmpleadoCreateView.as_view(), name='empleado_crear'),
    path('completado/', views.VistaCompletada.as_view(), name='completada'),
    path('editar/<pk>/', 
          views.EmpleadoEditarView.as_view(), 
          name='empleado_editar'
    ),
    path('admin/', 
          views.ListAdminEmpleados.as_view(), 
          name='empleado_admin'
    ),
    path('eliminar/<pk>/', 
          views.EmpleadoEliminarView.as_view(), 
          name='empleado_eliminar'
    ),
]