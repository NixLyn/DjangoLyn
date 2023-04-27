from django import forms
from .models import PostDash, MyTarget


class PostDash(forms.ModelForm):
    class Meta:
        model = PostDash
        fields = ('author', 'color')
        widgets = {
            'author':   forms.Select(attrs={'class': 'form-control', }),
            'color':    forms.Select(attrs={'class': 'form-control',}),
            }


class EditTarget(forms.ModelForm):
    class Meta:
        model = MyTarget
        fields = ('author', 'target')
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control', 'type':'hidden'}),
            'target': forms.TextInput(attrs={'class': 'form-control',}),
            }


