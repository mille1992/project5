from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profilePhotoUrl = models.CharField(max_length=255)
