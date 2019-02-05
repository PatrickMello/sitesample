from django.shortcuts import render
from django.views.generic import ListView

from core.models import Product


# Create your views here.
class HomePage(ListView):
    template_name = 'home.html'
    context_object_name = 'product_list'
    queryset = Product.objects.filter(is_active=True)

