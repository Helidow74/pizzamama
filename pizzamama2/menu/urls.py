from django.urls import path
from . import views  # on importe les vues

app_name = 'menu'

urlpatterns = [
    path('', views.index, name="index"),  # vue index qu'on affiche pour une url par défaut
]
