#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import Medico
from .serializers import MedicoSerializer


class MedicoApiView(APIView):
   @swagger_auto_schema(response={200: MedicoSerializer(many=True)})
   def get(self, request):
       medico = Medico.objects.all()
       serializer = MedicoSerializer(medico, many=True)
       return Response(serializer.data)   
   
   @swagger_auto_schema(request_body=MedicoSerializer, response={201: MedicoSerializer})
   def post(self, request):
     serializer = MedicoSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedicoDetails(APIView):
    #Para obtener, actualizar y eliminar a un medico en especifico

    @swagger_auto_schema(responses={200: MedicoSerializer})
    def get(self, request, pk):
           
        try:
            medico= Medico.objects.get(pk=pk)
        except Medico.DoesNotExist:
            return Response ({'Error': 'Medico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PacienteSerializer(medico)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=MedicoSerializer, responses={201: MedicoSerializer})
    def put(self, request, pk):

        try:
            medico= Medico.objects.get(pk=pk)
        except Medico.DoesNotExist:
            return Response ({'Error': 'Medico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicoSerializer(medico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=MedicoSerializer, responses={201: MedicoSerializer})
    def patch(self, request, pk):
        try:
            medico = Medico.objects.get(pk=pk)
        except Medico.DoesNotExist:
            return Response({'Error': 'Medico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicoSerializer(medico, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):
        try:
            medico = Medico.objects.get(pk=pk)
        except Medico.DoesNotExist:
            return Response ({'Error': 'Medico no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        Medico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
       

# Create your views here.
