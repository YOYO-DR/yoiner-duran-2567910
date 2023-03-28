from django.db import models
from django.db.models.fields import *

class Auto(models.Model):
  marca = CharField(max_length=20,verbose_name='Marca')
  nombre = CharField(max_length=30,verbose_name='Nombre')
  modelo = IntegerField(verbose_name='Modelo')
  color = CharField(max_length=20,verbose_name='Color')
  
  class Meta:
    db_table = 'auto'
  def __str__(self):
    return f'Marca {self.marca} - Nombre {self.nombre}'

class Clientes(models.Model):
  nombre = CharField(max_length=20)
  apellido = CharField(max_length=30)
  direccion = CharField(max_length=200)
  email = EmailField(max_length=100)
  telefono = CharField(max_length=20)
  
  class Meta:
    db_table='cliente'

  def __str__(self):
    return f'Cliente {self.nombre}'
  
# from autos.models import *
# Auto(marca='Chevrolet Onix',nombre='Onix',modelo=2021,color='negro').save()
# Auto(marca='Suzuki Swift',nombre='Swift',modelo=2022,color='blanco').save() 
# Auto(marca='Kia Picanto',nombre='Picanto',modelo=2023,color='verde').save()  
# Auto(marca='Renault Duster',nombre='Duster',modelo=2023,color='rojo').save()   
# Auto(marca='Mazda 2',nombre='Two',modelo=2022,color='blanco').save() 
# Clientes(nombre='yoiner',apellido='duran',direccion='cra 2b #12-53',email='yoiner@gmail.com',telefono='573148743538').save()
# Clientes(nombre='daniel',apellido='rojas',direccion='cra 3b #11-33',email='daniel@gmail.com',telefono='573148747894').save() 
# Clientes(nombre='breynner',apellido='perez',direccion='cra 2b #10-27',email='breynner@gmail.com',telefono='573218747894').save()  
# Clientes(nombre='alejandra',apellido='fajardo',direccion='cra 3b #09-12',email='alejadra@gmail.com',telefono='573214577894').save()  
# Clientes(nombre='frank',apellido='cuetia',direccion='cra 2c #11-67',email='frank@gmail.com',telefono='573218745894').save()