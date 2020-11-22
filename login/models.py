from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=254,blank=False)
    password = models.CharField(max_length=60,blank=False)
