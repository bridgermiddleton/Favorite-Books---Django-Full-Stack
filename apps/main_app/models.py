from __future__ import unicode_literals
from django.db import models

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2: 
            # letters only as well
            errors['first_name'] = "First name must be at least 2 characters."
        if hasNumbers(postData['first_name']):
            errors['first_name_letters_only'] = "LETTERS ONLY!"
        if len(postData['last_name']) < 2:
            # letters only as well
            errors['last_name'] = "Last name must be at least 2 characters."
        if hasNumbers(postData['last_name']):
            errors['last_name_letters_only'] = "LETTERS ONLY!"
        if postData['email'] == "":
            errors['email'] = "Email is required"
        if User.objects.filter(email=postData['email']):
            errors['email_exists'] = "Email already exists."
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
