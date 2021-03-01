from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    task = models.CharField(max_length=255)
    created = models.DateField()
    due_on = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
