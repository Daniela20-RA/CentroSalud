from django.db import models
from apps.catalogos.paciente.models import Paciente
from apps.catalogos.medico.models import Medico

class Cita(models.Model):
    codigo_cita = models.CharField(verbose_name='Código', max_length=30, unique=True)
    Fecha = models.DateField(verbose_name= 'Fecha')
    Hora_cita = models.DateTimeField(verbose_name= 'Hora')
    Dia_cita = models.CharField(verbose_name='Día', max_length=20)
    PacienteId = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.PROTECT)
    MedicoId = models.ForeignKey(Medico, verbose_name='Medico', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Cita'

    def __str__(self):
        return f"{self.codigo_cita} - {self.Fecha}-{self.Hora_cita} - {self.Dia_cita}"

# Create your models here.
