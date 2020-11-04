from django.shortcuts import render
from .forms import FormPedido
from .models import Pedido
# Create your views here.


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



