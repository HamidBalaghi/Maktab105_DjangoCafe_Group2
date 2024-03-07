from django.views.generic import ListView
from .models import Reserve
from typing import Any
from .form import TableNumberForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.http import HttpResponse
from menu.models import Table

class ReservedView(ListView, FormView):
    model = Reserve
    template_name = "tablereservation/reservation.html"
    form_class = TableNumberForm

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tableid'] = Table.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            table_number = form.cleaned_data["TableNumbers"]
            table = Table.objects.get(id=table_number)
            if table.is_reserved == True:
                raise PermissionDenied("this table is reserved")
            else:
                table.is_reserved = True
                table.save()
            return HttpResponse("Success: Table is reserved.")
        else:
            return HttpResponse("Error: Form is invalid. Please try again.")
        return redirect("home")
