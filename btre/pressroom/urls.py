from django.urls import path
from . import views

urlpatterns = [
    path('', views.press_room, name='press_room'),
]