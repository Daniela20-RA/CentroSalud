# Generated by Django 4.2 on 2024-10-27 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30, unique=True, verbose_name='Código')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Examenes',
            },
        ),
        migrations.CreateModel(
            name='DetallesConsultaExamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaEntrega', models.DateField(verbose_name='Fecha entrega')),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cita.cita', verbose_name='Cita')),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examen.examen', verbose_name='Examen')),
            ],
            options={
                'verbose_name_plural': 'Detalle Consulta Examenes',
            },
        ),
    ]
