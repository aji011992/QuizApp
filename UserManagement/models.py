from django.db import models
import os
from datetime import datetime

# Create your models here.
from django.db.models import DateTimeField


def get_image_path(instance, filename):
    return os.path.join('images', str(instance.user_id) + "."+ filename.split('.')[-1])

class RoleList(models.Model):

    class Meta:
        db_table = 'role_list'

    role_id = models.AutoField(primary_key=True)
    role_txt = models.CharField(max_length=250)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class UserList(models.Model):

    class Meta:
        db_table = 'user_list'

    user_id = models.CharField(max_length=64, db_index=True)
    user_name = models.CharField(max_length=250)
    password = models.CharField(max_length=36)
    roe_id = models.ForeignKey('RoleList', on_delete=models.PROTECT)
    active_ind = models.CharField(max_length=1)
    profile_pic = models.ImageField(blank=True, null=True, upload_to=get_image_path)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
