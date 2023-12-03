from django.urls import path

from . import views
from .views import abmView, ProductoListView, CrearClienteView

urlpatterns = [
    path("", views.index, name = "index"),
    path("abm/", abmView.as_view(), name = "abm"),
    path("editar/<uuid:id>", views.editar, name = "editar"),
    path("eliminar/<uuid:id>", views.eliminar, name = "eliminar"),
    path("comprar/<uuid:id>", views.comprar, name = "comprar"),
    path("productos/", ProductoListView.as_view(), name = "productos"),
    path("acercade/", views.acercaDe, name = "acercaDe"),
    path("contacto/", CrearClienteView.as_view(), name = "contacto"),
] 
