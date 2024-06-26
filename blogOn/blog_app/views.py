from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)

# Create your views here.


class AboutView(TemplateView):
    """
    Handles about page
    """
    template_name = 'about.html'

