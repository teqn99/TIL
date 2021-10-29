from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    
    def __str__(self):
        return f'{self.pk}: {self.title}'


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField(default=0)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')  # N쪽에서 외래키 선언

    def __str__(self):
        return f'{self.pk}: {self.title}'