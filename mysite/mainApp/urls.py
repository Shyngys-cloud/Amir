from . import views
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns =[
   path('', TemplateView.as_view(template_name='mainApp/Dairy_products_and_eggs.html'), name='index'),
   path('contact/',TemplateView.as_view(template_name='mainApp/basic.html'), name='contact'),
   path('Bread_and_pastries/', TemplateView.as_view(template_name='mainApp/Bread_and_pastries.html'), name='Bread_and_pastries'),
   path('Dairy_products_and_eggs/',TemplateView.as_view(template_name='mainApp/Dairy_products_and_eggs.html'), name='Dairy_products_and_eggs'),
   path('Fish_seafood_caviar/',TemplateView.as_view(template_name='mainApp/Fish_seafood_caviar.html'), name='Fish_seafood_caviar'),
   path('Breakfast_cereals_cereal_muesli/',TemplateView.as_view(template_name='mainApp/Breakfast_cereals_cereal_muesli.html'), name='Breakfast_cereals_cereal_muesli'),
   path('Vegetables_and_greens/',TemplateView.as_view(template_name='mainApp/Vegetables_and_greens.html'), name='Vegetables_and_greens'),
   path('Fruits_berries/', TemplateView.as_view(template_name='mainApp/Fruits_berries.html'), name='Fruits_berries'),
   path('Cheese/',TemplateView.as_view(template_name='mainApp/Cheese.html'), name='Cheese'),
   path('Meat/',TemplateView.as_view(template_name='mainApp/Meat.html'), name='Meat'),
   path('Mayonnaise_ketchup_sauces_vinegar/',TemplateView.as_view(template_name='mainApp/Mayonnaise_ketchup_sauces_vinegar.html'), name='Mayonnaise_ketchup_sauces_vinegar'),
   path('Fast_food/',TemplateView.as_view(template_name='mainApp/Fast_food.html'), name='Fast_food'),
   path('register/', TemplateView.as_view(template_name='mainApp/login.html'), name='login'),
]
