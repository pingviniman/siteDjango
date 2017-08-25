from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.
class PostsView(ListView):
    model = Post

class PostsDetailView(DetailView):
    model = Post