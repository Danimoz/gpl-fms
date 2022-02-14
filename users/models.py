from django.db import models
from django.contrib.auth.models import User
from dept.models import Dept
# Create your models here.

class StaffUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_user')
    department = models.ForeignKey(Dept, on_delete=models.RESTRICT)

    def __str__(self):
        return self.user.username


