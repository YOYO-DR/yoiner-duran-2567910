from django.shortcuts import render
from .models import *

def principal(request):
  context={
    'titulo':'Principal'
  }
  return render(request,'principal.html', context)

def autos(request):
  context = {
    'titulo':'Autos',
    'autos':Auto.objects.all()
  }

  return render(request,'autos.html', context)

def clientes(request):
  context = {
    'titulo':'Clientes',
    'clientes':Clientes.objects.all()
  }
  return render(request,'clientes.html', context)

# def ingresarAutos(request):
#   pass

# def ingresarAutos(request):
#   pass