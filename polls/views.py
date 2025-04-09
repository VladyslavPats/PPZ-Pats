from django.shortcuts import render
from .models import Question

def question_list(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/question_list.html', context)
