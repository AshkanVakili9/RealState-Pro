from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)



class Profile(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_picture/%Y/%m/%d/')

    def __str__(self):
        return f'Profile of {self.seller.username}'
