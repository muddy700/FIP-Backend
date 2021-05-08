from django.contrib.auth.models import User
from program_app.models import Program
from profession_app.models import Profession
from django.db import models

class InternshipPost(models.Model):
    organization = models.ForeignKey(User, on_delete=models.CASCADE)
    post_capacity = models.IntegerField()
    post_description = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    expiry_date = models.CharField(max_length=100)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.organization.username} Post'

class InternshipApplication(models.Model):
    post = models.ForeignKey(InternshipPost, on_delete=models.CASCADE, related_name="internship_application_post_id")
    alumni = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_application_id")
    status = models.CharField(max_length=100, default="pending")

    def __str__(self):
        return f'{self.alumni.username } Application' 