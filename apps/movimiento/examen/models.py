from django.db import models
from apps.catalogos.cita.models import Cita



class Examen(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    
    class Meta:
        verbose_name_plural = 'Examenes'

    def __str__(self) -> str:
        return f"{self.codigo} - {self.descripcion}"
    

# Create your models here.

class DetallesConsultaExamen(models.Model):
    examen = models.ForeignKey(Examen, verbose_name='Examen', on_delete=models.PROTECT)
    cita = models.ForeignKey(Cita, verbose_name='Cita', on_delete=models.PROTECT)
    fechaEntrega = models.DateField(verbose_name='Fecha entrega')

    class Meta:
        verbose_name_plural = 'Detalle Consulta Examenes'

    def __str__(self):
        return f"examen: {self.examen.descripcion}, cita: {self.cita.PacienteId}, fechaEntrega: {self.fechaEntrega}"

