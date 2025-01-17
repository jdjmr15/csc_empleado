import os
from django.conf import settings
from django.shortcuts import  redirect

# Create your views here.
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  TemplateView,
                                  UpdateView,
                                  DeleteView
                                  )

from .models import Empleado
from django.urls import reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger



class InicioView(TemplateView):
    template_name = 'empleado/inicio.html'


class ListAdminEmpleados(ListView):
    template_name = 'empleado/listado_personas_admin.html'
    context_object_name = 'listado_empleados_admin'
    paginate_by = 5
    model = Empleado

    ordering = 'id'


class ListAllEmpleados(ListView):
    template_name = 'empleado/listado_personas.html'
    context_object_name = 'listado_empleados'
    paginate_by = 3

    def get_queryset(self):
        palabra = self.request.GET.get('kword', '')        
        return Empleado.objects.filter(
            first_name__icontains=palabra.lower()
        ).order_by('id')

    def paginate_queryset(self, queryset, page_size):
        """
        Paginate the queryset for the view.
        """
        paginator = self.get_paginator(queryset, page_size)
        page = self.request.GET.get('page')

        try:
            page_number = int(page)
        except (TypeError, ValueError):
            page_number = 1

        try:
            page_obj = paginator.page(page_number)
        except (EmptyPage, PageNotAnInteger):
            page_obj = paginator.page(paginator.num_pages)

        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())

class ListAreaEmpleados(ListView):
    template_name = 'empleado/listado_personas_areas.html'
    context_object_name = 'listado_empleados'

    def get_queryset(self):
        area = self.kwargs['area']
        return Empleado.objects.filter(
            Departamento__short_name=area
        )


class ListEmpleadoByWord(ListView):
    template_name = 'empleado/listado_by_words.html'
    context_object_name = 'listado_empleados_by_words'
    #model = Empleado

    def get_queryset(self):
        palabra = self.request.GET.get('kword', )
        print('Palabra buscada:', palabra)
        return Empleado.objects.filter(
            first_name__icontains=palabra.lower()
        )


class ListEmpleadoHabilidades(ListView):
    template_name = 'empleado/listado_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        palabra = self.request.GET.get('kword', )
        empleado = Empleado.objects.get(first_name__icontains=palabra)

        return empleado.habilidad.all()


class EmpleadoVistaDetalle(DetailView):
    template_name = 'empleado/detalle_empleado.html'
    model = Empleado
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado = self.get_object()
        foto_path = os.path.join(settings.MEDIA_ROOT, str(empleado.Foto))
        context['foto_exists'] = os.path.isfile(foto_path)
        return context

class VistaCompletada(TemplateView):
    template_name = "empleado/completado.html"


class EmpleadoCreateView(CreateView):
    template_name = 'empleado/crear_empleado.html'
    model = Empleado
    fields = ('first_name', 'last_name', 'Departamento',  'Foto', 'professional', 'habilidad')
    #success_url = '../empleado_completado'

    def get_success_url(self):
        #return reverse_lazy('empleado_detalle', kwargs={'pk': self.object.pk})
        return reverse_lazy('empleado_app:empleado_admin')


class EmpleadoEditarView(UpdateView):
    template_name = 'empleado/editar_empleado.html'
    model = Empleado
    fields = ('first_name', 'last_name', 'Departamento', 'Foto', 'professional', 'habilidad')

    def post(self, request, *args, **kwargs): 
        print('Estamos editando un registro')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.full_name = self.object.first_name + ' ' + self.object.last_name
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        #return reverse_lazy('empleado_app:empleado_detalle', kwargs={'pk': self.object.pk})
        return reverse_lazy('empleado_app:empleado_admin')


class EmpleadoEliminarView(DeleteView):
    template_name = 'empleado/eliminar_empleado.html'
    model = Empleado
    context_object_name = 'empleado'
    success_url = reverse_lazy('empleado_app:empleado_admin')