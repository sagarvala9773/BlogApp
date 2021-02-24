from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    roll_no=models.IntegerField(unique=True,null=False)
    email=models.CharField(max_length=70)
    password=models.CharField(max_length=60)
    