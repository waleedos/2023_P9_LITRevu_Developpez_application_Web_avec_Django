"""
WSGI config for litreview project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/

Ce fichier est généralement utilisé dans un contexte de déploiement, où vous configurez un serveur WSGI comme
Gunicorn ou uWSGI pour servir votre application Django. Il configure l'environnement et crée l'application WSGI qui
gère les requêtes HTTP entrantes.
"""

# Importation du module os, qui permet d'interagir avec le système d'exploitation. Utilisé ici pour définir les
# variables d'environnement.
import os

# Importation de la fonction qui renvoie une application WSGI pour notre projet. Ceci est le point d'entrée pour
# le serveur WSGI.
from django.core.wsgi import get_wsgi_application

# Définition de la variable d'environnement DJANGO_SETTINGS_MODULE au module de paramètres de votre projet. Ceci
# indique à Django où trouver les paramètres pour cette instance de l'application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litreview.settings')

# Création d'une instance de l'application WSGI en utilisant les paramètres définis précédemment. Cette instance sera
# utilisée par le serveur WSGI pour servir votre application.
application = get_wsgi_application()
