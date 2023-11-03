from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('editora', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    isbn = models.CharField('ISBN', max_length=200) 
    numeroPaginas = models.IntegerField('Número de páginas') 
    anoObraEscrita = models.IntegerField('Ano da obra escrita')
      

    def __str__(self):
        return self.titulo