from django.urls import path
from . import views

app_name= 'lists_app'

urlpatterns = [
    path('', views.lessons_list, name='lesson_list'),
    path('<int:id>', views.lesson_words, name='lesson'),
    path('add', views.add_words, name='add_new_word')
]