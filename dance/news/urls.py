from django.urls import path, re_path
from .views import *

app_name = 'news'
urlpatterns = [
    path('', News.as_view(), name="news"),
    path('post/<int:id>', NewsDetail.as_view(), name="post"),
    path('mobile', News.as_view(), name='news_mobile'),
]
