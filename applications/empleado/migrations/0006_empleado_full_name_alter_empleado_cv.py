# Generated by Django 4.1.13 on 2024-12-28 19:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0005_empleado_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre_Completo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cv',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
