from django.db import models
from django.contrib.auth.models import User, AbstractUser



# Create your models here.
STATUS = [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ('Human Resource', 'Human Resource'),
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



