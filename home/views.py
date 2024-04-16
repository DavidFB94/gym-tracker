from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Workout
from .models import Exercise
from .forms import WorkoutForm
from .forms import ExerciseForm


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


def add_workout(request):
    workout_form = WorkoutForm(request.POST or None)
    if request.method == "POST":
        if workout_form.is_valid():
            workout_form.instance.user = request.user
            workout_form.save()
            messages.success(request, "Workout Added!")
            return redirect(reverse("home"))
    template = "home/add_workout.html"
    context = {
        "workout_form": workout_form,
    }
    return render(request, template, context)


def add_exercise(request):
    workout_form = WorkoutForm(request.POST or None)
    if request.method == "POST":
        if exercise_form.is_valid():
            exercise_form.instance.user = request.user
            exercise_form.save()
            messages.success(request, "Exercise Added!")
            return redirect(reverse("home"))
    template = "home/add_exercise.html"
    context = {
        "exercise_form": exercise_form,
    }
    return render(request, template, context)