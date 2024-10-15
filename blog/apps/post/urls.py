from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import AgregarArticulo, ActualizarArticulo, EliminarArticulo, ListarArticulo

app_name = 'apps.post'

urlpatterns = [
    path('agregar_articulo/', AgregarArticulo.as_view(), name = 'agregar_articulo'),
    path('actualizar_articulo/', ActualizarArticulo.as_view(), name = 'actualizar_articulo'),
    path('eliminar_articulo/', EliminarArticulo.as_view(), name = 'eliminar_articulo'),
    path('listar_articulo/', ListarArticulo.as_view(), name = 'listar_articulo'),
]