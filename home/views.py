from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView

class HomeView(ListView):
    def get_queryset(self) -> QuerySet[Any]:
        return None
    
    def get_template_names(self):
        return 'base/base-home.html'