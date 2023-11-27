from django import forms

from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'