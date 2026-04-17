from django.urls import path
from .views import PostListCreateView

urlpatterns = [
    # Барлық посттарды алу және жаңа пост салу: /api/posts/
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    
    # Болашақта әр постты жеке көру үшін (мысалы: /api/posts/5/)
    # path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]