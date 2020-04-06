from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

class item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=30, null=False)
