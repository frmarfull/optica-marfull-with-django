from django.urls import path

from .views import * 


urlpatterns=[
    path('pedidos/',listarPedidos, name="pedidos")

]