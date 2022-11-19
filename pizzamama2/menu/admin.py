from django.contrib import admin
from .models import Pizza, Category


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix', 'category', 'image')
    search_help_text = "Rechercher par nom de pizza"
    search_fields = ['nom']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_ajout')


# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Category, CategoryAdmin)
