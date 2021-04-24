from django.contrib.auth.models import User
from program_app.models import Program
from profession_app.models import Profession
from django.db import models

class InternshipPost(models.Model):
    post_title = models.CharField(max_length=100)
    organization_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_capacity = models.IntegerField()
    post_description = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    expiry_date = models.CharField(max_length=100)

    def __str__(self):
        return self.post_title

class InternshipPostProfession(models.Model):
    internship_profession_post_id = models.ForeignKey(InternshipPost, on_delete=models.CASCADE, related_name="internship_profession_post_id")
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.internship_profession_post_id.post_title } Profession'

class InternshipApplication(models.Model):
    internship_application_post_id = models.ForeignKey(InternshipPost, on_delete=models.CASCADE, related_name="internship_application_post_id")
    alumni_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_application_id")

    def __str__(self):
        return f'{self.internship_application_post_id.post_title } Application' 