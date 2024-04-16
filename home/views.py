from django.shortcuts import render
from django.views import generic
from .models import Workout


def home(request):
    if request.user.is_authenticated:
        queryset = Workout.objects.filter(user=request.user)
    else:
        queryset = []
    template = "home/home.html"
    context = {
        "object_list": queryset,
    }
    return render(request, template, context)