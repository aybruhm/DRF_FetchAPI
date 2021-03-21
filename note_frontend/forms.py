from django import forms
from django.contrib.auth.forms import UserCreationForm,\
    AuthenticationForm
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
    A form that inherits from the base *UserCreationForm*,
    and creates a user, with no privileges, from the given 
    username and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword2',
            'required': 'true',
            }
        ),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        ),
    }


class LogUserForm(forms.Form):
    """
    A form that inherits from the base *Form* class,
    and logs a user, with no privileges, from the given 
    username and password.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        )
    )