"""
ASGI config for litreview project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
# Importation de os : Ce module permet d'interagir avec le système d'exploitation, et il est utilisé ici pour définir
# des variables d'environnement.

from django.core.asgi import get_asgi_application
# Importation de get_asgi_application : Cette fonction renvoie une application ASGI pour votre projet Django, qui sera
# le point d'entrée pour le serveur ASGI.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litreview.settings')
# Définition de la variable d'environnement : Cela définit la variable d'environnement DJANGO_SETTINGS_MODULE pour
# indiquer à Django où trouver les paramètres pour cette instance de l'application. Si cette variable n'est pas déjà
# définie, elle sera fixée à 'litreview.settings'.

application = get_asgi_application()
# Création de l'application ASGI : Cette ligne crée une instance de l'application ASGI à l'aide des paramètres définis
# précédemment. Cette instance sera utilisée par le serveur ASGI pour traiter les requêtes HTTP entrantes.
