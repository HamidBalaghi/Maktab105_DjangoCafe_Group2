
from django.views.generic import ListView, View
from django.shortcuts import render
from .models import *

# Create your views here.


class MenuView(ListView):
    model = CategoryModel
    template_name = 'menu.html'
    context_object_name = 'category_list'



class ProductView(View):

    def get(self, request, id):
        category= CategoryModel.objects.get(id=id)
        products = ProductModel.objects.filter(category=category)
        return render(request, 'products.html', {'products_list':products})
 