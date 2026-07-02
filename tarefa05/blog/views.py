from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "index.html")

def post(request, id_post):
    context = {
        "post": Post.objects.get(id=id_post),
        "post": get_object_or_404(Post, id=id_post)
    }
    return render (request, "blog/post.html")