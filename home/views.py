from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm


def home(request):
    """
    Home view.
    Displays the saved workout cards
    in a paginted list, ordered by
    date, descending.
    """
    if request.user.is_authenticated:
        # Display workout list
        queryset = Workout.objects.filter(user=request.user).order_by('-date')
    else:
        queryset = []
    # Paginator
    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "home/home.html", {"page_obj": page_obj})


@login_required
def add_workout(request):
    """
    View for add_workout.
    Saves form on submission.
    Display confirmation message,
    redirects to home.
    """
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


@login_required
def add_exercise(request, id):
    """
    View for add_exercise.
    Checks for correct user.
    Connects the exercise to the selected workout.
    Saves form on submission.
    Display confirmation message.
    """
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
    template = "home/add_exercise.html"
    context = {
        "workout": workout,
        "exercise_form": exercise_form,
    }
    return render(request, template, context)


@login_required
def edit_workout(request, id):
    """
    View for edit_workout.
    Checks for correct user.
    Checks for workout.
    Saves form on submission.
    Display confirmation message,
    redirects to home.
    """
    workout = get_object_or_404(Workout, id=id)
    if workout.user != request.user:
        messages.error(request, "Access denied, this isn't your workout!")
        return redirect(reverse("home"))
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


@login_required
def edit_exercise(request, id):
    """
    View for edit_exercise.
    Checks for correct user.
    Checks the exercise with the selected workout.
    Saves form on submission.
    Display confirmation message.
    Redirect back to add_exercise inside same workout
    for further editing.
    """
    exercise = get_object_or_404(Exercise, id=id)
    if exercise.workout.user != request.user:
        messages.error(request, "Access denied, this isn't your exercise!")
        return redirect(reverse("home"))
    exercise_form = ExerciseForm(request.POST or None, instance=exercise)
    if request.method == "POST":
        if exercise_form.is_valid():
            exercise_form.instance.user = request.user
            exercise_form.instance.exercise = exercise
            exercise_form.save()
            exercise_form = ExerciseForm
            messages.success(request, "Exercise updated!")
            # Redirects back to add_exercise inside same workout
            return redirect(add_exercise, exercise.workout.id)
    template = "home/edit_exercise.html"
    context = {
        "exercise": exercise,
        "exercise_form": exercise_form,
    }
    return render(request, template, context)


@login_required
def delete_workout(request, id):
    """
    View for delete_workout.
    Checks for correct user.'
    Deletes selected workout.
    Display confirmation message,
    redirect back to home.
    """
    workout = get_object_or_404(Workout, id=id)
    if workout.user != request.user:
        messages.error(request, "Access denied, this isn't your workout!")
        return redirect(reverse("home"))
    workout.delete()
    messages.success(request, "Workout deleted!")
    return redirect(reverse("home"))


@login_required
def delete_exercise(request, id):
    """
    View for delete_exercise.
    Checks for correct user.'
    Deletes selected exercise.
    Display confirmation message,
    redirect back to home.
    """
    exercise = get_object_or_404(Exercise, id=id)
    if exercise.workout.user != request.user:
        messages.error(request, "Access denied, this isn't your exercise!")
        return redirect(reverse("home"))
    exercise.delete()
    messages.success(request, "Exercise deleted!")
    return redirect(reverse("home"))
