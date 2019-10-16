from __future__ import unicode_literals
from django.db import models
from apps.main_app.models import User

class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        pass

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    pass


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments")
    message = models.ForeignKey(Message, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
# Create your models here.
