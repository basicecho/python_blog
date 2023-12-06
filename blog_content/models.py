from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    