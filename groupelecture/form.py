from django.db import models
from django.forms import ModelForm, DateTimeField,DateTimeInput
from accounts.models import Groupe_Lecture

# Create your models here.

class Goupe_lecture_form(ModelForm):
    class Meta:
        model = Groupe_Lecture
        fields = [
            'title',
            'description',
            'date',
            'biblio',
        ]

        labels = {
            'title' : 'Titre',
            'description' : 'Description',
            'date' : 'Date du groupe lecture',
            'biblio': 'Lieu bibliothèque',
        }

        widgets = {
            'date': DateTimeInput(
                format='%d/%m/%Y %H:%M',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'datetime-local'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                       }),
        }
