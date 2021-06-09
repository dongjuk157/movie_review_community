from rest_framework import serializers
from .models import Review
from .models import Comment
from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields=('id','movie','title', 'content','user','score','created_at','updated_at', 'username')
        read_only_fields = ('movie','user')

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields=('id','review', 'content','user','created_at','updated_at','username')
        read_only_fields = ('review','user')
