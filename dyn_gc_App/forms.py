from django import forms
from dyn_gc_App.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput()}
        fields = ['username', 'password', 'first_name', 'last_name', 'mobile', 'email', 'dob']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())