from django.urls import path
from .views import *
urlpatterns = [
    path('',principal,name='principal'),
    path('autos/',autos,name='autos'),
    path('clientes/',clientes,name='clientes')
]
