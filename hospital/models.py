from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


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

# Department
class Department(models.Model):
    title = models.CharField(max_length=50, choices=DEPARTMENTS)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='department/')
    cover = models.ImageField(upload_to='department/')

    def __str__(self):
        return self.title


# Appointment
# class Appointment(models.Model):
#     time_choices = (
#         ('morning', "Morning"),
#         ('evening', "Evening")
#     )
#     patientId = models.PositiveIntegerField(null=True)
#     doctorId = models.PositiveIntegerField(null=True)
#     patientName = models.CharField(max_length=50, null=True)
#     doctorName = models.CharField(max_length=50, null=True)
#     appointmentDate = models.DateField(auto_now=True)
#     time = models.CharField(choices=time_choices, max_length=10)
#     note = models.TextField(blank=True, null=True)
#     status = models.BooleanField(default=False)




# Patient
# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True)
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20, null=False)
#     symptoms = models.CharField(max_length=100, null=False)
#     assignedDoctorId = models.PositiveIntegerField(null=True)
#     admitDate = models.DateField(auto_now=True)
#     status = models.BooleanField(default=False)

#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name
#     @property
#     def get_id(self):
#         return self.user.id
#     def __str__(self):
#         return self.user.first_name+" ("+self.symptoms+")"


# Patient Discharged Details
# class PatientDischargeDetails(models.Model):
#     patientId = models.PositiveIntegerField(null=True)
#     patientName = models.CharField(max_length=40)
#     assignedDoctorName = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20, null=True)
#     symptoms = models.CharField(max_length=100, null=True)

#     admitDate = models.DateField(null=False)
#     releaseDate = models.DateField(null=False)
#     daySpent = models.PositiveIntegerField(null=False)

#     roomCharge = models.PositiveIntegerField(null=False)
#     medicineCost = models.PositiveIntegerField(null=False)
#     doctorFee = models.PositiveIntegerField(null=False)
#     otherCharge = models.PositiveIntegerField(null=False)
#     total = models.PositiveIntegerField(null=False)


# Hospital Portfolio
# class Portfolio(models.Model):
#     title = models.CharField(max_length=120)
#     image = models.ImageField(upload_to="portfolio/")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name_plural = "Portfolios"