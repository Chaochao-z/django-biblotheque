from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from accounts.models import Livre, Biliotheque, Pret
from .form import LivreForm
from django.contrib import messages
from datetime import datetime, timedelta
import pytz


# Create your views here.
def index(request):
    context = {}
    context['user'] = request.user
    context['livres'] = Livre.objects.all()[:4]
    context['bibliotheques'] = Biliotheque.objects.all()[:4]
    return render(request, 'home.html', context=context)


@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraire(request):
    return redirect('libraire_emprunts')

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def bibliotheque(request):
    context = {}
    context["bibliotheques"] = Biliotheque.objects.order_by("name")
    return render(request, 'libraire/bibliotheque.html', context=context)

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def livre(request):
    context = {}
    context["livres"] = Livre.objects.order_by("titre")
    return render(request, 'libraire/livres.html', context=context)

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
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

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def deleteLivre(request, livre_pk):
    livre = Livre.objects.get(id=livre_pk)
    livre.delete()
    return redirect('libraire_livre')


def livres(request):
    context = {}
    context["alllivres"] = Livre.objects.all()
    context["livres"] = Livre.objects.all()
    return render(request, 'livre/livres.html', context=context)


@login_required
def emprumter(request, livre_pk):
    if request.user.pk:
        compteur = 0
        prets = Pret.objects.filter(user_id=request.user.pk)
        for pret in prets:
            if pret.daterendu:
                pass
            else:
                compteur = compteur + 1
        if compteur >= 5:
            messages.error(request,
                           "Vous avez déjè emprunter 5 livres, merci de les retourner au bibliothèque avant d'emprunter d'autre livre.")
            return redirect('livres')
        Pret.objects.create(user_id=request.user.pk, livre_id=livre_pk, dateend=datetime.now() + timedelta(days=15))
        livre = Livre.objects.get(id=livre_pk)
        livre.dispo = False
        livre.save()
        messages.success(request,
                         "Vous avez bien emprunter le livre, vous avez 15Jours pour le rendre. Vous Pouvez maximun enprumter 5 livres")
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

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraireEmprunt(request):
    context = {}
    now = datetime.now()
    context["todaynow"] = now.replace(tzinfo=pytz.utc)
    context["prets"] = Pret.objects.order_by("-date")
    return render(request, 'libraire/lesemprunts.html', context=context)

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraireRendreLivre(request, pret_pk):
    pret = Pret.objects.get(id=pret_pk)
    pret.daterendu = datetime.now()
    livre = Livre.objects.get(id=pret.livre.pk)
    livre.dispo = True
    pret.save()
    livre.save()
    messages.success(request, 'Le Livre est retourné au biblothèque')
    return redirect('libraire_emprunts')

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraireLivresRetard(request):
    context = {}
    now = datetime.now()
    context["todaynow"] = now.replace(tzinfo=pytz.utc)
    context["prets"] = Pret.objects.order_by("-date")
    return render(request, 'libraire/livre-retard.html', context=context)

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraireEmpruntAddTime(request, pret_pk):
    pret = Pret.objects.get(id=pret_pk)
    pret.dateend = pret.dateend + timedelta(days=5)
    pret.save()
    message = "Vous avez ajouter 5 jours pour M."+pret.user.username+" sur le livre "+ pret.livre.titre
    messages.success(request, message)
    return redirect('libraire_emprunts')


def searchLivre(request):
    livre = ""
    if request.GET:
        if request.GET['livre']:
            if Livre.objects.filter(id=request.GET['livre']).exists():
                livre = Livre.objects.get(id=request.GET['livre'])
    context = {}
    context["livre"] = livre
    context["alllivres"] = Livre.objects.all()
    return render(request, 'livre/searchlivre.html', context=context)

def bibliotheques(request):
    context = {}
    context["bibliotheques"] = Biliotheque.objects.order_by("name")
    return render(request, 'bibliotheque/index.html', context=context)

def bibliothequesearch(request):
    bibliotheque = ""
    if request.GET:
        if request.GET['id']:
            if Biliotheque.objects.filter(id=request.GET['id']).exists():
                bibliotheque = Biliotheque.objects.get(id=request.GET['id'])
    context = {}
    context["resultat"] = bibliotheque
    context["bibliotheques"] = Biliotheque.objects.all()
    return render(request, 'bibliotheque/search.html', context=context)

def bibliothequeLivre(request):
    livres =""
    bibliotheque =""
    if request.GET:
        if request.GET['id']:
            if Livre.objects.filter(biblio_id=request.GET['id']).exists():
                livres = Livre.objects.filter(biblio_id=request.GET['id'])
            if Biliotheque.objects.filter(id=request.GET['id']).exists():
                bibliotheque = Biliotheque.objects.get(id=request.GET['id'])
    context = {}
    context["bibliotheque"] = bibliotheque
    context["livres"] = livres
    return render(request, 'bibliotheque/livres.html', context=context)