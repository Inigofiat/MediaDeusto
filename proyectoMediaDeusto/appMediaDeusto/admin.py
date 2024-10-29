from django.contrib import admin

from .models import Marca, Modelo, Dispositivo

admin.site.register(Marca)
admin.site.register(Dispositivo)
admin.site.register(Modelo)

# Register your models here.
