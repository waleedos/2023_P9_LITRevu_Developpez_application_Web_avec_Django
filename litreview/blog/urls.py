# Importation des modules nécessaires.
from django.urls import path

from . import views  # Importation des vues de l'application.

# Définition des routes pour l'application.
urlpatterns = [

    path('flux/', views.flux_page, name='flux'),
    # Chemin pour le flux (page principale).

    path("Création d'un ticket/", views.create_ticket, name='create_ticket'),
    # Chemin pour créer un nouveau ticket.

    path("Création d'une critique/", views.create_review, name='review'),
    # Chemin pour créer une nouvelle critique sans spécifier un ticket.

    path("Création d'une critique/<int:ticket_id>/", views.review_answer, name='answer'),
    # Chemin pour créer une critique en réponse à un ticket spécifique.

    # Chemin pour voir les posts de l'utilisateur.
    path('Post/', views.post_page, name='post'),

    # Chemin pour modifier un ticket existant.
    path('Modifier ticket/<int:ticket_id>/', views.ticket_update, name='ticket_update'),

    # Chemin pour supprimer un ticket existant.
    path('Supprimer ticket/<int:ticket_id>/', views.ticket_delete, name='ticket_delete'),

    # Chemin pour gérer les abonnements.
    path('Abonnements/', views.subscript_page, name='subscrip'),

    # Chemin pour se désabonner d'un utilisateur.
    path('Désabonnement/<int:user_id>', views.follow_delete, name='unsubscrip'),

    # Chemin pour modifier une critique existante.
    path('Modifier critique/<int:review_id>/', views.review_update, name='review_update'),

    # Chemin pour supprimer une critique existante.
    path('Supprimer critique/<int:review_id>/', views.review_delete, name='review_delete'),
]
