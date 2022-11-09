from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza  # on récupère notre modèle Pizza

# Create your views here.


# accès par /menu
def index(request):
    '''pizzas = Pizza.objects.all()  # récupère tous les objets de la classe Pizza
    pizza_name_and_price = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizza_name_and_price_str = ", ". join(pizza_name_and_price)
    return HttpResponse("Les pizzas : " + pizza_name_and_price_str)'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, "menu/index.html", {'pizzas': pizzas})
