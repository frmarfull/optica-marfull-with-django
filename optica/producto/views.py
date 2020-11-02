from django.shortcuts import render, redirect
from .forms import FormProducto
from django.contrib import messages

# Create your views here.

def agregarProducto(request):
    formulario= FormProducto()
    if request.method =='POST':
        formulario = FormProducto(request.POST,request.FILES)
        if formulario.is_valid():
            productoNuevo= formulario.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'producto agregado'
            )
            return redirect('/home/')
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'agregar.html',
        context
    )
