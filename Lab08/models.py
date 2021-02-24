from django.db import models
from django.forms import widgets

# Create your models here.

class Post(models.Model):
    
    name=models.CharField(max_length=50)
    content=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'