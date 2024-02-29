from django.urls import path
from .views import CartListView, CartView

urlpatterns = [
    path('cart/<int:pk>/', CartView.as_view(), name='cart'),
    path('cart_list/', CartListView.as_view(), name='cart_list'),
]