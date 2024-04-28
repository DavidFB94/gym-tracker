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

    def test_render_add_workout_page_with_workout_form(self):
        """
        Verifies get request for add_workout containing a workout form
        """
        response = self.client.get(reverse(
            "add_workout",
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<form", response.content)
        self.assertIsInstance(
            response.context["workout_form"], WorkoutForm)

