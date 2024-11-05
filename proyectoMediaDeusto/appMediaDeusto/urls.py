from django.urls import path
from . import views

urlpatterns = [
    path('vistaIndex/', views.vistaIndex, name='vistaIndex'),
    
    path('listaMarcas/', views.listaMarcas, name='listaMarcas'),
    path('detalleMarca/<int:id_marca>/', views.detalleMarca, name='detalleMarca'),

    path('listaDispositivos/', views.listaDispositivos, name='listaDispositivos'),
    path('detalleDispositivo/<int:id_dispositivo>/', views.detalleDispositivo, name='detalleDispositivo'),

    path('listaModelos/', views.listaModelos, name='listaModelos'),
    path('detalleModelo/<int:id_modelo>/', views.detalleModelo, name='detalleModelo'),

    path('listaDispositivosPorMarca/<int:id_marca>/', views.listaDispositivosPorMarca, name='listaDispositivosPorMarca'),
    path('listaModelosPorDispositivo/<int:id_dispositivo>/', views.listaModelosPorDispositivo, name='listaModelosPorDispositivo')
]
