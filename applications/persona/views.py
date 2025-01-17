from django.shortcuts import render

from django.views.generic import ListView



# Create your views here.

from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/../../templates/empleado/listado_personas.html'
    model = Empleado
    context_object_name = 'listado_empleados'
