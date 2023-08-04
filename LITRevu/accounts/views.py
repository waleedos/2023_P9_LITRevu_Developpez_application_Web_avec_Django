from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.shortcuts import render
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class LogInView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogOutView(auth_views.LogoutView):
    template_name = 'accounts/logout.html'


class AccountsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/accounts.html')
