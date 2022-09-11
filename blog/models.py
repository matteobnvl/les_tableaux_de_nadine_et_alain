from pyexpat import model
from statistics import mode
from django.db import models
from django.urls import reverse

# Create your models here.


class Tableau(models.Model):
    """ Model représentabnt les tableaux"""
    nom_tableau = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    longueur = models.CharField(max_length=50)
    largeur = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='images/')
    peintre = models.ForeignKey('Peintre', on_delete=models.SET_NULL, null=True)
    meilleur_realisation = models.CharField(max_length=10)
    affichage = models.BooleanField()

    def __str__(self):
        return self.nom_tableau

    def get_absolute_url(self):
        return reverse("tableau-detail", args=[str(self.id)])

class Type(models.Model):
    """ Model représentant les types de peinture """
    type_nom = models.CharField(max_length=100)

    def __str__(self):
        return self.type_nom
    



class Peintre(models.Model):
    """ Model représentant les peintres"""
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    description_peintre = models.CharField(max_length=250)
    
    class Meta:
        ordering = ['nom', 'prenom']

    def get_absolute_url(self):
        return reverse("peintre-detail", args=[str(self.id)])
    
    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Commentaire(models.Model):
    """ Model représentant les commentaires sur les tableaux """

    personne = models.CharField(max_length=50)
    texte = models.TextField(null=True)
    date_publication = models.DateField(null=True)
    tableau = models.ForeignKey('Tableau', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.personne} {self.tableau}'
    