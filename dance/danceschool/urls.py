from django.urls import path, include, re_path
from .views import *


app_name = 'danceschool'
urlpatterns = [
    path('', redirect_view),
    path('profile/<int:id>', profile.as_view(), name='profile'),
    path('sprofile/<int:id>', profile_staff.as_view(), name='staff_profile'),
    path('commands/<int:id>/', command_detail, name='commands'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('mobile/achievements/', achievements, name='achievement'),
    path('mobile/profile/<int:id>', profile.as_view(), name='profile_mobile'),
    re_path(r'^mobile/messenger/$', messenger, name='messenger_mobile'),
    re_path(r'^mobile/statistic/$', statistic, name='statistic'),
]
