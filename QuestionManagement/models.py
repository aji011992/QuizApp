from django.db import models
from datetime import datetime

# Create your models here.
class QuestionBank(models.Model):

    class Meta:
        db_table = 'question_bank'

    question_id = models.CharField(max_length=50,unique=True)
    question_type_id = models.CharField(max_length=25)
    question_txt = models.CharField(max_length=260)
    answer_id = models.CharField(max_length=20)
    choice_50_50 = models.CharField(max_length=20)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)

class ChoiceBank(models.Model):

    class Meta:
        db_table = 'choice_bank'

    choice_id = models.CharField(max_length=20)
    choice_txt = models.CharField(max_length=250)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)

class QuestionTypeList(models.Model):

    class Meta:
        db_table = 'question_type_list'

    question_type_id = models.ForeignKey('QuestionBank',on_delete=models.PROTECT)
    question_type_txt = models.CharField(max_length=20)
    choice_id = models.ForeignKey('ChoiceBank',on_delete=models.PROTECT)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)
