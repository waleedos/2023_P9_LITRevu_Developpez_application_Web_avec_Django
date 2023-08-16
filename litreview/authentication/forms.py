# Powered By M. EL-WALID EL-KHABOU
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label="",
                               widget=forms.TextInput(attrs={"class": "user_name", "placeholder": "Nom d'utilisateur",
                                                             "size": 40}))
    password = forms.CharField(max_length=60, label="",
                               widget=forms.PasswordInput(attrs={"class": "pwd", "placeholder": "Mot de passe",
                                                                 "size": 40}))


class SignupForm(UserCreationForm):

    username = forms.CharField(label="", widget=forms.TextInput(attrs={"class": "text-center",
                                                                       "placeholder": "Nom d'utilisateur", "size": 60}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "text-center",
                                                                            "placeholder": "Mot de passe", "size": 60}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class": "text-center",
                                                                            "placeholder": "Confirmer mot de passe",
                                                                            "size": 60}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

