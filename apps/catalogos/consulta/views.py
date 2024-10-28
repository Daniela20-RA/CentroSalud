#from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.catalogos.consulta.models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

# Create your views here.
