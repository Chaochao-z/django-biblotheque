from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.models import Groupe_Lecture, GL_User, Biliotheque
from .form import Goupe_lecture_form
import pytz


# Create your views here.
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraireIndex(request):
    context ={}
    context['groupes'] = Groupe_Lecture.objects.order_by('-date')
    return render(request, 'libraire/groupe-lecture.html', context=context)

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraireAddGl(request):
    form = Goupe_lecture_form()
    if request.method == "POST":
        form = Goupe_lecture_form(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le Groupe de lecture a bien été crée")
            return redirect('libraire_gl')
        else: messages.error(request, form.errors)
    return render(request, 'libraire/gl-add.html', {'form':form})

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def libraireDeleteGl(request, groupe_pk):
    gl = Groupe_Lecture.objects.get(id=groupe_pk)
    gl.delete()
    messages.success(request,"Goupe de lecture a bien été supprimer")
    return redirect('libraire_gl')


def index(request):
    context = {}
    now = datetime.now()
    context["meslectures"] = GL_User.objects.filter(user_id=request.user.pk)
    context["exist"] = True
    context["todaynow"] = now.replace(tzinfo=pytz.utc)
    context['groupes'] = Groupe_Lecture.objects.order_by('-date')
    return render(request, 'groupe-lecture/index.html', context=context)

@login_required()
def gl_participate(request, groupe_pk):
    if GL_User.objects.filter(user_id=request.user.pk, groupe_lecture_id=groupe_pk):
        messages.error(request, "Vous etes deja inscrit")
        return redirect('groupe-lecture')
    GL_User.objects.create(user_id=request.user.pk, groupe_lecture_id=groupe_pk)
    messages.success(request,"Vous avez bien inscrit")
    return redirect('groupe-lecture')

@login_required()
def mesgroupelecture(request):
    context = {}
    context['participates'] = GL_User.objects.filter(user_id=request.user.pk)
    return render(request, 'groupe-lecture/meslecture.html', context=context)