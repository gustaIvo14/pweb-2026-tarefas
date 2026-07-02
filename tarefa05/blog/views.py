from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "index.html")

def post(request, id_post):
    context = {}
    return render (request, "blog/post.html")