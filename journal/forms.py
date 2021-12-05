from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import journal

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': "radio"
            })
        }

class CreateEntryForm(ModelForm):
    class Meta:
        model = journal
        fields = ('title','entry')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['entry'].widget.attrs.update({'class':'textarea','placeholder':'Enter a journal entry'})