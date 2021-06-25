from django.contrib.auth.models import User
from department_app.models import Department
from designation.models import Designation
from django.db import models

class StaffProfile(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_id")

    def __str__(self):
        return f'{self.staff.username } Profile'