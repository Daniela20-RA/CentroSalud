from django.urls import path
from .views import MedicoApiView,MedicoDetails

app_name = 'Medico'

urlpatterns = [
    path('', MedicoApiView.as_view(), name='Medico'),
    path('<int:pk>/', MedicoDetails.as_view()), #para delete,pust,pucth
    
]