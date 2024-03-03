from django.urls import path
from .views import UserLoginView, UserLogoutView, EditeUserView, RegisterView, CreateUserView, ChangePasswordView, \
    CreateProfileView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('creatuser/', CreateUserView.as_view(), name='creat_user'),
    path('creatprofile/', CreateProfileView.as_view(), name='creat_profile'),
    path('editeuser/', EditeUserView.as_view(), name='edit_user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('changepass/', ChangePasswordView.as_view(), name='change_pass'),
]
