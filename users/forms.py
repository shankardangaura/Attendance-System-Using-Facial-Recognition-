import re

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User
from django.urls import reverse_lazy

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'user-registration-form'
        self.helper.attrs = {
            'hx-post': reverse_lazy('index'),
            'hx-target': '#user-registration-form',
            'hx-swap': 'outerHTML'
        }
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = User
        fields = ('username', 'password')

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username[0].isalpha() or not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise forms.ValidationError("Username must start with an alphabet and should not contain symbols at the beginning.")
        return username

    def save(self, commit=True):
        """ Hash user's password on save """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    

