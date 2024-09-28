from django.shortcuts import render, redirect
from .models import Post
from datetime import date
from .forms import PostForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.core.paginator import Paginator

def index(request):
    return redirect('post-list')


class PostListView(ListView):
    model = Post
    ordering = ['-modifiedAt']
    paginate_by = 10
    # template_name = 'posts/post_list.html' 
    # context_object_name = 'posts'
    # page_kwarg = 'page' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context


class PostDetailView(DetailView):
    model = Post
    # pk_url_kwarg = 'pk'
    # template_name = 'posts/post_detail.html'
    # context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    # pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})
    

class PostDeleteView(DeleteView):
    model = Post
    # context_object_name = 'post'
    # template_name = 'posts/post_confirm_delete.html'
    # pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('post-list')