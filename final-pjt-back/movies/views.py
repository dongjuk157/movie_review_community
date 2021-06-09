from django.shortcuts import render
from rest_framework import serializers
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from accounts.models import User

# Create your views here.
@api_view(['GET'])
def main(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    if request.method == 'GET':
        if movie.like_users.filter(pk=request.user.id).exists():
            return Response({'like': True })
        else:
            return Response({'like': False })
    elif request.method == 'POST':
        if movie.like_users.filter(pk=request.user.id).exists():
            movie.like_users.remove(request.user)
            return Response({'like': False })
        else:
            movie.like_users.add(request.user)
            return Response({'like': True }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def recommend_vote(request):
    movies = Movie.objects.order_by('-vote_average')[:10]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_personal(request):
    user = request.user
    reviews = user.review_set.all()
    review_movies = set()
    movie_genres = dict()
    for review in reviews:
        movie = Movie.objects.get(pk=review.movie_id)
        review_movies.add(movie.title)
        genres=movie.genre_ids
        for genre in genres.split(','):
            if genre:
                if movie_genres.get(genre):
                    movie_genres[genre] += 1
                else:
                    movie_genres[genre] = 1
                    
    movie_genres = sorted(movie_genres,reverse=True, key=lambda item: item[1])
    if movie_genres:
        selectMovies=[]
        selectMovies_org = Movie.objects.filter(genre_ids__contains=movie_genres[0])
        for movie in selectMovies_org:
            if movie.title not in review_movies:
                selectMovies.append(movie)
        serializer = MovieSerializer(selectMovies[:10],many=True)
    else:
        random_movies = Movie.objects.order_by('?')[:10]
        serializer = MovieSerializer(random_movies, many=True)
    return Response(serializer.data)