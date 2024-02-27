from .views import MenuView
from django.urls import path

urlpatterns = [
    path('menu_list', MenuView.as_view(), name='menu_list'),
    
]
