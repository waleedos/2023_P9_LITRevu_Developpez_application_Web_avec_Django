"""
WSGI config for litreview project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# Importation du module os qui nous permet d'interagir avec le système d'exploitation. Ici, il est utilisé
# principalement pour définir une variable d'environnement.
import os

# Importation de get_wsgi_application : Cette fonction retourne une instance de l'application WSGI de Django, qui est le
# point d'entrée standard pour les serveurs WSGI pour servir votre application Django.
from django.core.wsgi import get_wsgi_application

# Définition de la variable d'environnement DJANGO_SETTINGS_MODULE : Cette ligne définit la variable d'environnement
# pour indiquer à Django où trouver les paramètres de l'application. Si cette variable n'est pas déjà définie, elle est
# fixée à 'litreview.settings'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litreview.settings')

# Création de l'application WSGI : Cette ligne crée une instance de l'application WSGI pour votre projet Django. Cette
# instance est utilisée par les serveurs WSGI pour gérer les requêtes HTTP entrantes.
application = get_wsgi_application()
