from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Marca, Dispositivo, Modelo

def listaMarcas(request):
    marcas = Marca.objects.order_by('nombre')
    nombres_marcas = ', '.join([marca.nombre for marca in marcas])
    return HttpResponse(nombres_marcas)

def detalleMarca(request, idMarca):
    try:
        marca = Marca.objects.get(pk=idMarca)
        dispositivos = marca.dispositivos.all() 

        cadenaDeTexto = f"{marca.nombre}\n"

        if dispositivos.exists():
            cadenaDeTexto += "Dispositivos:\n"
            for dispositivo in dispositivos:
                cadenaDeTexto += f"- {dispositivo.nombre}\n"
        else:
            cadenaDeTexto += "No hay dispositivos asociados a esta marca."

        return HttpResponse(cadenaDeTexto)
    except Marca.DoesNotExist:
        return HttpResponseNotFound("Marca no encontrada")

def listaDispositivos(request):
    dispositivos = Dispositivo.objects.order_by('nombre')
    nombres_dispositivos = ', '.join([dispositivo.nombre for dispositivo in dispositivos])
    return HttpResponse(nombres_dispositivos)

def detalleDispositivo(request, idDispositivo):
    try:
        dispositivo = Dispositivo.objects.get(pk=idDispositivo)
        modelos = dispositivo.modelos.all()  # Accedemos al related_name "modelos"

        cadenaDeTexto = f"Dispositivo: {dispositivo.nombre}, Número de serie: {dispositivo.numeroSerie}\n"

        if modelos.exists():
            cadenaDeTexto += "Modelos:\n"
            for modelo in modelos:
                cadenaDeTexto += (
                    f"- {modelo.nombre}, Cámara: {modelo.camara}, "
                    f"Capacidad de batería: {modelo.capacidadBateriaMAH} mAh, Procesador: {modelo.procesador}\n"
                )
        else:
            cadenaDeTexto += "No hay modelos asociados a este dispositivo."

        return HttpResponse(cadenaDeTexto)
    except Dispositivo.DoesNotExist:
        return HttpResponseNotFound("Dispositivo no encontrado")

def listaModelos(request):
    modelos = Modelo.objects.order_by('nombre')
    nombres_modelos = ', '.join([modelo.nombre for modelo in modelos])
    return HttpResponse(nombres_modelos)

def detalleModelo(request, idModelo):
    try:
        modelo = Modelo.objects.get(pk=idModelo)

        cadenaDeTexto = (
            f"Modelo: {modelo.nombre}, Cámara: {modelo.camara}, "
            f"Capacidad de batería: {modelo.capacidadBateriaMAH} mAh, Procesador: {modelo.procesador}\n"
        )

        return HttpResponse(cadenaDeTexto)
    except Modelo.DoesNotExist:
        return HttpResponseNotFound("Modelo no encontrado")