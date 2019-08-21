from django.contrib import admin
from QuizManagement.models import QuizList, ComplexityList, QuizQuestions, QuizAttempts, QuizResult

# Register your models here.
admin.site.register(QuizList)
admin.site.register(ComplexityList)
admin.site.register(QuizQuestions)
admin.site.register(QuizAttempts)
admin.site.register(QuizResult)
