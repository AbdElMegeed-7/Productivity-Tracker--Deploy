from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished', 'score']


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        widgets = {'date': DateInput()}
        fields = ['date']
