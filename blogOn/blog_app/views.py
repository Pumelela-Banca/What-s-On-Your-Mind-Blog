from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)
from .models import Post
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class AboutView(TemplateView):
    """
    Handles about page
    """
    template_name = 'about.html'


class PostListView(ListView):
    """
    Handles post list view
    """
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()).order_by(
                '-published_date')


class PostDetailView(DetailView):
    """
    Handles post detail view
    """
    model = Post


class PostCreateView(LoginRequiredMixin ,CreateView):
    """
    Handles creating a new post
    """
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    
    form_class = PostForm
    model = Post


