from django.urls import path
from .views import UserLoginView, UserLogoutView, EditeUserView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('editeuser/', EditeUserView.as_view(), name='edit_user'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)