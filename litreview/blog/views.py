from itertools import chain
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from authentication.models import User
from blog import forms
from blog.models import UserFollows, Review, Ticket


# Décorateur pour vérifier si un utilisateur est connecté.
@login_required
def flux_page(request):
    """Retourne le flux d'actualités (tickets et critiques).

    Affiche les tickets et critiques de l'utilisateur connecté et de ceux qu'il suit.
    """
    # Récupération des utilisateurs suivis.
    followed_users = [x.followed_user for x in UserFollows.objects.filter(user=request.user)]
    # Récupération des tickets de l'utilisateur et de ceux qu'il suit.
    tickets = Ticket.objects.filter(Q(user__in=followed_users) | Q(user=request.user))
    # Récupération des critiques de l'utilisateur et de celles liées à ses tickets.
    reviews = Review.objects.filter(Q(user__in=followed_users) | Q(user=request.user) | Q(ticket__user=request.user))

    # Fusion et tri des critiques et tickets.
    reviews_and_tickets = sorted(
        chain(reviews, tickets),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    # Mise en place de la pagination.
    paginator = Paginator(reviews_and_tickets, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'blog/flux.html', context=context)


@login_required
def post_page(request):
    """Retourne la page des publications de l'utilisateur."""
    # Récupération des critiques et tickets de l'utilisateur.
    reviews = Review.objects.filter(user=request.user)
    tickets = Ticket.objects.filter(user=request.user)

    # Fusion et tri des critiques et tickets.
    reviews_and_tickets = sorted(
        chain(reviews, tickets),
        key=lambda instance: instance.time_created,
        reverse=True
    )

    # Mise en place de la pagination.
    paginator = Paginator(reviews_and_tickets, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'blog/post.html', context=context)


@login_required
def ticket_update(request, ticket_id):
    """Modifie un ticket existant."""
    # Récupération du ticket à partir de son ID.
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = forms.TicketForm(instance=ticket)
    context = {
        'form': form,
        'ticket': ticket,
    }
    return render(request, 'blog/ticket_update.html', context=context)


@login_required
def ticket_delete(request, ticket_id):
    """Supprime un ticket existant."""
    # Récupération du ticket à partir de son ID.
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('post')
    return render(request, 'blog/ticket_delete.html', context={'ticket': ticket})


@login_required
def review_update(request, review_id):
    """Modifie une critique existante."""
    # Récupération de la critique à partir de son ID.
    review = Review.objects.get(id=review_id)
    # Récupération du ticket associé à la critique.
    ticket = review.ticket
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = forms.ReviewForm(instance=review)

    context = {
        'form': form,
        'ticket': ticket,
    }
    return render(request, 'blog/review_update.html', context=context)


@login_required
def review_delete(request, review_id):
    """Supprime une critique existante."""
    # Récupération de la critique à partir de son ID.
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('post')
    return render(request, 'blog/review_delete.html', context={'review': review})


@login_required
def subscript_page(request):
    """Gère la page des abonnements."""
    # Initialisation du message d'erreur ou de confirmation.
    message = ""
    # Initialisation du formulaire d'abonnement.
    form = forms.UserFollowing()
    # Récupération des utilisateurs suivis et des abonnés.
    followed_users = [x.followed_user for x in UserFollows.objects.filter(user=request.user)]
    followers = [x.user for x in UserFollows.objects.filter(followed_user=request.user)]

    # Traitement du formulaire d'abonnement.
    if request.method == 'POST':
        form = forms.UserFollowing(request.POST)
        if form.is_valid():
            followed_user_id = form.cleaned_data.get("followed_user")
            try:
                # Vérification de l'existence de l'utilisateur choisi.
                followed_user = User.objects.get_by_natural_key(followed_user_id)
            except User.DoesNotExist as e:
                e = "Cet utilisateur n'existe pas"
                context = {
                    'form': form,
                    'followed_users': followed_users,
                    'followers': followers,
                    'user': request.user,
                    "error": e,
                }
                return render(request, 'blog/subscrip.html', context=context)
            # Vérification si l'utilisateur est déjà suivi.
            if followed_user in followed_users:
                message = "Cet utilisateur est déja suivi."
                context = {
                    'form': form,
                    'followed_users': followed_users,
                    'followers': followers,
                    'user': request.user,
                    "message": message
                }
                return render(request, 'blog/subscrip.html', context=context)
            # Vérification si l'utilisateur tente de se suivre lui-même.
            elif followed_user == request.user:
                message = "Vous ne pouvez pas vous suivre."
                context = {
                    'form': form,
                    'followed_users': followed_users,
                    'followers': followers,
                    'user': request.user,
                    "message": message
                }
                return render(request, 'blog/subscrip.html', context=context)
            # Sinon, ajout de l'abonnement.
            else:
                UserFollows(
                    followed_user=followed_user, user=request.user).save()
            return redirect('subscrip')
    context = {
            'form': form,
            'followed_users': followed_users,
            'followers': followers,
            'user': request.user,
            'message': message
        }
    return render(request, 'blog/subscrip.html', context=context)


@login_required
def follow_delete(request, user_id):
    """Supprime un abonnement."""
    # Récupération de l'abonnement à partir de son ID.
    follow = UserFollows.objects.get(Q(followed_user=user_id) & Q(user=request.user))
    if request.method == 'POST':
        follow.delete()
        return redirect('subscrip')
    return render(request, 'blog/follow_remove.html', context={'follow': follow})


@login_required
def create_ticket(request):
    """Crée une demande de critique."""
    # Initialisation du formulaire de demande de critique.
    form = forms.TicketForm()
    # Traitement du formulaire.
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'blog/create_ticket.html', context=context)


@login_required
def create_review(request):
    """Crée une demande de critique et une critique."""
    # Initialisation des formulaires.
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    # Traitement des formulaires.
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('flux')
    context = {
            'ticket_form': ticket_form,
            'review_form': review_form,
            'user': request.user,
    }
    return render(request, 'blog/review.html', context=context)


@login_required
def review_answer(request, ticket_id):
    """Crée une critique en réponse à une demande de critique."""
    # Récupération de la demande de critique à partir de son ID.
    ticket = Ticket.objects.get(id=ticket_id)
    # Initialisation du formulaire de critique.
    review_form = forms.ReviewForm()
    # Traitement du formulaire.
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('flux')
    context = {
        'ticket': ticket,
        'review_form': review_form,
        'user': request.user
    }
    return render(request, 'blog/review_answer.html', context=context)
