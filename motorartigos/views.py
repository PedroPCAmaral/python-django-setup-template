from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Dicionário de autores exatamente como o professor pediu no slide
    autores = {
        1: {
            'nome': 'André Rogler',
            'biografia': 'estudante do SENAI de BD',
            'email': 'roglem@nasa.gov.br'
        },
        2: {
            'nome': 'Luiz Fernando',
            'biografia': 'Desenvolvedor Django ',
            'email': 'fernando@gmail.com'
        },
        3: {
            'nome': 'Victor Jonh',
            'biografia': 'Desenvolvedor SQL ',
            'email': 'victor@gmail.com'
        }
    }
    
    
    return render(request, 'motorartigos/index.html', {"autores": autores})

def artigo(request):
    return render(request, 'motorartigos/artigo.html')

def explicar_ia(request, nome_ia):
    nome_ia = nome_ia.lower()
    return render(request, f'motorartigos/ias/{nome_ia}.html')