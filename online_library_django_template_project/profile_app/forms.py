from django import forms
from django.core.exceptions import ValidationError

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

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, first_name=user.username)  # Create a UserProfile for the user
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Passwords do not match.",
                code="password_mismatch",
            )
        return password2


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ['user']


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
