from django.urls import path, re_path
from .views import *


app_name = 'danceschool'
urlpatterns = [
    path('', redirect_view),
    path('profile/', profile.as_view(), name='profile'),
    path('sprofile/', profile_staff.as_view(), name='staff_profile'),
    path('commands/<int:id>/', command_detail, name='commands'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    re_path(r'^mobile/$', mobile, name='mobile'),
    re_path(r'^mobile/achievements/$', achievements, name='achievement'),
    re_path(r'^mobile/profile/$', profile.as_view(), name='profile_mobile'),
    re_path(r'^sprofile/$', profile_staff.as_view(), name='sprofile_mobile'),
    re_path(r'^mobile/news/$', news, name='news_mobile'),
    re_path(r'^mobile/messenger/$', messenger, name='messenger_mobile'),
    re_path(r'^mobile/statistic/$', statistic, name='statistic'),
]
