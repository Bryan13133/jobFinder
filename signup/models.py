from django.db import models
from django.core.exceptions import ValidationError 
# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=60,blank=False,) 
    email = models.EmailField(max_length=70,blank=False) 
    password = models.CharField(max_length=60,blank=False) 
    confirmPassword = models.CharField(max_length=60,blank=False) 
