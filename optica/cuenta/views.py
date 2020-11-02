from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import FormularioCreacion, FormularioPerfil,FormIniciarSesion
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Vistas.
def home(request):
    context = {
        'title':'Óptica Marfull'
    }
    return render(request, 'cuenta\home.html', context)



def mostarFormularioRegistro(request):
    formulario1 = FormularioCreacion()
    formulario2 = FormularioPerfil()
    context = {
        'formulario1':formulario1,
        'formulario2':formulario2
    }
    return render(
        request,
        'registrar.html',
        context
    )
def registroUsuario(request):
    if request.method == 'POST':
        formulario1 = FormularioCreacion(request.POST)
        formulario2 = FormularioPerfil(request.POST)
        if formulario1.is_valid() and formulario2.is_valid():
            usuarioGuardado = formulario1.save()
            perfilGuardado = formulario2.save(commit=False)
            perfilGuardado.usuario = usuarioGuardado
            perfilGuardado.save()
            messages.add_message(request,
                messages.SUCCESS,
                'Usuario registrado con éxito :D'
            )
            return redirect('/inicio/')
        context = {
        'formulario1':formulario1,
        'formulario2':formulario2
        }
        return render(
            request,
            'registrar.html',
            context
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'No puedes estar aquí'
        )
        return redirect('/registro/')