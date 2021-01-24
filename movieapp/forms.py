from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Movieblog

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

class postMovieblogForm(ModelForm):
    class Meta:
        model = Movieblog
        fields = ['title', 'body']