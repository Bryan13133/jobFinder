from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Login
from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'),max_length=150,widget=forms.TextInput(attrs={'class': 'text'}),required=True)
    password = forms.CharField(label=_('Password'),widget=(forms.PasswordInput(attrs={'class': 'text'})),required=True)

    class Meta():
        model = Login
        fields =  ('username','password')