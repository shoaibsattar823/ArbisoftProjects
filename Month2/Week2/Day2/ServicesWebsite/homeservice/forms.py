from django import forms
# from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import re

from homeservice.models import SERVICE_CHOICES


class RequestForm(forms.Form):
    service_type = forms.ChoiceField(choices=SERVICE_CHOICES)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='email', max_length=30)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain'
                                        'alphanumeric characters and'
                                        'the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')
