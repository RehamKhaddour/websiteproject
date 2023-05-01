from django.shortcuts import render
from .models import Flashcards
from .form import FlashcardsForm

# Create your views here.
def all_flashcards(request):
    all_flashcards_obj = Flashcards.objects.all()
    context = {'flashcards': all_flashcards_obj}
    return render(request, 'flashcards.html', context)

def add_flashcard(request):
    if request.method=='POST':
        form = FlashcardsForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
    else:
        form = FlashcardsForm()
    
    context = {'form':form}
    return render(request, 'add_flashcard.html', context=context)