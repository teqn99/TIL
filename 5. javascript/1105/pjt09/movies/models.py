from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()   
    vote_count = models.IntegerField() # 평점수
    vote_average = models.FloatField() # 평점 평균 (rank)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)  

    def __str__(self):
        return f'{self.overview[:50]}...'
