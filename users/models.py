from django.db import models
from django.contrib.auth.models import User, AbstractUser
from hospital.models import Department




# Create your models here.
STATUS = [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ('Human Resource', 'Human Resource'),
]

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
 
 
class User(AbstractUser):
    user_type = models.CharField(choices=STATUS, max_length=20)
 
    def is_doctor(self):
        if self.user_type == 'Doctor':
            return True
        else:
            return False
 
    def is_patient(self):
        if self.user_type == 'Patient':
            return True
        else:
            return False
 
    def is_HR(self):
        if self.user_type == 'Human Resource':
            return True
        else:
            return False
 
    class Meta:
        ordering = ('id',)



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


class DoctorProfile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50,choices=SPECIALITIES, null=True, blank=True)
    date_of_birth = models.DateField(help_text='Format: YYYY-MM-DD', null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    available_time = models.DateTimeField()
    weekdays = models.CharField(max_length=20, help_text="Format: Monday - Friday")
    weekends = models.CharField(max_length=20, help_text="Format: Saturday - Sunday")

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

class PatientProfile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    date_of_birth = models.DateField(help_text='Format: YYYY-MM-DD', null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10, null=True, blank=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True)
    med_reps = models.FileField(upload_to='profile/med_reps', blank=True)
    case_paper = models.IntegerField(blank=True, null=True)
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', null=True, blank=True, default='/avatar.png')

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Profile for {}".format(self.user)


# def post_save_receiver(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)








    
# Doctors
# class Doctor(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     speciality = models.CharField(max_length=50,choices=departments,default='Cardiologist')
#     # email = models.EmailField(max_length=100, unique=True)
#     details = models.TextField()
#     department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
#     profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)

#     education = models.ManyToManyField(to='Education', related_name='doctors', blank=True)
#     training = models.ManyToManyField(to='Training', related_name='doctors', blank=True)
#     certificate = models.ManyToManyField(to='Certificate', related_name='doctors', blank=True)

#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=True)

#     facebook = models.CharField(max_length=120, blank=True, null=True)
#     whatsapp = models.CharField(max_length=120, blank=True, null=True)
#     twitter = models.CharField(max_length=120, blank=True, null=True)
#     instagram = models.CharField(max_length=120, blank=True, null=True)
#     status=models.BooleanField(default=False)

#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_id(self):
#         return self.user.id
#     def __str__(self):
#         return "{} ({})".format(self.user.first_name,self.department)


# class Education(models.Model):
#     name = models.CharField(max_length=120)

#     def __str__(self):
#         return self.name

# class Training(models.Model):
#     name = models.CharField(max_length=120)

#     def __str__(self):
#         return self.name

# class Certificate(models.Model):
#     name = models.CharField(max_length=120)

#     def __str__(self):
#         return self.name



