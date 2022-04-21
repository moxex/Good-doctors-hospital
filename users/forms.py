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


class PatientProfileForm(UserCreationForm):
   
    class Meta:
        model = PatientProfile
        fields = ('phone_number', 'gender', 'date_of_birth', 'country', 'city', 'address', 'blood_group', 'profile_picture' 'med_reps', 'case_paper')
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter Your Address'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


class DoctorProfileForm(UserCreationForm):
   
    class Meta:
        model = DoctorProfile
        fields = ('phone_number', 'gender', 'date_birth', 'address', 'country', 'city', 'department', 'education', 'training', 'certificate', 'about_me', 'profile_picture', 'facebook', 'twitter', 'linkedIn' 'status')
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter Your Phone Number'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter Your Address'}),
            'education': forms.TextInput(attrs={'placeholder': 'Enter Your Education'}),
            'certificate': forms.TextInput(attrs={'placeholder': 'Enter Your Certificate'}),
            'training': forms.TextInput(attrs={'placeholder': 'Enter Your Training'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Enter Your Facebook link'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Enter Your Twitter link'}),
            'linkedIn': forms.TextInput(attrs={'placeholder': 'Enter Your LinkedIn link'}),
            'about_me': forms.Textarea(attrs={'placeholder': 'Few Things About You...'}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')