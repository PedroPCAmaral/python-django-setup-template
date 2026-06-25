from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Artigo  # Importa o modelo Artigo do seu banco

TECNOLOGIAS_PERMITIDAS = ['chatgpt', 'claude', 'gemini', 'groq', 'maritaca', 'mysql']

def index(request):
    # Puxa os artigos do banco otimizando a busca dos relacionamentos (autor e eixo)
    artigos_resultado = Artigo.objects.select_related('id_fk_autor', 'id_fk_eixo').all()
    busca = request.GET.get('busca')

    if busca:
        # Filtra na tabela pelo texto do artigo
        artigos_resultado = artigos_resultado.filter(texto__icontains=busca)

    # Coleta os autores únicos que possuem artigos direto pelo relacionamento do banco
    autores_banco = [artigo.id_fk_autor for artigo in artigos_resultado if artigo.id_fk_autor]
    # Remove duplicados mantendo a ordem
    autores_unicos = list(dict.fromkeys(autores_banco))

    contexto = {
        "autores": autores_unicos,
        "artigos": artigos_resultado
    }
    return render(request, 'motorartigos/index.html', contexto)

def detalhe_artigo(request, id):
    artigo_encontrado = get_object_or_404(Artigo.objects.select_related('id_fk_autor', 'id_fk_eixo'), id=id)
    return render(request, 'motorartigos/artigo.html', {'artigo': artigo_encontrado})

def explicar_ia(request, nome_ia):
    nome_ia = nome_ia.lower()
    if nome_ia not in TECNOLOGIAS_PERMITIDAS:
        raise Http404("Página de explicação não encontrada.")
    return render(request, f'motorartigos/ias/{nome_ia}.html', {'nome_ia': nome_ia})