from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.form import UserForm


# Create your views here.

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a bien été creer")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    return render(request, 'auth/register.html', {'form':form})


def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login Success')
            return redirect('home')
        else:
            messages.error(request, "Erreur d'identifiant ou password")
    return render(request, 'auth/login.html')

@login_required
def deconnexion(request):
    logout(request)
    return redirect('home')
