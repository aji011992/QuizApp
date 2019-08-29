from django.db import models
from datetime import datetime

# Create your models here.
from django.db.models import DateTimeField
from django.utils import timezone


class QuestionTypeList(models.Model):

    class Meta:
        db_table = 'question_type_list'

    question_type_id = models.AutoField(primary_key=True)
    question_type_txt = models.CharField(max_length=200)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class ChoiceBank(models.Model):

    class Meta:
        db_table = 'choice_bank'

    choice_id = models.CharField(max_length=64, db_index=True)
    choice_txt = models.CharField(max_length=2000)
    created_user_id = models.CharField(max_length=250)
    # created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    #created_timestamp = models.DateTimeField(default=timezone.now(), blank=True)
    created_timestamp = DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    # last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    #last_updated_timestamp = models.DateTimeField(default=timezone.now(), blank=True)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class QuestionBank(models.Model):

    class Meta:
        db_table = 'question_bank'

    question_id = models.AutoField(primary_key=True)
    question_type_id = models.ForeignKey('QuestionTypeList', on_delete=models.PROTECT)
    question_txt = models.CharField(max_length=2000)
    answer_id = models.CharField(max_length=30)
    choice_50_50 = models.CharField(max_length=30)
    remaining_choice = models.CharField(max_length=30, default=None)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
