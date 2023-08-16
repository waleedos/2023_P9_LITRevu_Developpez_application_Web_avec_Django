# Powered By M. EL-WALID EL-KHABOU
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from . import forms


def logout_page(request):
    """Function allowing the disconnection of a user.
    After disconnection, the user is redirected to the login page
    """
    logout(request)
    return redirect('home')


def login_page(request):
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
