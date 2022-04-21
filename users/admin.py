from django.contrib import admin
from .models import User, DoctorProfile, PatientProfile, Country, City

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_type', 'email')
    list_filter = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')

admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(Country)
admin.site.register(City)


