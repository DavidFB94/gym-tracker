from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import WorkoutForm, ExerciseForm
from .models import Workout, Exercise


class TestHomeViews(TestCase):

    def setUp(self):
        """
        Sets up superuser + logs in to access all forms
        Creates workout + exercise content
        """
        self.user = User.objects.create_superuser(
            username ="myUsername",
            password ="myPassword",
            email = "test@test.com"
        )
        self.client.login(username="myUsername", password="myPassword")
        self.workout = Workout(name="", note="", date="2024-01-01", user=self.user)
        self.exercise = Exercise(name="", weight="", sets="0", reps="", workout=self.workout)
        self.workout.save()
        self.exercise.save()
