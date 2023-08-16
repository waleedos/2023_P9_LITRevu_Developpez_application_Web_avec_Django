
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models

from PIL import Image


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Ticket(BaseModel):
    title = models.CharField(max_length=128, verbose_name="Titre")
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="utilisateur")
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="date de création")

    class Meta:
        verbose_name = 'Demande de critique'

    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return self.title


class Review(BaseModel):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note"
    )
    headline = models.CharField(max_length=128, verbose_name="Titre")
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Utilisateur")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    class Meta:
        verbose_name = 'critique'
        verbose_name_plural = 'critiques'

    def __str__(self):
        return self.headline


class UserFollows(BaseModel):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following",
                             verbose_name="Utilisateur")
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followed_by",
                                      verbose_name="Utilisateur suivi")

    class Meta:
        unique_together = ('user', 'followed_user', )
        verbose_name = 'Suivi des utilisateurs'
