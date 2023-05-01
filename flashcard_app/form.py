from django import forms
from .models import Flashcards

class FlashcardsForm(forms.ModelForm):
    class Meta:
        model = Flashcards
        fields = ['word', 'translation', 'image']
