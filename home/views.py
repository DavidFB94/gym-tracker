from django.shortcuts import render
from django.views import generic
from .models import Workout

# Create your views here.
class WorkoutList(generic.ListView):
    queryset = Workout.objects.all()
    template_name = "home.html"