from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView

# Create your views here.
class Login(LoginView):
    template_name='accounts/login.html'
    form_class=AuthenticationForm
    success_url='/' 


class Register(CreateView):
    template_name='accounts/register.html'
    form_class=UserCreationForm
    success_url='/'


class logout(LogoutView):
    pass    
        