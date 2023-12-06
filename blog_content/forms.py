from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'content']
        labels = {'title': 'title', 
                  'description': 'description', 
                  'content': 'content',
                  }