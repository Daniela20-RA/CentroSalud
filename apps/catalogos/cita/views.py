#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Cita, Paciente
from .serializers import CitaSerializer


class CitasApiView(APIView):
    
     @swagger_auto_schema(response={200: CitaSerializer(many=True)})
     def get(self, request):
        citas = Cita.objects.all()
        serializer = CitaSerializer(citas, many=True)
        return Response(serializer.data)

    # Método POST: Crear una nueva cita médica sin validaciones de fecha ni hora
     @swagger_auto_schema(request_body=CitaSerializer, response={201: CitaSerializer})
     def post(self, request):
        serializer = CitaSerializer(data=request.data)
        
        if serializer.is_valid():
            # Guardar la cita sin validaciones de fecha ni hora
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CitaDetail(APIView):
   

    # Método GET: Obtener detalles de una cita específica
    @swagger_auto_schema(responses={200: CitaSerializer})
    def get(self, request, pk):
        try:
            cita = Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            return Response({"error": "Cita no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CitaSerializer(cita)
        return Response(serializer.data)

    # Método PUT: Actualizar una cita completa sin validaciones de fecha ni hora
    @swagger_auto_schema(request_body=CitaSerializer, responses={200: CitaSerializer})
    def put(self, request, pk):
        try:
            cita = Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            return Response({"error": "Cita no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CitaSerializer(cita, data=request.data)
        
        if serializer.is_valid():
         
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método PATCH: Actualizar parcialmente una cita sin validaciones de fecha ni hora
    @swagger_auto_schema(request_body=CitaSerializer, responses={200: CitaSerializer})
    def patch(self, request, pk):
        try:
            cita = Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            return Response({"error": "Cita no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CitaSerializer(cita, data=request.data, partial=True)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método DELETE: Eliminar una cita
    @swagger_auto_schema(response={204: 'No content'})
    def delete(self, request, pk):
        try:
            cita = Cita.objects.get(pk=pk)
        except Cita.DoesNotExist:
            return Response({"error": "Cita no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        
        cita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)