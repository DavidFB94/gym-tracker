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

    def test_render_add_exercise_page_with_exercise_form(self):
        """
        Verifies get request for add_exercise containing an exercise form
        """
        workout_id = self.workout.id
        response = self.client.get(reverse(
            "add_exercise", kwargs={'id': workout_id}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<form", response.content)
        self.assertIsInstance(
            response.context["exercise_form"], ExerciseForm)

    def test_successful_add_workout_form_submission(self):
        """
        Test for successfully submitting a workout form
        """
        workout_data = {
            "name": "Workout 1",
            "note": "A note",
            "date": "2024-10-10"
        }
        response = self.client.post(reverse("add_workout"), workout_data)
        self.assertRedirects(response, expected_url=reverse("home"), status_code=302, target_status_code=200)

    def test_unsuccessful_add_workout_form_submission(self):
        """
        Test for missing name in submiting a workout form
        """
        workout_data = {
            "name": "",
            "note": "A note",
            "date": "2024-10-10"
        }
        response = self.client.post(reverse("add_workout"), workout_data)
        self.assertTrue(response.context["form"].errors, msg="The form has all the required inputs.")

    def test_successful_add_exercise_form_submission(self):
        """
        Test for successfully submitting an exercise form
        """
        workout_id = self.workout.id
        exercise_data = {
            "name": "Squat",
            "weight": "100",
            "sets": "5",
            "reps": "5"
        }
        response = self.client.post(reverse("add_exercise", kwargs={'id': workout_id}), data=exercise_data)
        self.assertFalse(response.context["form"].errors, msg="The form is missing required input.")
        self.assertEqual(response.status_code, 200)

    def test_unsuccessful_add_exercise_form_submission(self):
        """
        Test for missing reps in submitting exercise form
        """
        workout_id = self.workout.id
        exercise_data = {
            "name": "Squat",
            "weight": "100",
            "sets": "5",
            "reps": ""
        }
        response = self.client.post(reverse("add_exercise", kwargs={'id': workout_id}), data=exercise_data)
        self.assertTrue(response.context["form"].errors, msg="The form has all the required inputs.")
        self.assertEqual(response.status_code, 200)
