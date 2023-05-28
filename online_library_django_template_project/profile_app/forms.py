from django import forms
from .models import UserProfile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        #     'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        #     'password': forms.PasswordInput(attrs={'placeholder': 'Password'}), }
        #
        # labels = {
        #     'username': 'Username',
        #     'email': 'Email',
        #     'age': 'Age',
        #     'password': 'Password', }
