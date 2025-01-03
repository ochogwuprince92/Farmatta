from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Customize the admin view for the CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Specify fields to display in the admin list view
    list_display = ('username', 'email', 'is_farmer', 'is_buyer', 'is_staff')
    
    # Add filters in the right sidebar
    list_filter = ('is_farmer', 'is_buyer', 'is_staff')
    
    # Enable searching by username and email
    search_fields = ('username', 'email')
    
    # Define the fieldsets for editing user information
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Roles', {'fields': ('is_farmer', 'is_buyer')}),
    )
    
    # Specify the fields used for creating a new user in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'is_farmer', 'is_buyer'),
        }),
    )

    # Make the username the default ordering field
    ordering = ('username',)
