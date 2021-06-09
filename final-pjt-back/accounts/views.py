from movies.serializers import MovieSerializer
from review.serializers import CommentSerializer
from movies.views import like_movie
from review.serializers import ReviewSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from accounts import serializers
# Create your views here.
@api_view(['POST'])
def signup(request):
    # 0. vue를 통해서 form이 전달 -> 서버에서 할거 없음
    # 1. account DB에 유저가 있는지 확인? -> 알아서 걸러짐
    # 2. 패스워드, 확인 체크 (유효성 검사?)
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'password': '비밀번호가 일치하지 않습니다.'},status=status.HTTP_400_BAD_REQUEST)
        # 409_conflict
    
    # 3. serializer 생성
    serializer = UserSerializer(data=request.data)
    # 4. 유효성검사가 넘어가면 회원가입 성공 (save())
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    reviews = user.review_set.all()
    reviewSerializer = ReviewSerializer(reviews, many=True)
    like_movies = user.like_movies.all()
    movieSerializer = MovieSerializer(like_movies, many=True)
    comments = user.comment_set.all()
    commentSerializer = CommentSerializer(comments,many=True)
    # serializer.data를 더해서 한꺼번에 response하면 될듯
    return Response({
        'reviews': reviewSerializer.data,
        'like_movies': movieSerializer.data,
        'comments': commentSerializer.data,
    })
