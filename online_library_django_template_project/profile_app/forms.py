from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Please choose a strong password'
        self.fields['password2'].help_text = 'Passwords must match'
        self.fields['username'].help_text = 'Min length: 3 symbols, Max length: 50 symbols.'
        self.fields['email'].help_text = 'Please enter an valid email address'

