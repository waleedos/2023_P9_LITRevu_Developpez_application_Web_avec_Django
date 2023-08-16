from django.urls import path

from . import views


urlpatterns = [
    path('flux/', views.flux_page, name='flux'),
    path("Création d'un ticket/", views.create_ticket, name='create_ticket'),
    path("Création d'une critique/", views.create_review, name='review'),
    path("Création d'une critique/<int:ticket_id>/", views.review_answer, name='answer'),
    path('Post/', views.post_page, name='post'),
    path('Modifier ticket/<int:ticket_id>/', views.ticket_update, name='ticket_update'),
    path('Supprimer ticket/<int:ticket_id>/', views.ticket_delete, name='ticket_delete'),
    path('Abonnements/', views.subscript_page, name='subscrip'),
    path('Désabonnement/<int:user_id>', views.follow_delete, name='unsubscrip'),
    path('Modifier critique/<int:review_id>/', views.review_update, name='review_update'),
    path('Supprimer critique/<int:review_id>/', views.review_delete, name='review_delete'),

]
