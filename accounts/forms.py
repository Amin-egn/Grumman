from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """Signup Form"""
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1', 'password2')
