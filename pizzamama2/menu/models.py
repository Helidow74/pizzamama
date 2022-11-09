from django.db import models
from django.db.models import ForeignKey

# Create your models here.


# on définit tous les champs en leur attribuant une catégorie de field. Pour un CharField, il faut obligatoirement
# indiquer un nombre de caractères.


class Category(models.Model):
    nom = models.CharField(max_length=200)
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):   # permet de renvoyer le nom de la cat dans l'affichage admin
        return self.nom


class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    description = models.TextField(default=" ")
    category = ForeignKey(Category, related_name="Categorie", on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.nom
