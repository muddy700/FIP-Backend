from django.contrib.auth.models import User
from department_app.models import Department
from profession_app.models import Profession
from program_app.models import Program
from django.db import models

class AlumniProfile(models.Model):
    completion_year = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    alumni = models.OneToOneField(User, on_delete=models.CASCADE, related_name="alumni_id")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_taken = models.BooleanField(default=False)
    organization = models.ForeignKey(User, on_delete=models.CASCADE, default=38, related_name="alumni_organization_id")
    is_public = models.BooleanField(default=False)
    gpa = models.FloatField(blank=True)

    def __str__(self):
        return f'{self.alumni.username} Profile'

class AlumniProfession(models.Model):
    alumni  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_profession_id")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.alumni.username} Profession'