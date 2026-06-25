from django.urls import path
from . import views

urlpatterns = [
    # Página inicial (index)
    path('', views.index, name='index'),
    
    # Página de leitura de cada artigo usando o ID dinâmico
    path('artigo/<int:id>/', views.detalhe_artigo, name='detalhe_artigo'),
    
    # Rota dinâmica para as 6 explicações de IA/Banco
    path('ia/<str:nome_ia>/', views.explicar_ia, name='explicar_ia'),
]

