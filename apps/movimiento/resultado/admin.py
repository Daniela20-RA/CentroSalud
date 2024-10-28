from django.contrib import admin

from apps.movimiento.resultado.models import Resultado,DetalleResultadoExamen

@admin.register(Resultado)
class ConsultaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion', 'examen']

@admin.register(DetalleResultadoExamen)
class ResultadoExamenAdmin(admin.ModelAdmin):
    list_display = ['detalleconsultaExamen', 'resultado']

# Register your models here.
