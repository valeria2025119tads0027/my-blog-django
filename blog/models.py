from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):        #método para implementar um gerenciador que nos permitirá recuperar posts 
    def get_queryset(self):
        return(
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.TextChoices):         #Campo "Status" add para gereciar o status do post do blog como "Rascunho" ou "Publicado"
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
        )
    author = models.ForeignKey(               #Criado um relacionamento entre usuários e posts que indicará qual usuário escreveu quais posts.
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,             #Usando CASCADE quando o usuário referenciado for deletado, o banco de dados também vai deletar todos os posts relacionados. 
        related_name='blog_posts'             #Usamos related_name p/ especificar o nome do relacionamento reverso, de User para Post.  
    )

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']                  #Usamos o atributo ordering para dizer ao Django que ele deve ordenar os resultados pelo campo publish. Essa ordenação será aplicada por padrão nas consultas ao banco de dados quando nenhuma ordem específica for fornecida na consulta. 
        indexes = [
            models.Index(fields=['-publish']),   #Isso vai melhorar o desempenho ao filtrar consultas ou ordenar resultados por esse campo
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(                           #A função reverse() vai construir a URL de forma dinâmica usando o nome da URL definido nos padrões de URL.
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )
    
    tags = TaggableManager()

class Comment(models.Model):
    post = models.ForeignKey(
      Post, on_delete=models.CASCADE, related_name='comments'
  )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
        models.Index(fields=['created']),
    ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'