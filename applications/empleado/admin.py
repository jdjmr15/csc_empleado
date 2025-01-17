from django.contrib import admin

# Register your models here.


from .models import Empleado, Habilidades


class EmpleadoAdmin(admin.ModelAdmin):

    list_display = ("first_name",
                    "last_name",
                    "Departamento",
                    "professional",
                    "full_name",
                    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = ("first_name",)
    list_filter = ("Departamento" , "habilidad",)

    filter_horizontal = ("habilidad",)



admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)