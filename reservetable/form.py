from django import forms
from .models import Reserve
from menu.models import Table


class TableNumberForm(forms.Form):

    table_number = forms.ModelChoiceField(Table.objects.filter(is_reserved=False))


