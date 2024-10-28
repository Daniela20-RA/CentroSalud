from django.db import models
from apps.catalogos.cita.models import Cita

class Consulta(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    Descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    citaId = models.ForeignKey(Cita, verbose_name='Cita', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Consulta'

    def __str__(self):
        return f"{self.codigo}-{self.Descripcion}"

# Create your models here.
