from django import forms
from .models import Producto, Usuario, Compra

class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nom_pro', 'desc', 'stock', 'precio']
        labels = {
            'cod_pro': 'Codigo de producto',
            'nom_pro': 'Nombre de producto',
            'desc': 'Descripcion',
            'stock': 'Stock del producto',
            'precio': 'Precio por unidad',
        }

class UsuarioCreateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nom_usr', 'nom', 'ape', 'dni', 'tel', 'email']
        labels = {
            'nom_usr': 'Nombre de Usario',
            'nom': 'Nombre/s',
            'ape': 'Apellido/s',
            'dni': 'Numero DNI',
            'tel': 'Telefono de contacto',
            'email': 'Correo Electronico',
        }

class CompraCreateForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cod_compra', 'cod_pro', 'cant', 'nom_usr']
        labels = {
            'cod_compra': 'Codigo de la Compra',
            'cod_pro': 'Codigo del Producto',
            'cant': 'Cantidad',
            'nom_usr': 'Nombre de Usuario',
        }

class ProductoSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre del producto"
    )