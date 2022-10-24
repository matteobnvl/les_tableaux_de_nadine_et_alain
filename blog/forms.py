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

class formContact(forms.Form):
    Nom = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Votre nom'}))
    Prenom = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Votre prénom'}))
    Email = forms.EmailField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Votre Email'}))
    Message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Votre message'}), max_length=2000, required=True)


