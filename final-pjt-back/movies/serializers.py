from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('genre_ids', 'movie_id', 'overview', 'poster_path', 'release_date', 'title', 'vote_average', )
        # fields = '__all__'