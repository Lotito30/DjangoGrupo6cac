from django.db import models
import uuid
from PIL import Image

class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=55, null=False)
    descripcion = models.CharField(max_length=255, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock = models.IntegerField(null=False)
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=25, null=False)
    apellido = models.CharField(max_length=25, null=False)
    ciudad = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)

    def __str__(self):
        return self.email

class Venta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField(null=False)
    cantidad = models.IntegerField(null=False)
    precioTotal = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente, self.fecha, self.precioTotal
