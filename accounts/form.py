from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'adresse',
            'cp'
        ]
        labels = {
            'first_name': 'prénom',
            'last_name': 'nom',
            'username': 'Identifiant'
        }
