from django.contrib import admin
from QuestionManagement.models import QuestionBank, ChoiceBank, QuestionTypeList

# Register your models here.
admin.site.register(QuestionBank)
admin.site.register(ChoiceBank)
admin.site.register(QuestionTypeList)
