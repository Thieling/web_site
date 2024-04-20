from django.contrib import admin
from django.urls import path
from .views import (
    view_add_prod_form,
    view_add_compra_form,    
    view_add_usuario_form,
    view_buscar_prod_form,
)

urlpatterns = [
 path("producto/create/", view_add_prod_form, name="producto-create"),
 path("usuario/create/", view_add_usuario_form, name="usuario-create"),
 path("compra/create/", view_add_compra_form, name="compra-create"),
 path("producto/buscar/", view_buscar_prod_form, name="buscar-producto"),
]