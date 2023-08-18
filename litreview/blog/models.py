# Importation des modules nécessaires.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image  # Bibliothèque pour traiter les images.


# Classe de base pour tous les modèles.
class BaseModel(models.Model):
    objects = models.Manager()  # Manager par défaut pour le modèle.

    class Meta:
        abstract = True  # Indique que ce modèle est abstrait et ne doit pas être créé dans la base de données.


# Modèle pour les tickets.
class Ticket(BaseModel):
    title = models.CharField(max_length=128, verbose_name="Titre")  # Champ pour le titre du ticket.
    description = models.TextField(max_length=2048, blank=True)  # Champ pour la description du ticket.
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="utilisateur")

    # Lien vers l'utilisateur qui a créé le ticket.
    image = models.ImageField(null=True, blank=True)  # Champ pour l'image associée au ticket.

    time_created = models.DateTimeField(auto_now_add=True, verbose_name="date de création")
    # Date et heure de création du ticket.

    class Meta:
        verbose_name = 'Demande de critique'  # Nom convivial pour le modèle dans l'interface d'administration.

    IMAGE_MAX_SIZE = (200, 200)  # Taille maximale de l'image.

    # Méthode pour redimensionner l'image.
    def resize_image(self):
        image = Image.open(self.image)  # Ouvre l'image.
        image.thumbnail(self.IMAGE_MAX_SIZE)  # Redimensionne l'image.
        image.save(self.image.path)  # Sauvegarde l'image redimensionnée.

    # Méthode pour sauvegarder le modèle.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Appelle la méthode save() de la classe parent.
        self.resize_image()  # Redimensionne l'image après avoir sauvegardé.

    # Méthode pour afficher le modèle sous forme de chaîne.
    def __str__(self):
        return self.title  # Retourne le titre du ticket.


# Modèle pour les critiques.
class Review(BaseModel):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name="reviews")
    # Lien vers le ticket associé.

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note"
    )  # Champ pour la note de la critique.
    headline = models.CharField(max_length=128, verbose_name="Titre")  # Titre de la critique.
    body = models.CharField(max_length=8192, blank=True)  # Corps de la critique.
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Utilisateur")
    # Lien vers l'utilisateur qui a créé la critique.

    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    # Date et heure de création de la critique.

    class Meta:
        verbose_name = 'critique'  # Nom convivial pour le modèle.
        verbose_name_plural = 'critiques'  # Forme plurielle du nom.

    # Méthode pour afficher le modèle sous forme de chaîne.
    def __str__(self):
        return self.headline  # Retourne le titre de la critique.


# Modèle pour suivre d'autres utilisateurs.
class UserFollows(BaseModel):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following",
                             verbose_name="Utilisateur")  # Lien vers l'utilisateur qui suit.
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followed_by",
                                      verbose_name="Utilisateur suivi")  # Lien vers l'utilisateur suivi.

    class Meta:
        unique_together = ('user', 'followed_user', )
        # Assure que chaque combinaison d'utilisateur et d'utilisateur suivi est unique.

        verbose_name = 'Suivi des utilisateurs'
        # Nom convivial pour le modèle.
