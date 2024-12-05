from django.urls import path
from django.urls import path
from .views import (
    IndexView, 
    ListaMarcasView,
    DetalleMarcaView,
    ListaDispositivosView,
    DetalleDispositivoView,
    ListaModelosView,
    DetalleModeloView,
    ListaDispositivosPorMarcaView,
    ListaModelosPorDispositivoView
)

urlpatterns = [
    # Todas las vistas convertidas a CBV usan .as_view()
    path('index/', IndexView.as_view(), name='index'),

    path('listaMarcas/', ListaMarcasView.as_view(), name='listaMarcas'),
    path('detalleMarca/<int:pk>/', DetalleMarcaView.as_view(), name='detalleMarca'),

    path('listaDispositivos/', ListaDispositivosView.as_view(), name='listaDispositivos'),
    path('detalleDispositivo/<int:pk>/', DetalleDispositivoView.as_view(), name='detalleDispositivo'),

    path('listaModelos/', ListaModelosView.as_view(), name='listaModelos'),
    path('detalleModelo/<int:pk>/', DetalleModeloView.as_view(), name='detalleModelo'),

    path('listaDispositivosPorMarca/<int:pk>/', ListaDispositivosPorMarcaView.as_view(), name='listaDispositivosPorMarca'),
    path('listaModelosPorDispositivo/<int:pk>/', ListaModelosPorDispositivoView.as_view(), name='listaModelosPorDispositivo')
]
