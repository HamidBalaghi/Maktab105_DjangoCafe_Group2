from django.urls import path
from .views import HomeView, MenuView, ProductView, CartView, LoginView, ChangeImageView, ChangePassView, RegisterView, ContactUsView, AboutUsView

urlpatterns = [
    path('', HomeView.as_view()),
    path('menu/', MenuView.as_view()),
    path('product/', ProductView.as_view()),
    path('basket/', CartView.as_view()),
    path('login/', LoginView.as_view(),),
    path('changeimg/', ChangeImageView.as_view()),
    path('register/', RegisterView.as_view()),
    path('change_password/', ChangePassView.as_view()),
    path('contactus/', ContactUsView.as_view()),
    path('about/', AboutUsView.as_view())
]