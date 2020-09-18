from django.shortcuts import render
from django.urls import reverse_lazy 
from ..forms import *
from ..models import *
from django.views import generic
# Create your views here.

class Register(generic.CreateView):
    form_class = CustomUsuarioCreateForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('index')