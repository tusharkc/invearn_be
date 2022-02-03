from pyexpat import model
from statistics import mode
from django.db import models
from pymongo import MongoClient

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
