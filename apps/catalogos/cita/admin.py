from django.contrib import admin

from apps.catalogos.cita.models import Cita

@admin.register(Cita)
class ConsultaAdmin(admin.ModelAdmin):
    search_fields = ['codigo_cita', 'PacienteId']
    list_display = ['codigo_cita','Fecha','Hora_cita','Dia_cita', 'PacienteId']
# Register your models here.
