from django import forms
from .models import Reserve


class TableNumberForm(forms.ModelForm):

    TableNumbers = forms.IntegerField(min_value=0)

    class Meta:
        model = Reserve
        fields = []
