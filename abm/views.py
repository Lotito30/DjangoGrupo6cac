from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Producto,Cliente
from .forms import ProductoForm,ClienteForm

modelProductos = Producto.objects.all()

title = {
    "home":"Home - DecorArte",
    "productos":"Productos - DecorArte",
    "editar":"Editar - DecorArte",
    "agregar":"Agregar - DecorArte",
    "acercade":"Acerca De - DecorArte",
    "contacto":"Contacto - DecorArte",
    "comprar":"Comprar - DecorArte"
}
class ProductoListView(ListView): #Esta clase sirve para listar los productos con la libreria ListView
    model = Producto
    context_object_name = 'productos'
    
#Esta clase sirve para crear el formulario para crear los productos con la libreria CreateView y hereda de ProductoListView para tener el contexto y pasarlo para que renderice los productos y tener las opciones de editar y eliminar
class CrearProductoView(CreateView,ProductoListView): 
    model = Producto
    form_class = ProductoForm
    success_url = '/agregarproducto'

#Esta clase sirve para crear el formulario para contacto con la libreria CreateView y hereda de ProductoListView para tener el contexto y pasarlo para que renderice los productos y tener las opciones de editar y eliminar
class CrearClienteView(CreateView,ProductoListView):
    model = Cliente
    form_class = ClienteForm
    success_url = '/contacto'


def index(request):
    productos = Producto.objects.all()
    return render(request,
                'index.html',
                    {
                    'title': title['home'],
                    'productos':productos
                    }
                )
def editar(request,id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
        return redirect("/agregarproducto")

    return render(request,'editar.html',{'form':form, 'producto':producto, 'title':title['editar']})

def eliminar(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('/agregarproducto')

def comprar(request,id):
    producto = get_object_or_404(Producto, id=id)
    return render(request,
                  "comprar.html",
                    {
                    'title':title['comprar'],
                    'producto': producto
                    }
                    )
    
def acercaDe(request):
    return render(request,
                    "acercade.html",
                    {
                        'title':title['acercade']
                    }
                
                )
