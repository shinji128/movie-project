from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

class MovieForm(forms.Form):
    query = forms.CharField(
        label='検索ワード',
        max_length=100,
        required=False)

    movietitle = forms.CharField(
        label='映画タイトル',
        max_length=100,
        required=False)