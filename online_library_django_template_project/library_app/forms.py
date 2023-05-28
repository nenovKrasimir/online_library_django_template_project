from django import forms
from .models import Book


class UploadBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['user']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'style': 'resize: none', 'rows': 3, 'cols': 40}),
            'type': forms.TextInput(attrs={'placeholder': 'Drama, Romantic etc.'})
        }

        labels = {
            'title': 'Title',
            'description': 'Description',
            'type': 'Type',
            }


class EditBookForm(UploadBookForm):
    pass