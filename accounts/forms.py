from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# class RegisterForm(UserCreationForm):
#     """Signup Form"""
#     name = forms.CharField(max_length=255, required=True)
#     email = forms.EmailField(max_length=255, required=True)
#
#     class Meta:
#         model = User
#         fields = ('name', 'username', 'email', 'password1', 'password2')


class RegisterForm(forms.ModelForm):
    """Register Form"""
    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password_repeat')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Passwords do not match!')
        else:
            raise forms.ValidationError('Password not confirms')
        return self.cleaned_data

    def save(self, commit=True):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        return user
