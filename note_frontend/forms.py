from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note


class NoteCreateForm(forms.ModelForm):
    """"
    This class creates a note.
    """
    class Meta:
        model = Note
        fields = ['title', 'thought']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control user_input',
                'id': 'validationCustomUsername',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'thought': forms.Textarea(attrs={
                'class': 'form-control edit_textarea',
                'id': 'editThought',
                'rows': '3',
                }
            )
        }


class NoteUpdateForm(forms.ModelForm):
    """
    This class updates a note.
    """

    class Meta:
        model = Note
        fields = ['title', 'thought']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control user_input',
                'id': 'validationCustomUsername',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'thought': forms.Textarea(attrs={
                'class': 'form-control edit_textarea',
                'id': 'editThought',
                'rows': '3',
                }
            )
        }


class CreateUserForm(UserCreationForm):
    """
    This class inherits from the base class *UserCreationForm*,
    and creates a new user.
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        ),
        'password1': forms.PasswordInput(attrs={
            'class': 'form-control password_input',
            'id': 'validationCustom03',
            'required': 'true',
            }
        ),
        'password2': forms.PasswordInput(attrs={
            'class': 'form-control password_input',
            'id': 'validationCustom03',
            'required': 'true',
            }
        ),
    }