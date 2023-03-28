from django.urls import path
from .views import *
urlpatterns = [
    path('',principal,name='principal'),
    path('autos/',autos,name='autos'),
    path('clientes/',clientes,name='clientes'),
    path('ingresarautos/',ingresarAutos,name='ingresarautos'),
    path('ingresarclientes/',ingresarClientes,name='ingresarclientes'),
    path('eliminarautos/<int:id>/',eliminarAutos,name='eliminarautos'),
    path('eliminarclientes/<int:id>/',eliminarClientes,name='eliminarclientes'),
]
