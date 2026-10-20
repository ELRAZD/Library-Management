from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import *


class RegisterForm(UserCreationForm):

    class Meta:
        model = UserModel

        fields = [
            'username',
            'full_name',
            'email',
            'phone',
            'profile_image',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username',
                'autocomplete': 'username',
            }),

            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'autocomplete': 'name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com',
                'autocomplete': 'email',
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+880 1XXXXXXXXX',
                'autocomplete': 'tel',
            }),

            'profile_image': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
            }),
        }


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'autocomplete': 'username',
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password',
        })
    )