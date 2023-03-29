from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
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

def ingresarAutos(request):
  if request.method == 'GET':
    context= {
      'titulo':'Ingresar Autos',
      'form':AutoForm
    }
    return render(request,'ingresarautos.html',context)
  else:
    form = AutoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('autos')

def ingresarClientes(request):
  if request.method == 'GET':
    context= {
      'titulo':'Ingresar Clientes',
      'form':ClienteForm
    }
    return render(request,'ingresarclientes.html',context)
  else:
    form = ClienteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('clientes')

def eliminarAutos(request,id):
  auto=get_object_or_404(Auto,pk=id)
  auto.delete()
  return redirect('autos')
def eliminarClientes(request,id):
  cliente=get_object_or_404(Clientes,pk=id)
  cliente.delete()
  return redirect('clientes')

def actualizarAuto(request,id):
  auto = get_object_or_404(Auto,pk=id)
  if request.method == 'GET':
    form = AutoForm(instance=auto)
    context = {
      'titulo':'Actualizar auto',
      'auto':auto,
      'form':form
    }
    return render(request,'actualizarautos.html',context)
  if request.method == 'POST':
    form = AutoForm(request.POST,instance=auto)
    if form.is_valid():
      form.save()
      return redirect('autos')

def actualizarCliente(request,id):
  cliente = get_object_or_404(Clientes,pk=id)
  if request.method == 'GET':
    form = ClienteForm(instance=cliente)
    context = {
      'titulo':'Actualizar cliente',
      'cliente':cliente,
      'form':form
    }
    return render(request,'actualizarclientes.html',context)
  if request.method == 'POST':
    form = ClienteForm(request.POST,instance=cliente)
    if form.is_valid():
      form.save()
      return redirect('clientes')