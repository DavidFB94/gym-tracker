from django.contrib import admin
from .models import Workout
from .models import Exercise


admin.site.register(Workout)
admin.site.register(Exercise)
