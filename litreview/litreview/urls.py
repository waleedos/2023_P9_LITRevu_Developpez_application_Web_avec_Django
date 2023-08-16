# Importation de admin : Vous importez le module d'administration de Django pour pouvoir utiliser l'interface
# d'administration intégrée.
from django.contrib import admin

# Importations de path et include : path nous permet de définir des routes/URL pour votre application. Et include est
# utilisé pour inclure les configurations d'URL d'autres applications ou modules.
from django.urls import path, include

# Importation de settings : donc nous importons les paramètres de notre projet pour accéder aux variables définies dans
# settings.py.
from django.conf import settings

# Importation de static : Cette fonction est utilisée pour ajouter des URL pour servir des fichiers statiques en mode
# développement python.
from django.conf.urls.static import static


# La liste définit l'ensemble des URL pour votre projet.
urlpatterns = [

    # connecter l'interface d'administration de Django à l'URL /admin/.
    path('admin/', admin.site.urls),

    # Inclure toutes les URL définies dans le module authentication.urls.
    path("", include('authentication.urls')),

    # Inclure toutes les URL définies dans le module blog.urls.
    path("", include('blog.urls')),
]

# Lorsque nous sommes en mode développement (DEBUG = True dans settings.py), cette condition ajoute des URL
# pour servir des fichiers médias (comme les images téléchargées par les utilisateurs) directement depuis
# le serveur de développement de Django. Dans un environnement de production, les fichiers médias sont
# généralement servis par des solutions plus performantes comme NGINX ou Amazon S3, donc cette configuration
# est spécifique au mode développement.
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
