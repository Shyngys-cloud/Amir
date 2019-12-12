from django.shortcuts import render

def index(request):
    return render (request, 'mainApp/homePage.html')

def contact(request):
    return render (request, 'mainApp/basic.html')

def Bread_and_pastries(request):
    return render (request, 'mainApp/Bread_and_pastries.html')

def Dairy_products_and_eggs(request):
    return render (request, 'mainApp/Dairy_products_and_eggs.html')

def Fish_seafood_caviar(request):
    return render (request, 'mainApp/Fish_seafood_caviar.html')

def Breakfast_cereals_cereal_muesli(request):
    return render (request, 'mainApp/Breakfast_cereals_cereal_muesli.html')

def Vegetables_and_greens(request):
    return render (request, 'mainApp/Vegetables_and_greens.html')

def Fruits_berries(request):
    return render (request, 'mainApp/Fruits_berries.html')

def Cheese(request):
    return render (request, 'mainApp/Cheese.html')

def Meat(request):
    return render (request, 'mainApp/Meat.html')

def Mayonnaise_ketchup_sauces_vinegar(request):
    return render (request, 'mainApp/Mayonnaise_ketchup_sauces_vinegar.html')

def Fast_food(request):
    return render (request, 'mainApp/Fast_food.html')
def login(request):
    return render (request, 'mainApp/login.html')


# Create your views here.
