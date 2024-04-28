from django.test import TestCase
from .forms import WorkoutForm, ExerciseForm


class TestWorkoutForm(TestCase):

    def test_workout_form_is_valid(self):
        """
        Test for required fields
        """
        workout_form = WorkoutForm(
            {
            "name": "My first workout",
            "date": "10/06/2024"
            }
            )
        self.assertTrue(workout_form.is_valid(), msg="Form is not valid")
    
    def test_workout_form_is_invalid(self):
        """
        Test for required fields
        """
        workout_form = WorkoutForm(
            {
            "name": "",
            "date": "10/06/2024"
            }
            )
        self.assertFalse(workout_form.is_valid(), msg="Form is valid")


class TestExerciseForm(TestCase):

    def test_exercise_form_is_valid(self):
        """
        Test for all fields
        """
        exercise_form = ExerciseForm(
            {
            "name": "Squat",
            "weight": "100",
            "sets": "3",
            "reps": "12"
            }
            )
        self.assertTrue(exercise_form.is_valid(), msg="Form is not valid")
    
    def test_exercise_form_is_invalid(self):
        """
        Test for all fields
        """
        exercise_form = ExerciseForm(
            {
            "name": "Squat",
            "weight": "100",
            "sets": "3",
            "reps": ""
            }
            )
        self.assertFalse(exercise_form.is_valid(), msg="Form is valid")