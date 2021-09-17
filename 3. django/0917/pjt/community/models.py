from django.db import models

# Create your models here.
class Community(models.Model):
    movie_title = models.TextField()
    title = models.TextField()
    rank = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title
    