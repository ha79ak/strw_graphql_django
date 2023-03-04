from django.contrib import admin

from .models import Author, Book, Fruit, Color

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Fruit)
admin.site.register(Color)
