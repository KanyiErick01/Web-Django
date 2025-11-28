from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    Author= models.CharField(max_length=20)
    Title=models.CharField()
    Date_created=models.DateField(default=timezone.now)
    content=models.TextField()

    class Meta():
        ordering = ['-Date_created']

    def __str__(self):
        return self.Title

class User(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField()
    date_created=models.DateField(default=timezone.now) 

    def __str__(self):
        return self.username      

