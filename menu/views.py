from django.views.generic import ListView, View
from django.shortcuts import render
from .models import *


# Create your views here.


class CategoryView(ListView):
    model = Category
    template_name = 'menu/categories.html'
    context_object_name = 'categories_list'


class ProductView(View):

    def get(self, request, id):
        category = Category.objects.get(id=id)
        products = Category.objects.filter(category=category)
        return render(request, 'products.html', {'products_list': products})
