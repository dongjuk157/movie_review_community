from django.http import response
from accounts.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from movies.serializers import MovieSerializer
from .serializers import CommentSerializer, ReviewSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from movies.models import Movie
from .models import Comment, Review
# Create your views here.

#전체 리뷰 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list(request):
    reviews = Review.objects.all()
    serializers = ReviewSerializer(reviews, many=True)
    return Response(serializers.data, status=status.HTTP_201_CREATED)

#단일 리뷰 조회 및 생성
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail_create(request, movie_id):
    # movie = get_object_or_404(Movie, movie_id=movie_id)
    movie = Movie.objects.get(movie_id=movie_id)
    if request.method == "GET":
        reviews = movie.review_set.all()
        serializers = ReviewSerializer(reviews, many=True)
        return Response(serializers.data)
    
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            review = serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id)
    movie = Movie.objects.get(movie_id=movie_id)
    author = User.objects.get(pk=review.user_id)
    if author != request.user:
        return Response({'data':'글쓴이가 다릅니다'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data)

    elif request.method == "DELETE":
        review.delete()
        return Response({ 'id': review_id })
    

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "GET":
        comments = review.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, review_id, comment_id):
    review = get_object_or_404(Review, pk=review_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    author = User.objects.get(pk=comment.user_id)
    if author != request.user:
        return Response({'data':'글쓴이가 다릅니다'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_id })
