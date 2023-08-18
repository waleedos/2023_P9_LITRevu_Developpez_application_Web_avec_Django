# Powered By M. EL-WALID EL-KHABOU
from django.contrib.auth import authenticate, login, logout
# Importation des méthodes d'authentification ou des 'fonctions) : authenticate pour la validation des identifiants d'un
# utilisateur, login : Cette fonction connecte un utilisateur et logout : Cette fonction déconnecte un utilisateur.

from django.shortcuts import redirect, render
# Importation des fonctions utilitaires : redirect qui Renvoie une réponse HTTP qui redirige le navigateur vers une URL
# spécifique, et render : Renvoie une réponse HTTP avec le contenu rendu d'un modèle spécifié.

from . import forms
# Importation des formulaires : Importe les formulaires définis dans le module forms de l'application actuelle.


def logout_page(request):
    # Vue logout_page : Cette fonction déconnecte un utilisateur et le redirige vers la page d'accueil.
    """Function allowing the disconnection of a user.
    After disconnection, the user is redirected to the login page
    """
    logout(request)
    return redirect('home')


def login_page(request):
    # Vue login_page : Cette fonction gère la logique de connexion pour un utilisateur. Si la méthode de la requête est
    # POST, elle vérifie les identifiants. Si les identifiants sont valides, l'utilisateur est connecté et redirigé vers
    # la page flux. Sinon, un message d'erreur est affiché.
    """his function allows a registered user to log in.
    After verifying his credentials, the user is redirected to the feed page if they are correct.
    """
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect('flux')
            else:
                message = "Identifiants invalides."
    return render(request, "authentication/login.html", context={"form": form, "message": message})


def signup_page(request):
    # Vue signup_page : Cette fonction gère l'inscription d'un nouvel utilisateur. Si la méthode de la requête est POST
    # et que le formulaire est valide, un nouvel utilisateur est créé, connecté, et redirigé vers la page flux.
    """This function allows the registration of a new user.
    After entering his credentials, the user is redirected to the feed page.
    """
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flux')

    return render(request, "authentication/signup.html", context={"form": form})
