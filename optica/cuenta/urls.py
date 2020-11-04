from django.urls import path
#from .views import home, mostarFormularioRegistro,registroUsuario,iniciarSesion,agregar
from .views import * 
urlpatterns = [
    path('', home, name='home'),                        
    path('registro/',mostarFormularioRegistro,name='Registrar'),
    path('crearUsuario/',registroUsuario, name="crear"),
    path('iniciarSesion/',iniciarSesion, name="iniciar"),

    path('agregar/',agregar,name='agregar'),
    path('cancelar/',cancelar, name="cancelar"),
    path('catalogo/',catalogo,name='catalogo'),             
    path('consultar/',consultar, name="consultar"),    
    path('listar_producto/',listar_producto,name='listar_producto'),
    path('modificar_producto/',modificar_producto, name="modificar_producto"),
    path('solicitar/',solicitar, name="solicitar"),
    #path('/',, name=""), ejemplo #
   
    

]
