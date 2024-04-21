from django import forms
from django.forms import ModelForm
from .models import Workout
from .models import Exercise

#Create forms here
class WorkoutForm(ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Workout name'}))
    note = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control',
    'placeholder': 'Note.... (optional)', 'rows': 5}), required=False)
    date = forms.DateField(label='', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Workout
        fields = ('name', 'note', 'date',)


class ExerciseForm(ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Exercise name'}))
    weight = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Weight'}))
    sets = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Sets'}))
    reps = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder': 'Reps',}))

    class Meta:
        model = Exercise
        fields = ('name', 'weight', 'sets', 'reps',)