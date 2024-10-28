from rest_framework.serializers import ModelSerializer

from .models import Medico

class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = ['codigo', 'nombres', 'primerApellido','segundoApellido','direccion','telefono']