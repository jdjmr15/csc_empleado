# Generated by Django 4.1.13 on 2025-01-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_empleado_full_name_alter_empleado_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
