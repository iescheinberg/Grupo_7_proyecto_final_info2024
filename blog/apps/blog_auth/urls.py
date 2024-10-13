from django.urls import path
from .views import RegistrarseView, LoguearseView
from django.contrib.auth.views import LogoutView

app_name = 'apps.blog_auth'

urlpatterns = [
    path('registro/', RegistrarseView.as_view(), name = 'registro'),
    path('sesion/', LoguearseView.as_view(), name = 'sesion'),
    path('cerrar_sesion/', LogoutView.as_view(), name = 'cerrar_sesion')
]