from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'

class ResumenView(TemplateView):
    template_name = 'home/resumen.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['Rojo', 'Verde', 'Azul', 'Amarillo']
    context_object_name = 'colores'

class ModeloPruebaListView(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/home'