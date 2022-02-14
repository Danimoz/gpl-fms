from django.contrib import admin
from .models import Dept, File, Folder

class StaffAdmin(admin.AdminSite):
    site_header = 'File Management System Admin'
    
dept_site = StaffAdmin(name='StaffAdmin')
dept_site.register(Dept)
dept_site.register(File)
dept_site.register(Folder)

# Register your models here.
admin.site.register(Dept)
admin.site.register(File)
admin.site.register(Folder)