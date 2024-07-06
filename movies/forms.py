from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . import models
from django.contrib.auth.models import User

class Register(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']

class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ['Username','Email','password1','password2']

