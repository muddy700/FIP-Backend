from django.contrib.auth.models import User
from department_app.models import Department
from profession_app.models import Profession
from program_app.models import Program
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models

class StudentProfile(models.Model):
    student_status = models.BooleanField(default=True, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    year_of_study = models.CharField(max_length=100, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_id")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, default=38, related_name="organization_id")
    field_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, default=38, related_name="field_supervisor")
    academic_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, default=38, related_name="academic_supervisor")
    has_reported = models.BooleanField(default=False, blank=True, null=True)
    date_reported = models.DateTimeField(blank=True, null=True)
    field_report = models.FileField(upload_to='field_report/', blank=True, null=True, storage=RawMediaCloudinaryStorage())
    report_marks = models.FloatField(blank=True, null=True)
    academic_supervisor_marks = models.FloatField(blank=True, null=True)
    field_supervisor_marks = models.FloatField(blank=True, null=True)
    average_marks = models.FloatField(blank=True, null=True)
    marks_grade = models.CharField(max_length=2, blank=True, null=True)
    cancellation_count = models.IntegerField(blank=True, null=True)
    week_1_logbook = models.FileField(upload_to='logbook/', blank=True, null=True, storage=RawMediaCloudinaryStorage())
    week_2_logbook = models.FileField(upload_to='logbook/', blank=True, null=True, storage=RawMediaCloudinaryStorage())
    week_3_logbook = models.FileField(upload_to='logbook/', blank=True, null=True, storage=RawMediaCloudinaryStorage())
    week_4_logbook = models.FileField(upload_to='logbook/', blank=True, null=True, storage=RawMediaCloudinaryStorage())
    week_5_logbook = models.FileField(upload_to='logbook/', blank=True, null=True, storage=RawMediaCloudinaryStorage())


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