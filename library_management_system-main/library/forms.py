from django import forms
from library.models import *


class AuthorForm(forms.ModelForm):

    class Meta:
        model = AuthorModel
        fields = ['name', 'email', 'bio']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
                'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com',
                'autocomplete': 'email',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a short bio',
                'rows': 4,
            }),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryModel
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name',
                'autocomplete': 'off',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a short description',
                'rows': 4,
            }),
        }


class BookForm(forms.ModelForm):

    class Meta:
        model = BookModel
        fields = [
            'title',
            'author',
            'category',
            'isbn',
            'description',
            'published_date',
            'quantity',
            'available_quantity',
            'cover_image',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title',
                'autocomplete': 'off',
            }),
            'author': forms.Select(attrs={
                'class': 'form-select',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN',
                'autocomplete': 'off',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book description',
                'rows': 5,
            }),
            'published_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter total quantity',
                'min': 1,
            }),
            'available_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter available quantity',
                'min': 0,
            }),
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }


class BorrowRecordForm(forms.ModelForm):

    class Meta:
        model = BorrowRecordModel
        fields = ['book', 'due_date']

        widgets = {
            'book': forms.Select(attrs={
                'class': 'form-select',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }