from django.shortcuts import render

# Create your views here.
from  django.views.generic.edit import FormView 
from django.views.generic import ListView

from applications.empleado.models import Empleado

from .models import Departamento
from .forms import NuevoDepartamentoForm


class RegistrarDepartamentoView(FormView):
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NuevoDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        # logica departamento.
        dep = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )

        dep.save()

        emp = Empleado.objects.create(
            first_name=form.cleaned_data['nombre'],
            last_name=form.cleaned_data['apellidos'],
            professional='1',
            Departamento=dep
        )

        emp.save()

        return super().form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista_departamento.html"
    context_object_name = 'departamentos'
