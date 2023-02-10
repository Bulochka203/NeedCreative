from django.shortcuts import render, redirect, reverse, HttpResponse
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from dance.settings import *
from django.contrib.auth.mixins import LoginRequiredMixin
from calendarapp.models import Event
from django.views.generic import DetailView, ListView
from .models import *


def redirect_view(request):
    # переход на домшнюю страницу
    return redirect("account/signin")


def statistic(request):
    return render(request, 'danceschool/statistic.html')


def achievements(request):
    return render(request, 'danceschool/achievements.html')


def mobile(request):
    return render(request, 'danceschool/mobile.html')


def messenger(request):
    return render(request, 'danceschool/mobile_messenger.html')


def home(request):
    return render(request, 'danceschool/index.html')


def about(request):
    return render(request, 'danceschool/about.html')


class DashboardView(LoginRequiredMixin, View):
    login_url = LOGIN_URL
    template_name = "calendarapp/dashboard.html"

    def get(self, request, id, **kwargs):
        events = Event.objects.get_all_events(user=request.user)
        running_events = Event.objects.get_running_events(user=request.user)
        latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
        context = {
            "total_event": events.count(),
            "running_events": running_events,
            "latest_events": latest_events,
        }
        return render(request, self.template_name, context)


class profile(LoginRequiredMixin, View):
    login_url = LOGIN_URL
    template_name = "danceschool/profile.html"

    def get(self, request, id, *args, **kwargs):
        data = Profile.objects.get(id=id)
        achievement = Achievements.objects.all()
        context = {
            "data": data,
            "achievement": achievement
        }
        return render(request, self.template_name, context)


class profile_staff(LoginRequiredMixin, View):
    login_url = LOGIN_URL
    template_name = "danceschool/profile_staff.html"

    def get(self, request, id, *args, **kwargs):
        data = Profile.objects.get(id=id)
        spisok = Profile.objects.all()
        commands = Commands.objects.all()
        context = {
            "data": data,
            "spisok": spisok,
            "commands": commands,
        }
        return render(request, self.template_name, context)


def command_detail(request, id):
    data = Commands.objects.get(id=id)
    members = data.get_users
    context = {
        "data": data,
        "members": members
    }
    return render(request, "danceschool/command_detail.html", context)


@csrf_exempt
def IncreaseCounter(request, value):
    _reponse = Profile.object.balance.update(total=F('total') + int(value))
    return HttpResponse('the counter has been increased')
