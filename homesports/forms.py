from django import forms
from .models import Moto, Categoria

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = "__all__"