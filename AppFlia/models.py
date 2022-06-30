from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre=models.CharField(max_length=60)
    relacion=models.CharField(max_length=60)
    fecha_nac=models.DateField()
    mayor_de_edad=models.BooleanField()

