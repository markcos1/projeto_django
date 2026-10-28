from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView): 
    model = Post
    template_name = 'portfolio/post_list.html'
    context_object_name = 'posts'

class PostDetail(DetailView): 
    model = Post
    template_name = 'portfolio/post_detail.html'
    context_object_name = 'post'    