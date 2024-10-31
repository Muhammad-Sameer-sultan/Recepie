from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    # image = models.ImageField()
    # file  = models.FileField()

class Car(models.Model):
    name = models.CharField(max_length=50)
    speed = models.IntegerField()

    def __str__(self)->str:
        return c