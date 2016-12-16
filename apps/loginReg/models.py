from __future__ import unicode_literals

from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def add_user(self, postData):
        errors = []
        if not len(postData['first_name']):
            errors.append('First name is required')
        if len(postData['first_name']) < 3:
            errors.append('Name must be at 3 characters long!')
        if len(postData['userName']) < 3:
            errors.append('User Name must be at 3 characters long!')
        if not len(postData['userName']):
            errors.append('userName is required!')
        check_email = self.filter(userName = postData['userName'])
        if check_email:
            errors.append('Sorry userName already exists!')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters!')
        if not postData['password'] == postData['confirm_password']:
            errors.append('Passwords must match!')
        modelsResponse = {}
        if errors:
            #failed ver
            modelsResponse['isRegistered'] = False
            modelsResponse['errors'] = errors
        else:
            #pass
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(first_name = postData['first_name'], userName =
            postData['userName'], password = hashed_password)
            modelsResponse['isRegistered'] = True
            modelsResponse['user'] = user
        return modelsResponse
    def login_user(self, postData):
        user = self.filter(userName = postData['userName'])
        errors = []
        modelsResponse = {}
        if not user:
            errors.append('Invalid userName!')
        else:
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                modelsResponse['isLoggedIn'] = True
                modelsResponse['user'] = user[0]
            else:
                errors.append('Invalid userName/password combination!')
        if errors:
            modelsResponse['isLoggedIn'] = False
            modelsResponse['errors'] = errors
        return modelsResponse
class AuthManager(models.Manager):
    def add_author(self, postData):
        errors = []
        modelsResponse = {}
        if not len(postData['authorList']):
            errors.append('Item is required')
        if len(postData['authorList']) < 3:
            errors.append('Item must be at 3 characters long!')
        if errors:
            #failed ver
            modelsResponse['isRegistered'] = False
            modelsResponse['errors'] = errors
        else:
            modelsResponse['isRegistered'] = True
            author = self.create(author = postData['authorList'])
            modelsResponse['author'] = author
        return modelsResponse

class User(models.Model):
    first_name = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
class Author(models.Model):
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthManager()
