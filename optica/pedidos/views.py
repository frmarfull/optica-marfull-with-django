from django.shortcuts import render,redirect
from .forms import FormPedido
from .models import Pedido
from django.contrib.auth.decorators import login_required
from producto.models import Producto
from django.contrib import messages
# Create your views here.

@login_required(login_url='iniciarSesion')
def listarPedidos(request):
    pedidos= Pedido.objects.all
    context = {
        'titulo':'Listar pedidos',
        'pedidos':pedidos
    }
    
    return render(
        request,
        'consultar.html',
        context
    )
@login_required(login_url='iniciarSesion')
def agregarPedidos(request,id_producto):
    pass
                
            



