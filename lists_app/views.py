from django.shortcuts import render
from .models import Lesson, Words
from django.core.paginator import Paginator
from .form import WordsForm

# Create your views here.
def lessons_list(request):
    all_lessons = Lesson.objects.all()
    context = {'lessons': all_lessons}
    return render(request, 'lesson_list.html', context)

def lesson_words(request, id):
    lesson_words = Words.objects.filter(lesson=id)
    paginator = Paginator(lesson_words, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "word_list.html", {"page_obj": page_obj})

def add_words(request):
    if request.method=='POST':
        form = WordsForm(request.POST)
        if form.is_valid():
            myform = form.save()
    else:
        form = WordsForm()
    
    context = {'form':form}
    return render(request, 'add_words.html', context=context)