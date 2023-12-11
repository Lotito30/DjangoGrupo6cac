from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from datetime import datetime
from django.contrib import messages

from .models import Producto, Cliente, Venta
from .forms import ProductoForm,ClienteForm,VentaForm

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
class VentasListView(ListView): #Esta clase sirve para listar las ventas con la libreria ListView
    model = Venta
    context_object_name = 'ventas'
class CrearClienteView(CreateView,ProductoListView):
    model = Cliente
    form_class = ClienteForm
    success_url = '/iniciarSesion'

    def form_valid(self, form):
        cliente = form.save(commit=False)
        if Cliente.objects.filter(email=cliente.email).exists():
            messages.info(self.request, 'Cliente reconocido, ¡Sigue explorando y disfrutando de nuestro sitio web!')
            return redirect('/iniciarSesion')
        else:
            messages.success(self.request, 'Acción realizada con éxito.')
            cliente.save()
            return super().form_valid(form)
#Esta clase sirve para crear el formulario para crear los productos con la libreria CreateView y hereda de ProductoListView para tener el contexto y pasarlo para que renderice los productos y tener las opciones de editar y eliminar
class AbmView(CreateView,ProductoListView,VentasListView): 
    model = Producto
    form_class = ProductoForm
    success_url = '/abm'

    def get_context_data(self, **kwargs):
        context = super(AbmView, self).get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        context['ventas'] = Venta.objects.all()
        context['title'] = 'ABM'
        return context

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
        return redirect("/abm")

    return render(request,'editar.html',{'form':form, 'producto':producto, 'title':title['editar']})

def eliminar(request,id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('/abm')
    
def acercaDe(request):
    return render(request,
                    "acercade.html",
                    {
                        'title':title['acercade']
                    }
                )

def comprar(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.fecha = datetime.utcnow()
            venta.producto = producto
            venta.cantidad = request.POST.get('cantidad')
            venta.cliente = form.cleaned_data['cliente']
            venta.precioTotal = producto.precio * int(request.POST.get('cantidad'))
            venta.save()
            
            if producto.stock > int(request.POST.get('cantidad')):
                producto.stock -= int(request.POST.get('cantidad'))
            else:
                producto.stock = 0

            producto.save()

            return redirect('productos')
    else:
        form = VentaForm()

    context = {
        'producto': producto,
        'form': form,
        'title':'Compra - DecorArte'
    }
    return render(request, 'abm/pagina_venta.html', context)