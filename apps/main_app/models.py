from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2: 
            # letters only as well
            errors['first_name'] = "First name must be at least 2 characters; letters only"
        if len(postData['last_name']) < 2:
            # letters only as well
            errors['last_name'] = "Last name must be at least 2 characters; letters only"
        if postData['email'] == "":
            errors['email'] = "Email is required"
        if postData['email']:
            errors['existingemail'] = "This email is already being used"
        if len(postData['password']) < 8 or postData['password'] == "" or postData['password'] != postData['password_confirmation']:
            errors['password'] = "Password is required.  Please make sure it is at least 8 characters and matches with your password confirmation."
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
