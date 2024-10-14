from django.urls import path
from .views import AgregarArticulo

app_name = 'apps.post'

urlpatterns = [
    path('Articulo/', AgregarArticulo.as_view(), name = 'agregar_articulo'),
]