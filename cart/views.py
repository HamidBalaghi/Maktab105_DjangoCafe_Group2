from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Cart
from .managers.manager import *

# Create your views here.


class CartListView(ListView):
    model = Cart
    template_name = 'cart_list.html'
    context_object_name = 'cart_list'
   

class CartView(DetailView):
    model = Cart
    template_name = 'cart_html.html'
    context_object_name = 'cart'
   