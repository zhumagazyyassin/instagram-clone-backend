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
    # Суреттің URL-ын алу үшін арнайы өріс (тексеру үшін)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'image_url', 'caption', 'created_at']

    def get_image_url(self, obj):
        if obj.image:
            # request арқылы суреттің толық сілтемесін (http://.../media/...) аламыз
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None