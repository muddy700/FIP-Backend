from django.contrib.auth.models import User
from department_app.models import Department
from profession_app.models import Profession
from program_app.models import Program
from django.db import models

class AlumniProfile(models.Model):
    phone_number = models.CharField(max_length=100)
    completion_year = models.CharField(max_length=100)
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    alumni_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="alumni_id")
    profile_image = models.ImageField(upload_to='images/', blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    organization_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_organization_id")

    def __str__(self):
        return self.alumni_id

class AlumniProfession(models.Model):
    alumni_id    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_profession_id")
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.alumni_id