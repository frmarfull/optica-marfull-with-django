from django.urls import path

from .views import agregarProducto

urlpatterns = [
    path('agregar/',agregarProducto,name='AgregarProducto')
]