from django.urls import path
from QuestionManagement import views

urlpatterns = [
    path('', views.createQuiz, name="createQuiz"),
]