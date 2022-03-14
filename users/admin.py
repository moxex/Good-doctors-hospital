from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_type', 'email')
    list_filter = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')

