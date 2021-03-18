from django.contrib.auth.models import User
from django.db import models


class Person(User):
    class Meta:
        proxy = True
        ordering = ('username',)


class List(models.Model):
    name = models.CharField(max_length=255)


class TaskManager(models.Manager):
    def get_task(self, request, list_id, task_id):
        if request.user.is_authenticated:
            return self.filter(owner_id=request.user.id, list_id=list_id, id=task_id).first()
        else:
            return None

    def get_tasks(self, request, list_id):
        if request.user.is_authenticated:
            return self.filter(owner_id=request.user.id, list_id=list_id)
        else:
            return None

    def get_completed_tasks(self, request, list_id):
        if request.user.is_authenticated:
            return self.get_tasks(request, list_id).filter(mark=True)
        else:
            return None

    def get_incomplete_tasks(self, request, list_id):
        if request.user.is_authenticated:
            return self.get_tasks(request, list_id).filter(mark=False)
        else:
            return None


class Task(models.Model):
    task = models.CharField(max_length=255)
    created = models.DateField()
    due_on = models.DateField()
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    mark = models.BooleanField(default=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    objects = TaskManager()
