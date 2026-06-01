from django import forms
from .models import Moto, Categoria

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = [
            "categoria",
            "marca",
            "modelo",
            "año",
            "descripcion",
            "imagen",
        ]