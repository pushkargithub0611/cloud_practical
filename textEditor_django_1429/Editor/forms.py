from .models import TextModel
from django import forms


class TextForm(forms.ModelForm):
    class Meta:
        model=TextModel
        fields='__all__'