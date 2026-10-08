from django.contrib import admin
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):                                  #Nessa classe, podemos incluir informações sobre como exibir o modelo no site de administração e como interagir com ele.
    list_display = ['title', 'slug', 'author', 'publish', 'status'] #O atributo list_display permite definir os campos do seu modelo que você quer mostrar na página de lista de objetos da administração.
    list_filter = ['title', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS        #Essas contagens indicam o número de objetos correspondentes a cada filtro específico,
                                                 #facilitando a identificação dos objetos correspondentes na visualização da lista de alterações do admin

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']