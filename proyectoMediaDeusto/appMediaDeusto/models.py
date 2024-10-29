from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    id = models.IntegerField()

def __str__(self):
    return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    numeroSerie = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, related_name='dispositivos', on_delete=models.CASCADE)

def __str__(self):
    return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    camara = models.CharField(max_length=100)
    capacidadBateriaMAH = models.IntegerField()
    procesador = models.CharField(max_length=1000)
    dispositivo = models.ForeignKey(Dispositivo, related_name='modelos', on_delete=models.CASCADE)

def __str__(self):
    return self.nombre

# Create your models here.