
from django.views.generic import ListView
from django.shortcuts import render
from .models import CategoryModel

# Create your views here.


class MenuView(ListView):
    model = CategoryModel
    template_name = 'menu.html'
    context_object_name = 'category_list'