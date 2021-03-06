from django.db import models
from datetime import datetime

# Create your models here.
from django.db.models import DateTimeField


class ComplexityList(models.Model):

    class Meta:
        db_table = 'complexity_list'

    complexity_id = models.CharField(max_length=20, unique=True)
    complexity_txt = models.CharField(max_length=250)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class QuizList(models.Model):

    class Meta:
        db_table = 'quiz_list'

    quiz_id = models.AutoField(primary_key=True)
    quiz_name = models.CharField(max_length=500)
    quiz_start_time = models.DateTimeField(blank=True)
    quiz_end_time = models.DateTimeField(blank=True)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class QuizQuestions(models.Model):

    class Meta:
        db_table = 'quiz_questions'

    quiz_id = models.ForeignKey('QuizList', on_delete=models.PROTECT)
    question_id = models.ForeignKey('QuestionManagement.QuestionBank', on_delete=models.PROTECT)
    complexity_id = models.ForeignKey('ComplexityList', on_delete=models.PROTECT)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class QuizAttempts(models.Model):

    class Meta:
        db_table = 'quiz_attempts'

    quiz_id = models.ForeignKey('QuizList', on_delete=models.PROTECT)
    user_id = models.ForeignKey('UserManagement.UserList', on_delete=models.PROTECT)
    ip_address = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=50)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class QuizResult(models.Model):

    class Meta:
        db_table = 'quiz_result'

    quiz_id = models.ForeignKey('QuizList', on_delete=models.PROTECT)
    user_id = models.ForeignKey('UserManagement.UserList', on_delete=models.PROTECT)
    question_id = models.ForeignKey('QuestionManagement.QuestionBank', on_delete=models.PROTECT)
    answer_id = models.CharField(max_length=30)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

