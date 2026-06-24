from django.contrib import admin
from .models import Autor, EixoTecnologico, Artigo

class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')
    
    # Injeta o script direto da nuvem e força a ativação do editor rico na Biografia
    class Media:
        js = (
            'https://cdn.jsdelivr.net/npm/tinymce@6/tinymce.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/django-tinymce/3.5.0/init_tinymce.min.js',
        )

class EixoTecnologicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_fk_autor', 'id_fk_eixo', 'data_publicacao')
    search_fields = ('id_fk_autor__nome', 'id_fk_eixo__nome')
    list_filter = ('id_fk_eixo', 'data_publicacao')
    
    # LUPA INTERATIVA: Ativa a busca inteligente por ID
    raw_id_fields = ('id_fk_autor', 'id_fk_eixo')
    
    # Injeta o script direto da nuvem e força a ativação do editor rico no Texto
    class Media:
        js = (
            'https://cdn.jsdelivr.net/npm/tinymce@6/tinymce.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/django-tinymce/3.5.0/init_tinymce.min.js',
        )

# Registro dos models no Django Admin
admin.site.register(Autor, AutorAdmin)
admin.site.register(EixoTecnologico, EixoTecnologicoAdmin)
admin.site.register(Artigo, ArtigoAdmin)