from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
def user_directory_path(instance, filename):
    return '{0}/{1}/{2}' .format(instance.department, instance.folder, filename)

class Dept(models.Model):
    name = models.CharField(max_length=60, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Folder(models.Model):
    name = models.CharField(max_length=60, unique=True)
    folder = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='folder_set')
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Dept, on_delete=models.RESTRICT)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
    

class File(models.Model):
    name_of_file = models.CharField(max_length=32)
    description = models.CharField(max_length=32, unique=True)
    document = models.FileField(upload_to=user_directory_path)
    other_docs = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, related_name='file_set')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    fileuser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Dept, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name_of_file