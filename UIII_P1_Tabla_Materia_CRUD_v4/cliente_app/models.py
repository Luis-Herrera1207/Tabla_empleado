from django.db import models

# Create your models here.

class Cliente (models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    telefono=models.CharField(max_length=25)
    fecha_nac=models.DateField(max_length=6)
    direccion=models.IntegerField(max_length=100)
    cp=models.IntegerField(max_length=10)
    curp=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre