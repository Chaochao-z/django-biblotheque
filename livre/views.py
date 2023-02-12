from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from accounts.models import Livre, Biliotheque, Pret
from .form import LivreForm
from django.contrib import messages
from datetime import datetime
import pytz



# Create your views here.
def index(request):
    context = {}
    context['user'] = request.user
    return render(request, 'test.html', context=context)

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
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
            obj = form.save()
            obj.dispo = True
            obj.save()
            messages.success(request, "Le livre a bien été crée")
            return redirect('libraire_livre')
        else:
            messages.error(request, form.errors)
    return render(request, 'libraire/livre-new.html', {'form': form})


def deleteLivre(request, livre_pk):
    livre = Livre.objects.get(id=livre_pk)
    livre.delete()
    return redirect('libraire_livre')


def livres(request):
    context = {}
    context["livres"] = Livre.objects.all()
    return render(request, 'livre/livres.html', context=context)

@login_required
def emprumter(request, livre_pk):
    if request.user.pk:
        Pret.objects.create(user_id=request.user.pk,livre_id=livre_pk, rendu=False,dateend=datetime.now() + timedelta(days=15))
        livre = Livre.objects.get(id=livre_pk)
        livre.dispo = False
        livre.save()
        messages.success(request, "Vous avez bien emprunter le livre, vous avez 15Jours pour le rendre")
        return redirect('livres')
    else:
        return redirect('login')

@login_required()
def meslivres(request):
    context = {}
    now = datetime.now()
    context["todaynow"] = now.replace(tzinfo=pytz.utc)
    context["prets"] = Pret.objects.filter(user_id=request.user.pk)
    return render(request, 'livre/meslivres.html', context=context)



