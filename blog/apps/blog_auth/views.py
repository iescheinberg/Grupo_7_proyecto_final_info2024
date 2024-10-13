from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import RegistrarseForm

class RegistrarseView(FormView):
    template_name = 'users/registro.html'
    form_class = RegistrarseForm
    success_url = reverse_lazy('index')

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)
    
class LoguearseView(LoginView):
    template_name = 'users/sesion.html'

# Create your views here.
