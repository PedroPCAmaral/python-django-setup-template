from django.db import models
# Importa o TinyMCE para ativar o editor de texto rico
from tinymce.models import HTMLField

class Autor(models.Model):
    nome = models.CharField(max_length=100)
   
    biografia = HTMLField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'autor'


class EixoTecnologico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome 
    
    class Meta:
        db_table = 'eixo'


class Artigo(models.Model):
    id_fk_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='id_fk_autor')
    id_fk_eixo = models.ForeignKey(EixoTecnologico, on_delete=models.CASCADE, db_column='id_fk_eixo')
    
    texto = HTMLField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Artigo {self.id}"
    
    class Meta:
        db_table = 'artigo'