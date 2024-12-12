from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Recepie(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True , blank= True)
    recepie_name= models.CharField(max_length=100)
    recepie_description = models.TextField()
    recepie_image = models.ImageField(upload_to="recepie")