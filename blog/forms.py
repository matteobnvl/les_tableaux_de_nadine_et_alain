from django import forms
from blog.models import Tableau


class AddComments(forms.Form):
    personne = forms.CharField(max_length=50, required=True)
    texte = forms.CharField(widget=forms.Textarea, required=True)

class FormTableau(forms.ModelForm):
    class Meta:
        model = Tableau
        fields = ['nom_tableau', 'description','longueur','largeur','date_debut','date_fin','type','photo','peintre','affichage']


class FormAddType(forms.Form):
    type_nom = forms.CharField(max_length=100, required=True)
