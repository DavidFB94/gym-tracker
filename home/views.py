from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from django.contrib import messages
from .models import Workout
from .models import Exercise
from .forms import WorkoutForm
from .forms import ExerciseForm


def home(request):
    if request.user.is_authenticated:
        # Display workout list
        queryset = Workout.objects.filter(user=request.user).order_by('-date')
    else:
        queryset = []
    # Paginator setup: 15 items per page
    paginator = Paginator(queryset, 15)  # 15 workouts per page
    page_number = request.GET.get('page')  # get the page number from the query parameters
    page_obj = paginator.get_page(page_number)  # get the requested page
    context = {
        "page_obj": page_obj,  # use 'page_obj' in your template to access the paginated items
    }
    return render(request, "home/home.html", {"page_obj": page_obj})


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


def add_exercise(request, id):
    workout = get_object_or_404(Workout, id=id)
    if workout.user != request.user:
        messages.error(request, "Access denied, this isn't your workout!")
        return redirect(reverse("home"))
    exercise_form = ExerciseForm(request.POST or None)
    if request.method == "POST":
        if exercise_form.is_valid():
            exercise_form.instance.user = request.user
            exercise_form.instance.workout = workout
            exercise_form.save()
            exercise_form = ExerciseForm
            messages.success(request, "Exercise Added!")
            return redirect(reverse("home"))
    template = "home/add_exercise.html"
    context = {
        "workout": workout,
        "exercise_form": exercise_form,
    }
    return render(request, template, context)


def edit_workout(request, id):
    workout = get_object_or_404(Workout, id=id)
    workout_form = WorkoutForm(request.POST or None, instance=workout)
    if request.method == "POST":
        if workout_form.is_valid():
            workout_form.instance.user = request.user
            workout_form.save()
            messages.success(request, "Workout updated!")
            return redirect(reverse("home"))
    template = "home/edit_workout.html"
    context = {
        "workout": workout,
        "workout_form": workout_form,
    }
    return render(request, template, context)


def edit_exercise(request, id):
    exercise = get_object_or_404(Exercise, id=id)
    exercise_form = ExerciseForm(request.POST or None, instance=exercise)
    if request.method == "POST":
        if exercise_form.is_valid():
            exercise_form.instance.user = request.user
            exercise_form.instance.exercise = exercise
            exercise_form.save()
            exercise_form = ExerciseForm
            messages.success(request, "Exercise updated!")
            return redirect(reverse("home"))
    template = "home/edit_exercise.html"
    context = {
        "exercise": exercise,
        "exercise_form": exercise_form,
    }
    return render(request, template, context)


def delete_workout(request, id):
    workout = get_object_or_404(Workout, id=id)
    workout.delete()
    messages.success(request, "Workout deleted!")
    return redirect(reverse("home"))


def delete_exercise(request, id):
    exercise = get_object_or_404(Exercise, id=id)
    exercise.delete()
    messages.success(request, "Exercise deleted!")
    return redirect(reverse("home"))