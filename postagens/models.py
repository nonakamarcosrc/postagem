from django.db import models
from django.contrib.auth.models import User

# Campos da classe Post
class Post(models.Model):
    postagem_titulo = models.CharField(max_length=200)
    postagem_texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    data_atualizacao = models.DateTimeField(auto_now=True)

    # Ordernar por ultima Receita criada
    class Meta:
        ordering = ("-data_postagem",)

    # Converter em letra maiúscula do campo postagem_titulo
    def save(self, force_insert=False, force_update=False):
        self.postagem_texto = self.postagem_texto.upper()
        super(Post, self).save(force_insert, force_update)

    # Melhorando visualização da lista de nome do post do admin
    def __str__(self):
        return self.postagem_titulo
