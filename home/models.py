from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    """
    Model for user workout tracking.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    note = models.TextField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    """
    Model for user exercises for the workout.
    """
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    weight = models.CharField(max_length=30, null=False, blank=False)
    sets = models.PositiveIntegerField(null=False, blank=False)
    reps = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name