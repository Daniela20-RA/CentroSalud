from django.urls import path, include

urlpatterns = [
    path('paciente/', include('apps.catalogos.paciente.urls')),
    path('medico/', include('apps.catalogos.medico.urls')),
    path('cita/', include('apps.catalogos.cita.urls')),
    path('consulta/', include('apps.catalogos.consulta.urls')),
]