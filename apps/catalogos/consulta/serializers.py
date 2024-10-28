from rest_framework.serializers import ModelSerializer 
from apps.catalogos.consulta.models import Consulta

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['codigo', 'Descripcion', 'citaId']