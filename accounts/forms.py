from django import forms
from django.contrib.auth.models import User
from accounts.models import user
import re
from django.core.validators import RegexValidator
from ckeditor.widgets import CKEditorWidget
from bootstrap_datepicker_plus import DatePickerInput


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)
    company = forms.CharField(max_length=20)
    skills = forms.CharField(label="Your Skills",
                            widget=CKEditorWidget)
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = user
        fields = ('firstname', 'lastname', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
