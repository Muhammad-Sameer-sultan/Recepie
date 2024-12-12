# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager  # Adjust the import path as necessary

class CustomUser(AbstractUser):
    username = None  # Remove the username field
    user_profile_image = models.ImageField(upload_to="profile", blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    user_bio = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=True)  # Make email optional
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []  # No additional required fields
    
    objects = UserManager()  # Link the custom manager

    def __str__(self):
        return str(self.phone_number)
