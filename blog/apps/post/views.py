from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Articulo

# Create your views here.
class AgregarArticulo(CreateView):
    model = Articulo
    template_name = 'articulos/agregar_articulo.html'
    fields = ['titulo','subtitulo','texto','categoria','imagen']
    success_url = reverse_lazy('index')
    