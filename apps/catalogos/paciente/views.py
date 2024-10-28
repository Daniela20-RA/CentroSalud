#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Paciente 
from .serializers import PacienteSerializer


class PacienteApiView(APIView):
   @swagger_auto_schema(response={200: PacienteSerializer(many=True)})
   def get(self, request):
       paciente = Paciente.objects.all()
       serializer = PacienteSerializer(paciente, many=True)
       return Response(serializer.data)   
   
   @swagger_auto_schema(request_body=PacienteSerializer, response={201: PacienteSerializer})
   def post(self, request):
     serializer = PacienteSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PacienteDetails(APIView):
    #Para obtener, actualizar y eliminar a un paciente en especifico

    @swagger_auto_schema(responses={200: PacienteSerializer})
    def get(self, request, pk):
           
        try:
            paciente= Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            return Response ({'Error': 'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=PacienteSerializer, responses={201: PacienteSerializer})
    def put(self, request, pk):

        try:
            paciente= Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            return Response ({'Error': 'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=PacienteSerializer, responses={201: PacienteSerializer})
    def patch(self, request, pk):
        try:
            Paciente = Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            return Response({'Error': 'Paciente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PacienteSerializer(Paciente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):
        try:
            paciente = Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            return Response ({'Error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        paciente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
       