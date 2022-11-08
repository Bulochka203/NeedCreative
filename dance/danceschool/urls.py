from django.urls import path, re_path
from .views import *


app_name = 'danceschool'
urlpatterns = [
    path('', redirect_view),
    path('profile/<int:id>', profile.as_view(), name='profile'),
    path('sprofile/<int:id>', profile_staff.as_view(), name='staff_profile'),
    path('commands/<int:id>/', command_detail, name='commands'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('mobile/', mobile, name='mobile'),
    path('mobile/achievements/', achievements, name='achievement'),
    path('mobile/profile/<int:id>', profile.as_view(), name='profile_mobile'),
    path('sprofile/', profile_staff.as_view(), name='sprofile_mobile'),
    re_path(r'^mobile/news/$', news, name='news_mobile'),
    re_path(r'^mobile/messenger/$', messenger, name='messenger_mobile'),
    re_path(r'^mobile/statistic/$', statistic, name='statistic'),
]
