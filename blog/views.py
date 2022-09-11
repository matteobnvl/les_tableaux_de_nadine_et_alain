import datetime
from glob import escape
from shutil import register_unpack_format
from urllib.request import Request
from urllib.robotparser import RequestRate
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from .models import Peintre, Tableau, Commentaire, Type
from blog.forms import AddComments, FormAddType, FormTableau
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.


def index(request):
    num_tableau = Tableau.objects.all()
    tableau = Tableau.objects.filter(affichage=True).order_by('id')[:3]
    nombre_tableau = 0
    for affiche in num_tableau:
        if affiche.affichage == True:
            nombre_tableau += 1
    


    context = {
        'num_tableau' : nombre_tableau,
        'tableau' : tableau
    }

    return render(request, 'index.html', context=context)




def TableauListView(request):
    tableau = Tableau.objects.filter()
    peintre = Peintre.objects.filter()
    type = Type.objects.filter()
    


    context={
        'tableau':tableau,
        'peintre':peintre,
        'type':type
    }

    return render(request, 'blog/tableau_list.html' , context=context)


class PeintreListView(generic.ListView):
    model = Peintre


def TableauDetailView(request, pk):
    try:
        tableau = Tableau.objects.get(id=pk)
        form = AddComments()
    except Tableau.DoesNotExist:
        raise Http404("Le tableau n'existe pas")
    return render(request,'blog/tableau_detail.html',{'tableau':tableau, 'form':form})

def addComments(request, pk):
    personne = escape(request.POST.get('personne'))
    texte = escape(request.POST.get('texte'))
    date = datetime.datetime.now().date()
    tableau = Tableau.objects.get(id=pk)

    commentaire = Commentaire(personne=personne, texte=texte, date_publication=date, tableau=tableau)

    commentaire.save()


    return render(request, 'comments/comments.html', context={'commentaire' : commentaire})

@login_required
def MonCompte(request):
    return render(request, 'registration/compte.html')


def Connexion(request):
    return render(request, 'registration/connexion.html')

@login_required
def AdministrationSite(request):
    tableau = Tableau.objects.all()

    return render(request,'registration/administration.html', {'tableau':tableau})


@csrf_exempt
@login_required
def CreateTableau(request):
    form = FormTableau()
    form_type = FormAddType()
    if request.method == 'POST':
        form = FormTableau(request.POST, request.FILES)
        if form.is_valid():
            tableau = form.save(commit=False)
            peintre = Peintre.objects.get(pk=request.POST.get('peintre'))
            tableau.peintre = peintre
            tableau.save()
            redirect('administration')

    peintre = Peintre.objects.all()
    context = {
        'peintre':peintre,
        'form':form,
        'form_type':form_type
    }
    return render(request, 'registration/ajout_tableau.html', context=context)


@csrf_exempt
@login_required
def UpdateTableau(request, pk):
    try:
        tableau = Tableau.objects.get(id=pk)
        
        if request.method == 'POST':
            form = FormTableau(request.POST,request.FILES, instance=tableau)
            if form.is_valid():
                print(request.FILES)
                tableau = form.save(commit=False)
                peintre = Peintre.objects.get(pk=request.POST.get('peintre'))
                tableau.peintre = peintre
                tableau.save()
                return redirect('administration')
        else:
            form = FormTableau(instance=tableau)

        context = {
                'form':form,
            }

    except Tableau.DoesNotExist:
        raise Http404("Le tableau n'existe pas")
    return render(request,'registration/modifier_tableau.html',context=context)



def SearchTableau(request):
    name_tableau = escape(request.POST.get('recherche'))
    tableau = Tableau.objects.filter(nom_tableau__icontains = name_tableau)
    return render(request, 'comments/searchTableau.html', context={'tableau':tableau})

def FiltreTableau(request):
    peintre = escape(request.POST.get('peintre'))
    type = escape(request.POST.get('type'))
    date = escape(request.POST.get('date'))

    if peintre == "" and type == "":
        if date == 'date-r':
            tableau = Tableau.objects.filter()
        else:
            tableau = Tableau.objects.filter()
    elif peintre == "" and type != "":
        tableau = Tableau.objects.filter(type = type)
    elif peintre != "" and type == "":
        tableau = Tableau.objects.filter(peintre = peintre)
    else:
        tableau = Tableau.objects.filter(peintre = peintre, type = type)
        
    return render(request, 'comments/searchTableau.html', context={'tableau':tableau})



    



@csrf_exempt
@login_required
def AddType(request):
    type_nom = escape(request.POST.get('type_nom'))
    type = Type(type_nom=type_nom)
    type.save()
    return redirect('ajouter-tableau')


def page_not_found_view(request):
    return render(request,'404.html', context={})