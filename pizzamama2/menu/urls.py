from django.urls import path
from . import views  # on importe les vues

app_name = 'menu'

urlpatterns = [
    path('', views.index, name="index"),  # vue index qu'on affiche pour une url par défaut
    path('pizzas_traditionnelles', views.pizzasTrad, name="pizzas_traditionnelles"),
    path('pizzas_a_la_creme', views.pizzasCreme, name="pizzas_a_la_creme"),
    path('pizzas_de_la_mer', views.pizzasMer, name="pizzas_de_la_mer"),
    path('pizzas_exclusives', views.pizzasExclusives, name="pizzas_exclusives"),
    path('pizzas_vegetariennes', views.pizzasVegetariennes, name="pizzas_vegetariennes"),
]
