from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    genre_ids = models.CharField(max_length=50)
    movie_id = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    def __str__(self):
        return self.title    
