from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
import re  # for custom phone number validation

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

    # Email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('This email is already registered. Please choose another one')
        return email

    # Phone number validation (example, customize based on your requirements)
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_regex = r'^(?:\+234|0)[789]\d{9}$'  # Nigerian phone number format
        if not re.match(phone_regex, phone_number):
            raise ValidationError('Enter a valid phone number.')
        return phone_number

    # Make sure the data are clean and passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        # Check if password matches
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data