from django.db import models

class Course(models.Model):
    name= models.CharField(max_length=200)
    student=models.CharField(max_length=200)
    email=models.EmailField()
# Create your models here.
