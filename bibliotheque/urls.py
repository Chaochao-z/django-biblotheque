"""bibliotheque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import livre.views as livre_views
import accounts.views as accounts_views

urlpatterns = [
    path('', livre_views.index, name="home"),
    path('register', accounts_views.register, name="register"),
    path('login', accounts_views.connexion, name="login"),
    path('accounts/login/', accounts_views.connexion, name="login_next"),
    path('logout', accounts_views.deconnexion, name="logout"),
    path('livres',livre_views.livres, name="livres"),
    path('searchLivre', livre_views.searchLivre, name="search_livre"),
    path('meslivres', livre_views.meslivres, name="meslivres"),
    path('livres/emprunter/<int:livre_pk>/', livre_views.emprumter, name="livre_emprunter"),
    path('libraire',livre_views.libraire, name="libraire"),
    path('libraire/livres', livre_views.livre, name="libraire_livre"),
    path('libraire/livres/retard', livre_views.libraireLivresRetard, name="libraire_livres_retard"),
    path('libraire/livres/add', livre_views.addLivre, name="libraire_livre_add"),
    path('libraire/livres/delete/<int:livre_pk>/', livre_views.deleteLivre, name="libraire_livre_delete"),
    path('libraire/livre/rendre/<int:pret_pk>/', livre_views.libraireRendreLivre, name="rendre_livre"),
    path('libraire/bibliotheque', livre_views.bibliotheque, name="livraire_bibliotheque"),
    path('libraire/emprunts', livre_views.libraireEmprunt, name="libraire_emprunts"),
    path('libraire/emprunts/addtime/<int:pret_pk>/', livre_views.libraireEmpruntAddTime, name="libraire_emprunt_add_time"),
    path('admin/', admin.site.urls),
]
