from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Article
from .forms import ArticleForm

@login_required(login_url='blog_account:login')
def homepage(request):
    username = request.user.username
    context = {'username': username}
    return render(request, 'learning/homepage.html', context)

@login_required(login_url='blog_account:login')
def articles(request):
    articles = Article.objects.filter(owner=request.user).order_by('date_added')
    context = {'articles': articles}
    return render(request, 'learning/articles.html', context)

@login_required(login_url='blog_account:login')
def article(request, article_id):
    article = Article.objects.get(id=article_id)
    # 确认请求的主题属于当前用户
    if article.owner != request.user:
        raise Http404

    context = {'article': article}
    return render(request, 'learning/article.html', context)

@login_required(login_url='blog_account:login')
def new_article(request):
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blog_content:articles')
        
    context = {'form': form}
    return render(request, 'learning/new_article.html', context)

@login_required(login_url='blog_account:login')
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_content:article', article_id=article.id)
        
    context = {'article': article, 'form': form}
    return render(request, 'learning/edit_article.html', context)

@login_required(login_url='blog_account:login')
def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if article.owner != request.user:
        raise Http404
    
    if request.method == 'POST':
        article.delete()
        return redirect('blog_content:articles')
    
    context = {'article': article}
    return render(request, 'learning/articles.html', context)