from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    imagenUrlMa = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    marca = models.ForeignKey(Marca, related_name='dispositivos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    imagenUrlDis = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, related_name='modelos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    procesador = models.CharField(max_length=1000, blank=True)
    ram = models.CharField(max_length=1000, blank=True)
    grafica = models.CharField(max_length=1000, blank=True)
    capacidadBateriaMAH = models.IntegerField()
    camara = models.CharField(max_length=100, blank=True)
    audio = models.CharField(max_length=100, blank= True)
    proteccionIP = models.CharField(max_length=1000, blank=True)
    imagenUrlMo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre