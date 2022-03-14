from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import * 

User = get_user_model

STATUS = [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ('Human Resource', 'Human Resource'),
]


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "user_type")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
