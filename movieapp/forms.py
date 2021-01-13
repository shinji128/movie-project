from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

#class MovieForm(models.Form):
#    query = forms.CharField(
#        label='検索ワード',
#        max_length=100,
#        required=False,
#        widget=forms.TextInput(attrs={'placeholder': '数字 7 桁(ハイフンなし)'}))
#    movietitle = forms.CharField(
#        label='映画タイトル',
#        max_length=100,
#        required=False)