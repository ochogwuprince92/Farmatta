from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserRegistrationForm(forms.ModelForm):    
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password_confirmation', 'is_farmer', 'is_buyer', 'address', 'phone_number']

# Username Validation 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken. Please choose another one')
        return username

# Make sure the data are clean
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmaton = cleaned_data.get('password_confirmation')

# check if password matches
        if password != password_confirmaton:
            raise forms.ValidationError('passwords do not match.')
        return cleaned_data