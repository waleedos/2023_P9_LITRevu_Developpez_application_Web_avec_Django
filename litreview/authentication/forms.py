# Powered By M. EL-WALID EL-KHABOU

from django import forms
# Importation du module forms de Django, qui contient des utilitaires et des classes pour créer des formulaires.

from django.contrib.auth import get_user_model
# Importation de la fonction get_user_model qui retourne le modèle utilisateur actuellement actif dans ce projet. Ce
# modèle est utilisé pour référencer le modèle utilisateur sans avoir à nommer le modèle utilisateur directement.

from django.contrib.auth.forms import UserCreationForm
# Importation de UserCreationForm qui est un formulaire intégré fourni par Django pour la création de nouveaux
# utilisateurs.


# Définition du LoginForm qui est le formulaire pour la connexion des utilisateurs.
class LoginForm(forms.Form):

    # Définition de deux Champs du formulaire de connexion: username et password. Les attributs label et widget sont
    # utilisés pour personnaliser le rendu et le comportement des champs dans le formulaire.
    username = forms.CharField(max_length=60, label="",
                               widget=forms.TextInput(attrs={"class": "user_name", "placeholder": "Nom d'utilisateur",
                                                             "size": 40}))
    password = forms.CharField(max_length=60, label="",
                               widget=forms.PasswordInput(attrs={"class": "pwd", "placeholder": "Mot de passe",
                                                                 "size": 40}))


# Définition du SignupForm : Nous définissons un formulaire pour l'inscription des utilisateurs, qui hérite de
# UserCreationForm.
class SignupForm(UserCreationForm):

    # Champs du formulaire d'inscription : Nous redéfinisson les champs username, password1 (mot de passe) et password2
    # (confirmation du mot de passe) pour personnaliser leur rendu. Comme pour le LoginForm, nous utilisons les attributs
    # label et widget pour cela.
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "text-center",
                                                                       "placeholder": "Nom d'utilisateur", "size": 60}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "text-center",
                                                                            "placeholder": "Mot de passe", "size": 60}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "text-center",
                                                                            "placeholder": "Confirmer mot de passe",
                                                                            "size": 60}))

    # Classe Meta interne : Cette classe est utilisée pour fournir des métadonnées supplémentaires au formulaire. Dans
    # le cas de SignupForm, il fournit des informations sur le modèle associé au formulaire.
    class Meta(UserCreationForm.Meta):

        # Définition du modèle pour le formulaire : Vous indiquez que ce formulaire est associé au modèle utilisateur
        # actif du projet.

        model = get_user_model()
