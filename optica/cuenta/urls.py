from django.urls import path
from .views import home, mostarFormularioRegistro,registroUsuario,iniciarSesion

urlpatterns = [
    path('', home, name='home'),
    path('registro/',mostarFormularioRegistro,name='Registrar'),
    path('crearUsuario/',registroUsuario, name="crear"),
    path('iniciarSesion/',iniciarSesion, name="iniciar")
]
