from django.urls import path
from motorartigos.views import index, artigo, explicar_ia

urlpatterns = [
    path('', index, name='index'), 
    path('artigo/', artigo, name='artigo'),
    
    # Rota dinâmica para capturar o nome de cada
    path('ia/<str:nome_ia>/', explicar_ia, name='explicar_ia'),
]