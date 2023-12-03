from django import forms

from .models import Producto, Cliente, Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente']