from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

# Юзер ақпаратын көрсету үшін
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Пост ақпаратын JSON-ға айналдыру үшін
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'caption', 'created_at']