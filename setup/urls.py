from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota do painel de administração do Django
    path('admin/', admin.site.urls),  
    
    # Rota que inclui as URLs do seu aplicativo motorartigos
    path('', include('motorartigos.urls')), 
    
    # Rota indispensável para o TinyMCE carregar os componentes visuais
    path('tinymce/', include('tinymce.urls')), 
]

# Configuração para carregar arquivos de mídia e estáticos em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)