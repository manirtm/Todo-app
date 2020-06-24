from django.db import models

# Create your models here.
STATUS = [
    ("open", "open"),
    ("closed", "closed")
]

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status= models.CharField(max_length=200, choices=STATUS)
    
    def __str__(self):
        return self.title

