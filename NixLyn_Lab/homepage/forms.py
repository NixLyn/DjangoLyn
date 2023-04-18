from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'add_on', 'color')
        widgets = {
            'title':    forms.TextInput(attrs={'class': 'form-control',}),
            'author':   forms.Select(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'body':     forms.Textarea(attrs={'class': 'form-control'}),
            'add_on':   forms.TextInput(attrs={'class': 'form-control'}),
            'color':    forms.Select(attrs={'class': 'form-control'}),
            }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'add_on', 'color')
        widgets = {
            'title':    forms.TextInput(attrs={'class': 'form-control'}),
            'body':     forms.Textarea(attrs={'class': 'form-control'}),
            'add_on':   forms.TextInput(attrs={'class': 'form-control'}),
            'color':    forms.Select(attrs={'class': 'form-control', 'style':f'backround-color: blue'}),
        }
