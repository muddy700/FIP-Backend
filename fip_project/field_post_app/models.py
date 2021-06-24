from program_app.models import Program
from django.db import models
from profession_app.models import Profession
from django.contrib.auth.models import User

class FieldPost(models.Model):
    reference_number = models.CharField(max_length=100,  default="FIP/2021/F000", unique=True)
    organization = models.ForeignKey(User, on_delete=models.CASCADE)
    post_description = models.CharField(max_length=500, blank=True)
    post_capacity = models.IntegerField(null=True, blank=True)
    applied_chances = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField()

    def __str__(self):
        return self.reference_number
        # return f'{self.organization.username} Post'

class FieldPostProfession(models.Model):
    post = models.ForeignKey(FieldPost, on_delete=models.CASCADE, related_name="field_profession_post_id")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    profession_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.post.reference_number } Profession'

class FieldPostProgram(models.Model):
    post = models.ForeignKey(FieldPost, on_delete=models.CASCADE, related_name="field_program_post_id")
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    program_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.post.reference_number } Program'

class FieldApplication(models.Model):
    post = models.ForeignKey(FieldPost, on_delete=models.CASCADE, related_name="field_application_post_id")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_application_id")
    has_reported = models.BooleanField(default=False)
    has_released = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post.reference_number } Application' 