from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'email', 'password']

    # You can add additional form validation or customization here if needed
