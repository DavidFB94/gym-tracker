from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('add_exercise/<int:id>/', views.add_exercise, name='add_exercise'),
    path('edit_workout/<int:id>/', views.edit_workout, name='edit_workout'),
]