from django.shortcuts import render, redirect
from .models import Post
from datetime import date


def index(request):
    return redirect('post-list')


def postList(request):
    today = date.today() 

    posts = Post.objects.all()
    context = {
                'posts': posts,
                'today': today,
               }
    return render(request, 'posts/postList.html', context)

def postDetail(request, postId):
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'posts/postDetail.html', context)