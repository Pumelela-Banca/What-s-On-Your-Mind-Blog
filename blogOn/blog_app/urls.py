"""
URL configuration for blogOn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog_app.views import (AboutView, PostListView, 
                            PostDetailView, PostCreateView,
                            PostUpdateView, PostDeleteView,
                            PostDraftListView, RegisterView,
                            add_comment_to_post,
                            comment_approve, comment_remove,
                            post_publish)


urlpatterns = [
    path('', PostListView.as_view(), 
         name='post_list'),
    path('about/', AboutView.as_view(), 
         name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), 
         name='post_detail'),
     path('register/', RegisterView.as_view(),
           name='register'),
    path('post/new/', PostCreateView.as_view(), 
         name='post_new'),
    path('post/<int:pk>/edit/', 
         PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', 
         PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', PostDraftListView.as_view(),
          name='post_draft_list'),
    path('post/<int:pk>/comment', add_comment_to_post, 
          name='add_comment_to_post'),
    path('comment/<int:comment_pk>/approve/',
         comment_approve,
         name='comment_approve'),
    path('comment/<int:comment_pk>/remove/',
          comment_remove,
          name='comment_remove'),
    path('post/<int:pk>/publish/',
          post_publish,
          name='post_publish'),
]
