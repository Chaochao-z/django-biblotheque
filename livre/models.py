from django.db import models
from accounts.models import CustomUser


# Create your models here.


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
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    user = models.ForeignKey(CustomUser)
    livre = models.ForeignKey(Livre)
