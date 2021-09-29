from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateField()
