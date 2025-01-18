from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # references tuple on ln. 4 blog/models.py 
    template_name = "blog/index.html"
    paginate_by = 6