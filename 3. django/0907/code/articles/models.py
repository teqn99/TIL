from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)  # max_length는 필수
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)