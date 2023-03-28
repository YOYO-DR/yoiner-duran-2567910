from django.forms import ModelForm
from .models import *

class AutoForm(ModelForm):
  class Meta:
    model = Auto
    fields = '__all__'

class ClienteForm(ModelForm):
  class Meta:
    model = Clientes
    fields = '__all__'