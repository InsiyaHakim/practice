# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
     def creating_db(self,form_data):
        error=[]
        f_name=str(form_data['f_name'])
        l_name=str(form_data['l_name'])
        email=str(form_data['email'])
        password=str(form_data['password'])
        hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        if len(f_name) <= 1:
            error.append("first name must be 8 characters")
        if len(l_name) <= 1:
            error.append("last name must be 8 characters")
        if not EMAIL_REGEX.match(email):
            error.append("invalid email")
        if len(error)>0:
            return error
        else:
            self.create(f_name=form_data['f_name'], l_name=form_data['l_name'], email=form_data['email'],password=hash1)
            return error

class User(models.Model):
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    object=UserManager()
