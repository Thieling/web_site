from django.contrib import admin
from .models import Producto, Usuario, Compra

# Register your models here.
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Compra)