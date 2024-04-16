from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add-workout/', views.add_workout, name='add-workout'),
    path('add-exercise/', views.add_exercise, name='add-exercise'),
]