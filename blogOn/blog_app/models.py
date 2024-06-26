from django.db import models
from django.utils import timezone
from django.urls import reverse
from typing import Any

# Create your models here.


class Post(models.Model):
    """
    This will cobtrol the post model.
    """

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=200, default='General')

    def publish(self) -> None:
        """
        This will publish the post.
        """
        self.published_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        """
        This will approve comments.
        """
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self) -> Any:
        """
        This will return the absolute url.
        """
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    Comments are controlled here.
    """
    post = models.ForeignKey('blog_app.Post', 
                             related_name='comments', 
                             on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    
    def approve(self) -> None:
        """
        This will approve the comment.
        """
        self.approved_comment = True
        self.save()

    def get_absolute_url(self) -> Any:
        """
        This will return the absolute url.
        """
        return reverse('post_list')

    def __str__(self) -> str:
        return self.text
