from __future__ import unicode_literals
from django.db import models
from apps.main_app.models import User

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['title'] == "":
            errors['title'] = "Title is required."
        if len(postData['description']) < 5:
            errors['description'] = "Description must be at least 5 characters."
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

# Create your models here.
