from django.contrib.auth.models import User
from department_app.models import Department
from profession_app.models import Profession
from program_app.models import Program
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models

class StudentProfile(models.Model):
    student_status = models.BooleanField()
    phone_number = models.CharField(max_length=100)
    year_of_study = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_id")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, default=38, related_name="organization_id")
    field_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, default=38, related_name="field_supervisor")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    academic_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, default=38, related_name="academic_supervisor")
    has_reported = models.BooleanField(default=False)
    date_reported = models.DateTimeField(blank=True, null=True)
    field_report = models.FileField(upload_to='raw/', blank=True, null=True, storage=RawMediaCloudinaryStorage())


    def __str__(self):
        return f'{self.student.username } Profile'

class StudentProfession(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_profession_id")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_id.username } Profession' 

class FieldReport(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="report_owner_id")
    report_file = models.FileField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return f'{self.student_id.username } Report' 