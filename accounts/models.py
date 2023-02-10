from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    is_libraire = models.BooleanField(default=False)
    adresse = models.CharField(max_length=200, blank=False)
    cp = models.CharField(max_length=6, blank=False)

class Biliotheque(models.Model):
    name = models.CharField(max_length=60)
    adresse = models.CharField(max_length=60)
    cp = models.CharField(max_length=60)


class Livre(models.Model):
    titre = models.CharField(max_length=60)
    auteur = models.CharField(max_length=60)
    jaquette = models.CharField(max_length=60)
    editeur = models.CharField(max_length=60)
    collection = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    bibliotheque = models.ForeignKey(Biliotheque, on_delete=models.CASCADE)


class Pret(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)