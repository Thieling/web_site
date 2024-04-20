from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import Producto, Usuario, Compra
from .forms import ProductoCreateForm, UsuarioCreateForm, CompraCreateForm, ProductoSearchForm

# Create your views here.

#def view_buscar_prod_form(request, cod_pro):
#    cod_producto = Producto.objects.filter(nombre_producto=cod_pro).all()
#    contexto_busc = {"producto": cod_producto}
#    return render(request, "TecHard/lista_prod.html", contexto_busc)

#def view_searchproducto_form(request):
#    buscar = request.GET.get("buscar")
#    productos = Producto.objects.all()

#    if buscar:
#        productos = Producto.objects.filter(
#            Q(nom_pro__icontains = buscar)
#            #nom_pro__incontains busca en el campo nom_pro
#            #si hay algo parecido al objeto a buscarS
#        ).distinct
#
#    return render(request, 'TecHard/buscar-producto.html', {'productos': productos})

def view_buscar_prod_form(request):
    if request.method == "GET":
        form = ProductoSearchForm()
        return render(
            request, "TecHard/buscar-producto.html", context={"search_form": form}
        )
    elif request.method == "POST":
        #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
        form = ProductoSearchForm(request.POST)
        if form.is_valid():
            nom_pro = form.cleaned_data["nombre"]#[]se usa el campo puesto en el formulario
            lista_productos = Producto.objects.filter(
            Q(nom_pro__icontains = nom_pro)
        ).distinct()
        contexto_dict = {"lista": lista_productos}
        return render(request, "TecHard/lista_prod.html", contexto_dict)
#    if request.method == "GET":
#        form = ProductoSearchForm()
#        return render(
#            request, "TecHard/buscar-producto.html", context={"search_form": form}
#        )
#    elif request.method == "POST":
#        #  devolverle a "chrome" la lista de reservas encontrada o avisar que no se encontró nada
#        form = ProductoSearchForm(request.POST)
#        if form.is_valid():
#            nom_pro = form.cleaned_data["nom_pro"]
#            lista_productos = Producto.objects.filter(
#            #nom_pro=nom_pro
#            Q(nom_pro__icontains = nom_pro)
#            #nom_pro__incontains busca en el campo nom_pro
#            #si hay algo parecido al objeto a buscarS
#       ).distinct
#        contexto_dict = {"todos_los_productos": lista_productos}
#        return render(request, "TecHard/buscar-producto.html", contexto_dict)


def view_add_usuario_form(request):
    data = {
        'form': UsuarioCreateForm()
    }

    if request.method == 'POST':
        formulario=UsuarioCreateForm(data=request.POST)
        if formulario.is_valid():
            formulario.save() #guarda el formulario si los datos que vinieron son validos
            data["mensaje"] = "Usuario Creado"
        else:
            data["form"] = formulario #si el formulario tiene datos invaliods reenvio el formulario

    return render(request, 'TecHard/create-usuario.html', data)


def view_add_prod_form(request):
    data = {
        'form': ProductoCreateForm()
    }

    if request.method == 'POST':
        formulario=ProductoCreateForm(data=request.POST)
        if formulario.is_valid():
            formulario.save() #guarda el formulario si los datos que vinieron son validos
            data["mensaje"] = "Producto agregado"
        else:
            data["form"] = formulario #si el formulario tiene datos invaliods reenvio el formulario

    return render(request, 'TecHard/create-producto.html', data)

def view_add_compra_form(request):
    data = {
        'form': CompraCreateForm()
    }

    if request.method == 'POST':
        formulario=CompraCreateForm(data=request.POST)
        if formulario.is_valid():
            formulario.save() #guarda el formulario si los datos que vinieron son validos
            data["mensaje"] = "Compra Realizada"
        else:
            data["form"] = formulario #si el formulario tiene datos invaliods reenvio el formulario

    return render(request, 'TecHard/create-compra.html', data)