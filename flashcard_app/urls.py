from django.urls import path
from . import views

app_name= 'flashcard_app'

urlpatterns = [
    path('', views.all_flashcards, name='flashcards_list'),
    path('add/', views.add_flashcard, name='add_flashcard'),
]