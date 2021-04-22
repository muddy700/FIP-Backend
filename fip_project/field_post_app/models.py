from program_app.models import Program
from django.db import models
from profession_app.models import Profession
from organization_app.models import Organization
from django.contrib.auth.models import User

class FieldPost(models.Model):
    post_name = models.CharField(max_length=100)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    post_capacity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    expiry_date = models.CharField(max_length=100)

    def __str__(self):
        return self.post_name

class FieldPostProfession(models.Model):
    field_profession_post_id = models.ForeignKey(FieldPost, on_delete=models.CASCADE, related_name="field_profession_post_id")
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.field_profession_post_id

class FieldApplication(models.Model):
    field_application_post_id = models.ForeignKey(FieldPost, on_delete=models.CASCADE, related_name="field_application_post_id")
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_application_id")

    def __str__(self):
        return self.field_application_post_id 