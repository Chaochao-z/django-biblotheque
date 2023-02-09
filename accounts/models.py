from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_libraire = models.BooleanField(default=False)
    adresse = models.CharField(max_length=200, blank=False)
    cp = models.CharField(max_length=6, blank=False)
