# Powered By M. EL-WALID EL-KHABOU
from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_page, name='home'),
    path('Inscription/', views.signup_page, name='signup'),
    path('Déconnexion/', views.logout_page, name='logout'),

]
