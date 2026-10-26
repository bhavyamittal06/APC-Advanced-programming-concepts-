import re

from django import forms
from django.contrib.auth.models import User

USERNAME_PATTERN = r"^[A-Za-z][A-Za-z0-9_]{2,19}$"
EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
PASSWORD_PATTERN = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s]).{8,}$"


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, help_text="3-20 characters: letters, numbers and _. Start with a letter.")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, help_text="Minimum 8 characters with upper, lower, number and symbol.")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.fullmatch(USERNAME_PATTERN, username):
            raise forms.ValidationError("Invalid username format.")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not re.fullmatch(EMAIL_PATTERN, email):
            raise forms.ValidationError("Enter a valid email address.")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not re.fullmatch(PASSWORD_PATTERN, password):
            raise forms.ValidationError("Password does not meet the required format.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data

    def save(self):
        return User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
        )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
