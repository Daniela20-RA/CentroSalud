from django.contrib import admin

from apps.catalogos.paciente.models import Paciente

@admin.register(Paciente)
class ClientesAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'telefono']
    list_display = ['codigo', 'nombres', 'primerApellido', 'segundoApellido', 'direccion', 'telefono' ]

# Register your models here.
