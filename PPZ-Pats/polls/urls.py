from .views import QuestionListView
from django.urls import path
from . import views

app_name = 'polls'  # Це дозволяє використовувати простір імен у шаблонах: polls:login, polls:register тощо

urlpatterns = [
    path('', views.question_list, name='home'),  # Головна сторінка зі списком питань
    path('register/', views.register_view, name='register'),  # Сторінка реєстрації
    path('login/', views.login_view, name='login'),  # Сторінка входу
    path('logout/', views.logout_view, name='logout'),  # Вихід
    path('api/questions/', QuestionListView.as_view(), name='questions-api'),
]
