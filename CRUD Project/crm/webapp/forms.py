from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput

from django import forms

# Register/Create a User

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields= ['username', 'password1', 'password2']

# Login a User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())