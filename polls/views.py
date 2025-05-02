from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from .models import Question

# Сторінка зі списком питань (головна сторінка)
def question_list(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/question_list.html', context)

# Реєстрація користувача
def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний вхід після реєстрації
            return redirect('polls:question_list')  # 'polls:question_list' має бути в urls.py
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {"form": form})

# Вхід користувача
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Перенаправлення після логіну
    return render(request, 'login.html', {'form': form})

# Вихід користувача
def logout_view(request):
    logout(request)
    return redirect('login')
