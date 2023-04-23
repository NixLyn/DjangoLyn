from django import forms
from .models import PostDash


class PostDash(forms.ModelForm):
    class Meta:
        model = PostDash
        fields = ('author', 'color')
        widgets = {
            'author':   forms.Select(attrs={'class': 'form-control', }),
            'color':    forms.Select(attrs={'class': 'form-control',}),
            }


