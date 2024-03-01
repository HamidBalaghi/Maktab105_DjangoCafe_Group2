from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView

class HomeView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'home/home.html'

class MenuView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'product/menu.html'
    
class ProductView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'product/product.html'
    
class CartView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'basket/cart.html'

class LoginView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'profile/login.html'

class ChangeImageView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'profile/change_img.html'
    
class ChangePassView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'profile/change_password.html'

class RegisterView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'profile/register.html'

class ContactUsView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'contact/contact_us.html'
class AboutUsView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'about/about_coffe.html'