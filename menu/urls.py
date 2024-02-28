from .views import *
from django.urls import path

urlpatterns = [
    path('menu_list', MenuView.as_view(), name='menu_list'),
    path('products_list/<int:id>/', ProductView.as_view(), name='products_list'),
    
]
