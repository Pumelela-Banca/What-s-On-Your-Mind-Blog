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
                            PostDraftListView)


urlpatterns = [
    path('', PostListView.as_view(), 
         name='post_list'),
    path('about/', AboutView.as_view(), 
         name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), 
         name='post_detail'),
    path('post/new/', PostCreateView.as_view(), 
         name='post_new'),
    path('post/<int:pk>/edit/', 
         PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', 
         PostDeleteView.as_view(), name='post_delete'),
    path('drafts/', PostDraftListView.as_view(),
            name='post_draft_list'),
]
