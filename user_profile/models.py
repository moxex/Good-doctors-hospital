from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
DEPARTMENTS=[
    ('Anesthesiology','Anesthesiology'),
    ('Pharmacy','Pharmacy'),
    ('Radiology', 'Radiology'),
    ('Gastroenterology', 'Gastroenterology'),
    ('Orthopaedics', 'Orthopaedics'),
    ('Community Medicine', 'Community Medicine'),
    ('Internal Medicine', 'Internal Medicine'),
    ('Laboratory', 'Laboratory'),
    ('Nursing', 'Nursing'),
    ('Medical Records', 'Medical Records'),
    ('Cardiology', 'Cardiology'),
    ('Pediatrics', 'Pediatrics'),
    ('Obstetics', 'Obstetics'),
    ('Nephrology', 'Nephrology'),
    ('Physiotherapy', 'Physiotherapy'),
    
     ]

SPECIALITIES = [
    ('Dermatologists', 'Dermatologists'),
    ('Cardiologists', 'Cardiologists'),
    ('Gastroenterologist', 'Gastroenterologist'),
    ('Physiotherapist', 'Physiotherapist'),
    ('Pharmacist','Pharmacist'),
    ('Orthopaedist', 'Orthopaedist'),
    ('Nephrologist', 'Nephrologist'),
    ('Neurologist', 'Neurologist'),
    ('Rectal Surgeons', 'Rectal Surgeons'),
    ('Anesthesiologists','Anesthesiologists'),
    ('Allergists/Immunologists', 'Allergists/Immunologists'),
    ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
]

GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

BLOOD_GROUPS = [
    ('O-', 'O-'),
    ('O+', 'O+'),
    ('A-', 'A-'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),
    ('AB+', 'AB+'),
] 


class Country(models.Model):
    alpha_2 = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models. ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f' {self.name} - ({self.country.name})'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    speciality = models.CharField(max_length=50,choices=SPECIALITIES, null=True, blank=True)
    date_of_birth = models.DateField(help_text='Format: YYYY-MM-DD', null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, null=True, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True)

    
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    department= models.CharField(max_length=50,choices=DEPARTMENTS, null=True, blank=True)
    med_reps = models.FileField(upload_to='profile/med_reps', blank=True)
    case_paper = models.IntegerField(blank=True, null=True)
    about_me = models.TextField(max_length=300, help_text='Write something about yourself, not more than 300 words', null=True, blank=True)


    
    education = models.CharField(max_length=100, blank=True, help_text='Eductional Background')
    training = models.CharField(max_length=100, blank=True, help_text='Training Attended')
    certificate = models.CharField(max_length=100, blank=True, help_text='Cerficate and award')

    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', null=True, blank=True, default='/avatar.png')
    facebook = models.CharField(max_length=120, blank=True, null=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)
    linkedIn = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], null=True, blank=True, max_length=8)


    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Profile for {}".format(self.user)

