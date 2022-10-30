from django.shortcuts import render
from .models import Post


def homepage(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "homepage.html", context)


def post_view(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    return render(request, "post_view.html", context)
