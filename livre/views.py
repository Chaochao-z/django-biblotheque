from django.shortcuts import render, redirect
from accounts.models import Livre, Biliotheque
from .form import LivreForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'test.html', context={})


def libraire(request):
    return render(request, 'libraire/index.html', context={})


def bibliotheque(request):
    context = {}
    context["bibliotheques"] = Biliotheque.objects.order_by("name")
    return render(request, 'libraire/bibliotheque.html', context=context)


def livre(request):
    context = {}
    context["livres"] = Livre.objects.order_by("titre")
    return render(request, 'libraire/livres.html', context=context)


def addLivre(request):
    form = LivreForm()
    if request.method == "POST":
        form = LivreForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le livre a bien été crée")
            return redirect('libraire_livre')
        else:
            messages.error(request, form.errors)
    return render(request, 'libraire/livre-new.html', {'form': form})
