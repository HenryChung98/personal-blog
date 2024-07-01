from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.postList, name='post-list'),
    path('posts/<int:postId>/', views.postDetail, name='post-detail'),
]