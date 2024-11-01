from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    imagenUrlMa = models.URLField(blank=True, null=True)
    idMarca = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, related_name='dispositivos', on_delete=models.CASCADE)
    imagenUrlDis = models.URLField(blank=True, null=True)
    idDispositivo = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    camara = models.CharField(max_length=100)
    capacidadBateriaMAH = models.IntegerField()
    procesador = models.CharField(max_length=1000)
    dispositivo = models.ForeignKey(Dispositivo, related_name='modelos', on_delete=models.CASCADE)
    imagenUrlMo = models.URLField(blank=True, null=True)
    idModelo =models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre