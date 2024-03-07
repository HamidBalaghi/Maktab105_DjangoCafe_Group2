from django.urls import path
from .views import ReservedView

urlpatterns = [
    path("reserve/", ReservedView.as_view(), name="reserve"),
]
