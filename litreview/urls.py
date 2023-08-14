""" Ce fichier urls.py constitue la base de la configuration des URL de votre projet. Il dirige les requêtes entrantes
vers les bonnes vues en fonction de l'URL demandée, en agissant comme un routeur pour votre application. """

# Importation des paramètres de configuration de Django, nous permettant d'accéder à des variables telles que DEBUG,
# MEDIA_URL, etc.
from django.conf import settings

# Importation de la fonction utilisée pour ajouter les URL pour servir les fichiers statiques et médias en mode de
# développement.
from django.conf.urls.static import static

# Importation de l'interface d'administration de Django.
from django.contrib import admin

# Importation des fonctions utilisées pour définir les chemins d'URL et inclure d'autres fichiers URL.
from django.urls import path, include


# Liste des chemins d'URL pour votre projet.
urlpatterns = [
    # Dirige toutes les URL commençant par admin/ vers l'interface d'administration de Django.
    path('admin/', admin.site.urls),

    # Inclut les fichiers URL des différentes applications de votre projet. L'argument vide '' signifie que ces URL
    # seront ajoutées à la racine.
    path('', include('authentication.urls')),
    path('', include('ticketing.urls')),
    path('', include('subscription.urls')),
]


# Ce bloc ajoute des URL pour servir les fichiers médias directement à partir de Django lorsque nous sommes en mode
# de débogage (DEBUG = True). Ceci est utile en développement mais ne doit pas être utilisé en production.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
