from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import * 


class ProfileUpdateForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER)
    class Meta:
        model = UserProfile
        fields = ('name', 'phone_number', 'gender', 'date_of_birth', 'country', 'city', 'address', 'blood_group', 'profile_picture' 'med_reps', 'case_paper')


class DoctorProfileForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER)
    class Meta:
        model = UserProfile
        fields = ('name', 'phone_number', 'email', 'gender', 'date_birth', 'address', 'country', 'city', 'department', 'education', 'training', 'certificate', 'about_me', 'profile_picture', 'facebook', 'twitter', 'linkedIn' 'status')

