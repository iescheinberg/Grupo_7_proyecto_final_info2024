from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Articulo

# Create your views here.
class AgregarArticulo(CreateView):
    model = Articulo
    template_name = 'articulos/agregar_articulo.html'
    fields = ['titulo','subtitulo','texto','categoria','imagen']
    success_url = reverse_lazy('index')

class ActualizarArticulo(UpdateView):
    model = Articulo
    template_name = 'articulos/actualizar_articulo.html'
    fields = ['titulo','subtitulo','texto','categoria','imagen']
    success_url = reverse_lazy('index')

class EliminarArticulo(DeleteView):
    model = Articulo
    template_name = 'articulos/Eliminar_articulo.html'
    success_url = reverse_lazy('index')

class ListarArticulos(ListView):
    model = Articulo
    template_name = 'articulos/listar_articulos.html'
    context_object_name = 'articulos'
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        articulos = Articulo.objects.all()
        context['articulos'] = articulos
        return context
    