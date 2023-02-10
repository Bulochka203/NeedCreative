from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from dance.settings import *
from .models import *


def news(request):
    return render(request, 'danceschool/mobile_news.html')


class NewsDetail(LoginRequiredMixin, View):
    login_url = LOGIN_URL
    template_name = 'danceschool/post.html'
    model = Post

    def get(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        context = {
            "data": post
        }
        return render(request, self.template_name, context)


class News(LoginRequiredMixin, View):
    login_url = LOGIN_URL
    template_name = 'danceschool/mobile_news.html'
    model = Post

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            "posts": posts
        }
        return render(request, self.template_name, context)
