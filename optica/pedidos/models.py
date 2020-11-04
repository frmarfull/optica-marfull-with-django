from django.db import models
from cuenta.models import Perfil
from producto.models import Producto
# Create your models here.


class Pedido(models.Model):
    producto= models.ForeignKey(Producto, on_delete=CASCADE)
    perfil= models.ForeignKey(Perfil,on_delete=CASCADE)
    