from django.contrib.auth.models import User
from department_app.models import Department
from profession_app.models import Profession
from program_app.models import Program
from django.db import models

class StudentProfile(models.Model):
    student_status = models.BooleanField()
    phone_number = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=100)
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    student_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_id")
    organization_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organization_id")
    profile_image = models.ImageField(upload_to='images/', blank=True)
    field_supervisor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="field_supervisor")
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_supervisor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="academic_supervisor")

    def __str__(self):
        return f'{self.student_id.username } Profile'

class StudentProfession(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_profession_id")
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_id.username } Profession' 