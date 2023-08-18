# Powered By M. EL-WALID EL-KHABOU
from django.urls import path
# Importation de path qui est une fonction Django utilisée pour définir les routes (URL) de l'application.

from . import views
# Importation des vues : Importe toutes les fonctions de vue du module views.py de l'application courante
# (indiquée par le point .).

urlpatterns = [
    # Définition des URL : La variable urlpatterns est une liste qui définit toutes les routes pour cette application.

    path("", views.login_page, name='home'),
    # Route de la page de connexion : Si l'utilisateur visite l'URL de base de l'application (par exemple,
    # http://example.com/), il sera redirigé vers la fonction de vue login_page définie dans views.py. La route
    # est également nommée "home", ce qui permet de référencer facilement cette URL ailleurs dans le code (par exemple,
    # dans les modèles).

    path('Inscription/', views.signup_page, name='signup'),
    # Route de la page d'inscription : Si l'utilisateur visite l'URL http://example.com/Inscription/, il sera redirigé
    # vers la fonction de vue signup_page. La route est nommée "signup".

    path('Déconnexion/', views.logout_page, name='logout'),
    # Route de déconnexion : Si l'utilisateur visite l'URL http://example.com/Déconnexion/, il sera redirigé vers la
    # fonction de vue logout_page. La route est nommée "logout".
]
