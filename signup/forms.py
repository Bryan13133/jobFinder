from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Signup


class SignupForm(UserCreationForm):
    username = forms.CharField(label=_('Username'),max_length=150,help_text=_('Required. 150 characters or fewer.'),widget=forms.TextInput(attrs={'class': 'text'}),required=True)
    email = forms.EmailField(label = ('Email'),max_length=50,widget=(forms.TextInput(attrs={'class': 'text'})),required=True)
    password1 = forms.CharField(label=_('Password'),widget=(forms.PasswordInput(attrs={'class': 'text'})),help_text=password_validation.password_validators_help_text_html(),required=True)
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'text'}),help_text=_('Just Enter the same password, for confirmation'),required=True)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('username','email','password1','password2')
        # fields = [
        #     'username',
        #     'email',        
        #     'password1',        
        #     'password2',      
        # ]
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'text','placeholder':'Username'},),
        #     'email':        forms.TextInput(attrs={'class': 'text email','placeholder':'Email'},),
        #     'password':        forms.PasswordInput(attrs={'class': 'text','placeholder':'Password'},),
        #     'confirmPassword':       forms.PasswordInput(attrs={'class': 'text w3lpass','placeholder':'Confirm Password'},),
           
        # }
    # def clean(self):
    #     cleaned_data = super(SignupForm,self).clean()
    #     password = cleaned_data.get("password")
    #     confirmPassword = cleaned_data.get("confirmPassword")

    #     if password and confirmPassword:
    #         if password != confirmPassword:
    #             raise forms.ValidationError("The two password fields must match.")
    #     return cleaned_data

