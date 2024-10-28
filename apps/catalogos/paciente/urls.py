from django.urls import path
from .views import PacienteApiView, PacienteDetails

app_name = 'paciente'

urlpatterns = [
    path('', PacienteApiView.as_view(), name='paciente'),
    path('<int:pk>/', PacienteDetails.as_view()), #para delete,pust,pucth
    
]