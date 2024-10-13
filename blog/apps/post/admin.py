from django.contrib import admin
from .models import Categoria, Articulo

# Register your models here.

@admin.register(Articulo)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'subtitulo',
        'fecha','texto',
        'activo',
        'categoria',
        'imagen',
        'publicado'
        )
    
admin.site.register(Categoria)