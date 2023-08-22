"""
Django settings for litreview project.

Generated by 'django-admin startproject' using Django 4.2.4

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Importations des deux modules Path de pathlib pour manipuler les chemins d'une manière indépendante de la plateforme,
# et le module os pour interagir avec le système d'exploitation.

BASE_DIR = Path(__file__).resolve().parent.parent
# Parametrage de la variable BASE_DIR qui détermine le répertoire de base de notre projet. Il est utilisé pour
# construire des chemins relatifs pour d'autres configurations.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rbe!i)gyrdbk0(#xo96(06$wf*1tw7b1kk!co3l7v1sg@@dsn7'
# clé unique et secrète utilisée par Django pour diverses tâches cryptographiques. Pour des raisons de sécurité, cette
# clé doit rester secrète et être unique pour chaque installation de Django.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True,
# Cette variable détermine si le mode de débogage est activé. En production, cette valeur doit être mise à False pour
# des raisons de sécurité.

ALLOWED_HOSTS = []
# Liste des hôtes/domains autorisés à servir cette application. En production, vous devez ajouter les domaines de notre
# application à cette liste.


# Application definition
# Liste des applications installées. Ces applications peuvent être des applications intégrées à Django
# (comme django.contrib.admin) ou des applications que vous avez créées ou installées (comme authentication ou blog).
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authentication',
    'blog',
    'django_extensions',
]

# Liste des middlewares installés. Les middlewares sont des classes qui traitent les requêtes et les réponses à
# différents stades de leur traitement.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Le module qui contient les configurations d'URL de niveau supérieur pour votre projet.
ROOT_URLCONF = 'litreview.urls'

# Configuration pour le chargement et le rendu des templates.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath("templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Le chemin d'accès à l'application WSGI utilisée par les serveurs WSGI pour servir votre application.
WSGI_APPLICATION = 'litreview.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# Configuration de la base de données. Ici, vous utilisez SQLite comme base de données, qui est une base de données
# basée sur des fichiers.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
# Liste des validateurs de mots de passe pour l'authentification des utilisateurs.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Paramètres d'internationalisation : Ces paramètres définissent le code de langue, le fuseau horaire, et d'autres
# configurations liées à la localisation et à l'internationalisation.
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True


# L'URL utilisée pour servir les fichiers statiques. (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# Le type de champ utilisé pour les clés primaires auto-incrémentées.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Le modèle personnalisé utilisé pour la gestion des utilisateurs.
AUTH_USER_MODEL = 'authentication.User'

# L'URL à laquelle les utilisateurs non authentifiés seront redirigés lorsqu'une vue nécessitant une authentification
# est demandée.
LOGIN_URL = 'home'

# MEDIA_URL est l'URL de base pour servir les fichiers média. MEDIA_ROOT est le répertoire sur le système de fichiers où
# ces fichiers sont stockés.
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
