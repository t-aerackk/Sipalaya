from django.db import models

# Create your models here.

class Student_Info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images')

class Student_Query(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    message=models.CharField(max_length=300)


