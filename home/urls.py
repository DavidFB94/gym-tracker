from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('add-exercise/', views.add_exercise, name='add-exercise'),
]