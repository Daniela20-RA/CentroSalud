from django.contrib import admin

from apps.movimiento.examen.models import Examen, DetallesConsultaExamen

@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion'] 

@admin.register(DetallesConsultaExamen)
class DetalleExamenAdmin(admin.ModelAdmin):
    list_display = ('examen', 'cita', 'fechaEntrega')

# Register your models here.
