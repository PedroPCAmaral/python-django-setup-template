from django.contrib import admin
from django.urls import path, include
# Importações necessárias para corrigir o visual dos arquivos estáticos
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

# CORREÇÃO DA CAIXA BRANCA: Força o Django a carregar os arquivos CSS/JS no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)