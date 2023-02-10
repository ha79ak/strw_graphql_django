import uuid
from django.db import models


class Author(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=200)


class Book(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
