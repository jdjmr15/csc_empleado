
from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('', views.ListAllEmpleados.as_view(), name='empleados'),
]