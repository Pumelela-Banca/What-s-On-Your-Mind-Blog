from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)
from .models import Post
from django.utils import timezone


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
    