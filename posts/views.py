from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class PostListCreateView(generics.ListCreateAPIView):
    # Посттарды жаңадан ескіге қарай сұрыптау
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Егер қолданушы жүйеге кірсе, соның атына жазамыз
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            # Егер кірмесе (тест кезінде), базадағы бірінші юзерге (админге) тіркейміз
            admin_user = User.objects.first()
            serializer.save(author=admin_user)