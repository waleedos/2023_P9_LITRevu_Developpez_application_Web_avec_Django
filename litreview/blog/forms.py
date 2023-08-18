# Importation des modules nécessaires.
from django import forms
from . import models

# Formulaires pour l'application.


# Définition du formulaire pour la création/modification des tickets.
class TicketForm(forms.ModelForm):
    # Définition du champ `title` avec un style et un placeholder personnalisés.
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"style": "width: 100%;", "placeholder": "Titre"})
    )
    # Zone de texte pour la description du ticket.
    description = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={"style": "width: 100%;", "rows": 5, "placeholder": "Description"})
    )
    # Champ pour le téléchargement d'une image.
    image = forms.ImageField(
        label="",
        widget=forms.FileInput()
    )

    # Classe Meta définissant le modèle sur lequel ce formulaire est basé et les champs à inclure.
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


# Formulaires pour suivre d'autres utilisateurs.
class UserFollowing(forms.Form):
    # Champ de texte pour entrer le nom d'utilisateur à suivre.
    followed_user = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'text-center', "style": "width: 100%;", "placeholder": "Nom d'utilisateur"})
    )


# Formulaires pour la création/modification des critiques.
class ReviewForm(forms.ModelForm):
    # Définition des choix possibles pour la note.
    CHOICES = [
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    # Champ pour le titre de la critique.
    headline = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"style": "width: 100%;", "placeholder": "Titre"})
    )
    # Champ de choix pour la note de la critique.
    rating = forms.ChoiceField(
        label='Note',
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    # Zone de texte pour le contenu de la critique.
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={"style": "width: 100%;", "rows": 5, "placeholder": "Commentaire"})
    )

    # Classe Meta définissant le modèle sur lequel ce formulaire est basé et les champs à inclure.
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
