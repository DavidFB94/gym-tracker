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


