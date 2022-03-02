from django.db import models
import re
import bcrypt
from app_1.models import *

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        user_emails = User.objects.filter(email = postData['email'])
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be atleast 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be atleast 2 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Email address is invalid'
        if len(user_emails) > 0:
            errors['email'] = 'Email is already in use'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be 8 or more characters'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Both password fields must match'
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors['email'] = 'Email address is invalid'
        if email_regex.match(postData['email']):
            if len(user) < 1:
                errors['email'] = 'There is no account registered with this email'
        if len(user) == 1:
            if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                    errors['password'] = 'Email and password do not match'
        return errors

    def update_validator(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be atleast 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be atleast 2 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Email address is invalid'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()