from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Category  # on récupère notre modèle Pizza

# Create your views here.


# accès par /menu
def index(request):
    '''pizzas = Pizza.objects.all()  # récupère tous les objets de la classe Pizza
    pizza_name_and_price = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizza_name_and_price_str = ", ". join(pizza_name_and_price)
    return HttpResponse("Les pizzas : " + pizza_name_and_price_str)'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, "menu/index.html", {'pizzas': pizzas})


def pizzasTrad(request):
    pizzas = Pizza.objects.filter(category__in=Category.objects.filter(nom="Pizzas traditionnelles")).distinct().order_by('prix')
    return render(request, "menu/pizzas_traditionnelles.html", {'pizzas': pizzas})


def pizzasCreme(request):
    pizzas = Pizza.objects.filter(category__in=Category.objects.filter(nom="Pizzas crème")).distinct().order_by('prix')
    return render(request, "menu/pizzas_a_la_creme.html", {'pizzas': pizzas})


def pizzasMer(request):
    pizzas = Pizza.objects.filter(category__in=Category.objects.filter(nom="Pizzas de la mer")).distinct().order_by('prix')
    return render(request, "menu/pizzas_de_la_mer.html", {'pizzas': pizzas})


def pizzasExclusives(request):
    pizzas = Pizza.objects.filter(category__in=Category.objects.filter(nom="Pizzas exclusives")).distinct().order_by('prix')
    return render(request, "menu/pizzas_exclusives.html", {'pizzas': pizzas})


def pizzasVegetariennes(request):
    pizzas = Pizza.objects.filter(vegetarienne=True).order_by('prix')
    return render(request, "menu/pizzas_vegetariennes.html", {'pizzas': pizzas})
