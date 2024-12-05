from django.views.generic import ListView, DetailView
from .models import Marca, Dispositivo, Modelo

# Vista índice
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

# Detalle y lista de marcas
class DetalleMarcaView(DetailView):
    model = Marca
    template_name = 'detalleMarca.html'
    context_object_name = 'marca'

class ListaMarcasView(ListView):
    model = Marca
    template_name = 'listaMarcas.html'
    context_object_name = 'marca_list'
    queryset = Marca.objects.order_by('nombre')

# Detalle y lista de dispositivos
class DetalleDispositivoView(DetailView):
    model = Dispositivo
    template_name = 'detalleDispositivo.html'
    context_object_name = 'dispositivo'

class ListaDispositivosView(ListView):
    model = Dispositivo
    template_name = 'listaDispositivos.html'
    context_object_name = 'dispositivo_list'
    queryset = Dispositivo.objects.order_by('nombre')

# Detalle y lista de modelos
class DetalleModeloView(DetailView):
    model = Modelo
    template_name = 'detalleModelo.html'
    context_object_name = 'modelo'

class ListaModelosView(ListView):
    model = Modelo
    template_name = 'listaModelos.html'
    context_object_name = 'modelo_list'
    queryset = Modelo.objects.order_by('nombre')

# Vistas de listas filtradas
class ListaDispositivosPorMarcaView(ListView):
    model = Dispositivo
    template_name = 'listaDispositivosPorMarca.html'
    context_object_name = 'dispositivo_list'

    def get_queryset(self):
        return Dispositivo.objects.filter(marca_id=self.kwargs['pk']).order_by('nombre')

class ListaModelosPorDispositivoView(ListView):
    model = Modelo
    template_name = 'listaModelosPorDispositivo.html'
    context_object_name = 'modelo_list'

    def get_queryset(self):
        return Modelo.objects.filter(dispositivo_id=self.kwargs['pk']).order_by('nombre')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Llama al método padre para obtener el contexto inicial
        context = super().get_context_data(**kwargs)
        # Define la lista de modelos
        context['modelos'] = [
            {'imagen': '../static/style/iphone16.jpeg', 'precio': '950€'},
            {'imagen': '../static/style/Victus.jpg', 'precio': '825€'},
            {'imagen': '../static/style/RelojGalaxy.jpg', 'precio': '300€'},
            {'imagen': '../static/style/galaxy S24 Ultra.webp', 'precio': '1100€'},
            {'imagen': '../static/style/relojAppleS10.png', 'precio': '450€'},
            {'imagen': '../static/style/lenovoIdepadSlim3.webp', 'precio': '650€'},
            {'imagen': '../static/style/redmiNote13Pro.webp', 'precio': '750€'},
            {'imagen': '../static/style/macbookProM4.jpeg', 'precio': '1325€'},
            {'imagen': '../static/style/omenTranscend.jpg', 'precio': '1550€'},
        ]
        return context