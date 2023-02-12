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
    ville = models.CharField(max_length=50)
    cp = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Livre(models.Model):
    titre = models.CharField(max_length=60)
    auteur = models.CharField(max_length=60)
    jaquette = models.CharField(max_length=60)
    editeur = models.CharField(max_length=60)
    collection = models.CharField(max_length=60)
    genre = models.CharField(max_length=60)
    dispo = models.BooleanField(default=True)
    biblio = models.ForeignKey(Biliotheque, on_delete=models.CASCADE)


class Pret(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    dateend = models.DateTimeField()
    daterendu = models.DateTimeField(default=None, blank=True, null=True)

class Groupe_Lecture(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    date = models.DateTimeField()
    biblio = models.ForeignKey(Biliotheque, on_delete=models.CASCADE)

class GL_User(models.Model):
    dateinscription = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    groupe_lecture = models.ForeignKey(Groupe_Lecture, on_delete=models.CASCADE)

