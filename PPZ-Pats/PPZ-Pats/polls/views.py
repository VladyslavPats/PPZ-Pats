from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.http import JsonResponse

# ✅ API View для отримання списку питань
class QuestionListAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

# ✅ Сторінка зі списком питань (HTML)
def question_list_view(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/question_list.html', context)

# ✅ Простий JSON API (альтернатива DRF APIView, якщо не хочеш DRF)
def question_list_json(request):
    questions = list(Question.objects.values())
    return JsonResponse(questions, safe=False)

# ✅ Реєстрація користувача
def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {"form": form})

# ✅ Вхід користувача
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html', {'form': form})

# ✅ Вихід користувача
def logout_view(request):
    logout(request)
    return redirect('login')
