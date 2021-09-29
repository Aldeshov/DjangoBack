from django.db import models
from base.models import BookJournalBase
from utils.types import *


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=TYPES, default=Bullet)
    publisher = models.IntegerField()
    # for publisher -> Char field just forgot
