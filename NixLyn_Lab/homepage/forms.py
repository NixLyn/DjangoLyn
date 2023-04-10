from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',  'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'form-control-color'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control', 'form-control-color'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'add_on': forms.TextInput(attrs={'class': 'form-control'}),
        }

