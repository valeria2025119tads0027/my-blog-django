from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name = 'blog'                                             #define um namespace de aplicação com a variável app_name. Isso permite que você organize URLs por aplicação e use o nome ao se referir a elas.

urlpatterns = [
    path('', views.post_list, name='post_list'),              #dois padrões diferentes são definidos usando a função path(). O primeiro padrão de URL não recebe nenhum argumento e é mapeado para a view post_list.
    path(
            'tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'
        ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'
        ),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path(
        '<int:post_id>/comment/', views.post_comment, name='post_comment'
    ),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]