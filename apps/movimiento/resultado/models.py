from django.db import models
from apps.movimiento.examen.models import Examen
from apps.movimiento.examen.models import DetallesConsultaExamen

class Resultado(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    examen = models.ForeignKey(Examen,verbose_name='Examen', on_delete=models.PROTECT )

    class Meta:
        verbose_name_plural = 'Resultados'
            
    def __str__(self):
        return f"{self.codigo} - {self.descripcion} "

# Create your models here.

class DetalleResultadoExamen(models.Model):
    detalleconsultaExamen = models.ForeignKey(DetallesConsultaExamen, verbose_name='Detalle Examen', on_delete=models.PROTECT)
    resultado = models.ForeignKey(Resultado,verbose_name='Resultado', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalle Resultados Examenes'
            
    def __str__(self):
        return f"{self.detalleconsultaExamen} - {self.resultado}"
