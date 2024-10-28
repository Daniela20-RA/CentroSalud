from django.contrib import admin
from apps.catalogos.consulta.models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'Descripcion']

# Register your models here.
