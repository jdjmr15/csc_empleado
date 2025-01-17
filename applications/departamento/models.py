from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name= models.CharField('Nombre corto', max_length=20)
    active = models.BooleanField("Activo", default=False)

    def __str__(self):
        return self.name


    class Meta:

        verbose_name_plural = 'Departamentos'
        ordering = ['name']