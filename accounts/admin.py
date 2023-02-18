
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = [
        "username",
        "member",
        "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("member",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("member",)}),)

admin.site.register(CustomUser, CustomUserAdmin)