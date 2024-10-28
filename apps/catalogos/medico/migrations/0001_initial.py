# Generated by Django 4.2 on 2024-10-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('primerApellido', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('segundoApellido', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=50, unique=True, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name_plural': 'Medico',
            },
        ),
    ]
