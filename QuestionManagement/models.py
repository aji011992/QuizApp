from django.db import models
from datetime import datetime

# Create your models here.
class QuestionTypeList(models.Model):

    class Meta:
        db_table = 'question_type_list'

    question_type_id = models.CharField(max_length=20, unique=True)
    question_type_txt = models.CharField(max_length=200)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)

class ChoiceBank(models.Model):

    class Meta:
        db_table = 'choice_bank'

    choice_id = models.CharField(max_length=30, unique=True)
    choice_txt = models.CharField(max_length=2000)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)

class QuestionBank(models.Model):

    class Meta:
        db_table = 'question_bank'

    question_id = models.CharField(max_length=20, unique=True)
    question_type_id = models.ForeignKey('QuestionTypeList', on_delete=models.PROTECT)
    question_txt = models.CharField(max_length=2000)
    answer_id = models.CharField(max_length=30)
    choice_50_50 = models.CharField(max_length=30)
    remaining_choice = models.CharField(max_length=30, default=None)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)
