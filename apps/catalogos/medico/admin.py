from django.contrib import admin
from apps.catalogos.medico.models import Medico

@admin.register(Medico)
class ClientesAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'telefono']
    list_display = ['codigo', 'nombres', 'primerApellido', 'segundoApellido', 'direccion', 'telefono' ]

# Register your models here.
