from django import forms
from django.forms import models
from .models import Todo

# create forms

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo

        fields="__all__"