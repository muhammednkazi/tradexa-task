# in this file we create tables as classes for database.

from django.db import models
from django.utils import timezone
# Create your models here.
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default='')
    last_name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    username=models.CharField(max_length=50,default='')
    password=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.first_name + self.last_name

class posts(models.Model):
    posts_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default='')
    text=models.TextField(max_length=1500,default='')
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title