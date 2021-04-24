from django.contrib.auth.models import User
from department_app.models import Department
from designation.models import Designation
from django.db import models

class StaffProfile(models.Model):
    phone_number = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE)
    staff_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff_id")

    def __str__(self):
        return f'{self.staff_id.username } Profile'