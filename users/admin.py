from django.contrib import admin
from .models import StaffUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from dept.admin import dept_site
# Register your models here.

class UsersInline(admin.StackedInline):
    model = StaffUser
    can_delete = False
    verbose_name_plural = 'Users'

class CustomUserAdmin(UserAdmin):
    inlines = (UsersInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
dept_site.register(User, CustomUserAdmin)
