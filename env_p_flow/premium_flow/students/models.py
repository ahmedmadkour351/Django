from ast import mod
import email
from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    mobil = models.CharField(max_length=15)
    mail = models.EmailField(max_length=100)
    active = models.BooleanField(default=True)


