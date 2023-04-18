from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditUserForm

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class      = SignUpForm
    template_name   = 'registration/register.html'
    success_url     = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class      = EditUserForm
    template_name   = 'registration/edit_profile.html'
    success_url     = reverse_lazy('dashboards')

    def get_object(self):
        return self.request.user

