from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Permission 
from django import forms


COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
    ('purple','PURPLE'),
    ('white','WHITE'),
)


CURRENT_COURSE = (
    ('RedTeam', 'Red_Team'),
    ('BlueTeam', 'Blue_Team'),
    ('DevOps', 'Dev_Ops'),
    ('FrontEnd', 'Front_End'),
    ('BackEnd', 'Back_End'),
    ('PyData', 'PyData'),
    ('Q-Sec', 'Quantum_Security'),
    ("Frankie's Lab Rat", "Frankie's Course"),
)

PERMS_C = (
    ('poes', 'naai'),
    ('fuck', 'head')
)


class SignUpForm(UserCreationForm):
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',}))
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), max_length=100)
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), max_length=100)


    class meta:
        model   = User
        fields  = ('username',  'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'forms-control'
        self.fields['password1'].widget.attrs['class'] = 'forms-control'
        self.fields['password2'].widget.attrs['class'] = 'forms-control'



class EditUserForm(UserChangeForm):
    username        = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), max_length=100)
    first_name      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), max_length=100)
    last_name       = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), max_length=100)
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',}))
    profile_color   = forms.CharField(widget=forms.Select(choices=COLOR_CHOICES, attrs={'class': 'btn btn-danger dropdown-toggle',}))
    active_course   = forms.CharField(widget=forms.Select(choices=CURRENT_COURSE, attrs={'class': 'btn btn-danger dropdown-toggle',}))

    is_superuser    = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check', 'type':'hidden'}), max_length=1)
    is_staff        = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check', 'type':'hidden'}),)
    is_active       = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check', 'type':'hidden'}))
    groups          = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-conrtol', 'type': 'hidden'}))
    password     = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'hidden'}))
    date_joined     = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'read-only'}))
    last_login      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'read-only'}))


    class meta:
        model   = User
        fields  = (
            'is_active', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'profile_color', 
            'active_course',

        )



