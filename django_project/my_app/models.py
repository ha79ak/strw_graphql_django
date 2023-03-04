import uuid
from django.db import models


class Author(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Fruit(models.Model):
    """A tasty treat"""
    name = models.CharField(max_length=20)
    color = models.ForeignKey('Color', blank=True, null=True,
            related_name='fruits', on_delete=models.CASCADE)

class Color(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="field description",
    )
