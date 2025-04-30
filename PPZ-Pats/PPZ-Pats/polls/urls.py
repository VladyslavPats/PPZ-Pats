from django.urls import path
from .views import (
    question_list_view,
    question_list_json,
    QuestionListAPIView,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    path('', question_list_view, name='home'),  # HTML сторінка
    path('api/polls/', question_list_json),     # JSON (без DRF)
    path('api/polls-drf/', QuestionListAPIView.as_view()),  # JSON через DRF
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
