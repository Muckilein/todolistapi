from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth.models import User
# class AuthorAdmin(admin.ModelAdmin):
#     pass

class Todo(models.Model):
   title = models.CharField(max_length=30)
   description = models.CharField(max_length=30)
   created_at = models.DateField(default=datetime.date.today)
   user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
