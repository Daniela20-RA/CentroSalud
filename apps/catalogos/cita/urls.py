from django.urls import path
from .views import CitasApiView,CitaDetail

app_name = 'Cita'

urlpatterns = [
    path('', CitasApiView.as_view(), name='Cita'),
    path('<int:pk>/', CitaDetail.as_view()), #para delete,pust,pucth
    
]