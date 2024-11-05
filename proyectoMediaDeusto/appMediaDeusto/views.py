from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Marca, Dispositivo, Modelo


#VISTA INDEX
def index(request):
    return render(request, 'index.html')




#DETALLE Y LISTA MARCAS
def detalleMarca(request, id_marca):
    marca = get_object_or_404(Marca, pk=id_marca)
    contexto = {'marca': marca}
    return render (request, 'detalleMarca.html', contexto)

def listaMarcas(request):
    marcas = Marca.objects.order_by('nombre')
    contexto = {'marca_list': marcas}
    return render(request, 'listaMarcas.html', contexto)




#DETALLE Y LISTA DISPOSITIVOS
def detalleDispositivo(request, id_dispositivo):
    dispositivo = get_object_or_404(Dispositivo, pk=id_dispositivo)
    contexto = {'dispositivo': dispositivo}
    return render(request, 'detalledispositivo.html', contexto)

def listaDispositivos(request):
    dispositivos = Dispositivo.objects.order_by('nombre')
    contexto = {'dispositivo_list': dispositivos}
    return render(request, 'listaDispositivos.html', contexto)




#DETALLE Y LISTA MODELOS
def detalleModelo(request, id_modelo):
    modelo = get_object_or_404(Modelo, pk=id_modelo)
    contexto = {'modelo': modelo}
    return render(request, 'detalleModelo.html', contexto)

def listaModelos(request):
    modelos = Modelo.objects.order_by('nombre')
    contexto = {'modelo_list': modelos}
    return render(request, 'listaModelos.html', contexto)



#VISTAS DE LISTAS FILTRADAS
def listaDispositivosPorMarca(request, id_marca):
    marca = get_object_or_404(Marca, pk=id_marca)
    dispositivos = Dispositivo.objects.filter(marca=marca)
    contexto = {'marca':marca,'dispositivo_list': dispositivos}
    return render(request, 'listaDispositivosPorMarca.html', contexto)

def listaModelosPorDispositivo(request, id_dispositivo):
    dispositivo = get_object_or_404(Dispositivo, pk=id_dispositivo)
    modelos = Modelo.objects.filter(dispositivo=dispositivo)
    contexto = {'dispositivo':dispositivo,'modelo_list': modelos}
    return render(request, 'listaModelosPorDispositivo.html', contexto)