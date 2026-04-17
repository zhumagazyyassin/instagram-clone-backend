from django.urls import path
from .views import PostListCreateView  # ОСЫ ЖЕРДЕГІ АТ ПЕН VIEWS-ТАҒЫ АТ БІРДЕЙ БОЛУЫ КЕРЕК

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
]