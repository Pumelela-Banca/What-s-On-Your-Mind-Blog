from django.shortcuts import (render, 
                              get_object_or_404, redirect)
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


class AboutView(TemplateView):
    """
    Handles about page
    """
    template_name = 'blog_app/about.html'


class PostListView(ListView):
    """
    Handles post list view
    """
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()).order_by(
                '-published_date')


class RegisterView(TemplateView):
    """
    Handles register page
    """
    template_name = 'registration/registration.html'

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


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class for updating post
    """

    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class for deleting a post
    """
    model = Post
    success_url = reverse_lazy('post_list')


class PostDraftListView(LoginRequiredMixin, ListView):
    """
    Class for listing drafts
    """
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_list.html'
    
    model = Post

    def get_queryset(self):
        return Post.objects.filter(
            published_date__isnull=True).order_by('created_date')


####################################
####################################


@login_required
def add_comment_to_post(request, pk):
    """
    connects comment to post 
    """

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 
                  'blog_app/comment_form.html', 
                  {'form': form})


@login_required
def comment_approve(request, pk):
    """
    Approve comment
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    """
    Remove comment
    """
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

@login_required
def post_publish(request, pk):
    """
    Publish post
    """
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
