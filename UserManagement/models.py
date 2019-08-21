from django.db import models
import os
from datetime import datetime

# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('images', str(instance.user_id), filename)

class RoleList(models.Model):

    class Meta:
        db_table = 'role_list'

    role_id = models.CharField(max_length=40, unique=True)
    role_txt = models.CharField(max_length=250)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)

class UserList(models.Model):

    class Meta:
        db_table = 'user_list'

    user_id = models.CharField(max_length=100, unique=True)
    user_name = models.CharField(max_length=250)
    password = models.CharField(max_length=36)
    roe_id = models.ForeignKey('RoleList', on_delete=models.PROTECT)
    active_ind = models.CharField(max_length=1)
    profile_pic = models.ImageField(blank=True, null=True, upload_to=get_image_path)
    created_user_id = models.CharField(max_length=250)
    created_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    updated_user_id = models.CharField(max_length=250)
    last_updated_timestamp = models.DateTimeField(default=datetime.now, blank=True)
