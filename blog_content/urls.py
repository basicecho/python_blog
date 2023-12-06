from django.urls import path

from . import views

app_name = 'blog_content'
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('new_article/', views.new_article, name='new_article'),
    path('edit_article<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete_article<int:article_id>/', views.delete_article, name='delete_article')
]