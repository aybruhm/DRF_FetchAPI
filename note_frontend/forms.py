from django import forms
from .models import Note


class NoteCreateForm(forms.ModelForm):
    """"
    This class creates a form for Note models
    """
    class Meta:
        model = Note
        fields = ['title', 'thought']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control user_input',
                    'id': 'validationCustomUsername',
                    'aria-describedby': 'inputGroupPrepend' 
                    'required': "true",
                }
            ),
            'thought': forms.Textarea(
                attrs={
                    'class': 'form-control edit_textarea',
                    'id': 'editThought',
                    'rows': '3',
                }
            )
        }