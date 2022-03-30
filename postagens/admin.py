from django.contrib import admin
from .models import Post

@admin.register(Post)
class ListandoPosts(admin.ModelAdmin):
    # Informa colunas personalizadas
    list_display = ("postagem_titulo", "postagem_texto", "data_postagem", "author", "data_atualizacao")
    search_fields = ('postagem_titulo',)

# Pode informar esse comando para poder exibir as colunas informadas acima, caso não configurar @admin.register(Post)
# admin.site.register(Post, ListandoPosts)


