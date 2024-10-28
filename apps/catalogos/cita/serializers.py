from rest_framework.serializers import ModelSerializer

from .models import Cita

class CitaSerializer(ModelSerializer):
    class Meta:
        model = Cita
        fields = ['codigo_cita', 'Fecha', 'Hora_cita','Dia_cita','PacienteId']