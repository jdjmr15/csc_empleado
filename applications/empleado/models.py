from django.db import models

from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return self.habilidad

    class Meta:
        verbose_name_plural = 'Habilidades'



class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name = models.CharField("Nombres", max_length=50)
    last_name = models.CharField("Apellidos", max_length=50)
    full_name = models.CharField("Nombre_Completo", max_length=100, blank=True)
    professional = models.CharField('Profesión',choices=JOB_CHOICES, max_length=1)
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE, name='Departamento')
    photo = models.ImageField(name='Foto', upload_to='empleado', blank=True, null=True)

    habilidad = models.ManyToManyField(Habilidades)
    cv = RichTextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name