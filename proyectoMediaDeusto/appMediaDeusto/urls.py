from django.urls import path
from . import views

urlpatterns = [
    path('marcas/', views.listaMarcas, name='listaMarcas'),
    path('marcas/<int:idMarca>/', views.detalleMarca, name='detalleMarca'),

    path('dispositivos/', views.listaDispositivos, name='listaDispositivos'),
    path('dispositivos/<int:idDispositivo>/', views.detalleDispositivo, name='detalleDispositivo'),

    path('modelos/', views.listaModelos, name='listaModelos'),
    path('modelos/<int:idModelo>/', views.detalleModelo, name='detalleModelo'),
]
