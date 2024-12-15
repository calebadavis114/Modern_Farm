from django.db import models
from django.contrib.auth.models import AbstractUser

class Farmer(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    #PASSWORD field is their by default no need to add
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #email and password are required by default