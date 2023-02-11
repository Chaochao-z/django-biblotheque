from django import forms
from accounts.models import Livre, Biliotheque
from django.forms import ModelForm, ModelChoiceField


class LivreForm(ModelForm):
    biblio = ModelChoiceField(
        queryset=Biliotheque.objects.order_by('name'),
        to_field_name='name',
        required=False,

    )

    class Meta:
        model = Livre
        fields = [
            'titre',
            'auteur',
            'jaquette',
            'editeur',
            'collection',
            'genre',
            'biblio'
        ]
        labels = {
            'title': 'Titre',
            'auteur': 'Auteur',
            'jaquette': 'Jaquette',
            'editeur': 'Éditeur',
            'collection': 'Collection',
            'genre': 'Genre',
            'biblio': 'Bibliothèque'
        }
