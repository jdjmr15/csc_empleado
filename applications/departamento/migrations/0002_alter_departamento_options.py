# Generated by Django 4.1.13 on 2024-12-11 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name_plural': 'Departamentos'},
        ),
    ]