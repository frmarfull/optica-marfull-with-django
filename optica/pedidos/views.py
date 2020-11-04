from django.shortcuts import render
from .forms import FormPedido
from .models import Pedido
from django.contrib.auth.decorators import login_required
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



