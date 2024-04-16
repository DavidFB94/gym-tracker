from django import forms
from django.forms import ModelForm
from .models import Workout
from .models import Exercise

#Create forms here
class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ('name', 'note', 'date',)


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'weight', 'sets', 'reps',)