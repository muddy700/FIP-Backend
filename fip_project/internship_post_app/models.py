from django.contrib.auth.models import User
from program_app.models import Program
from profession_app.models import Profession
from django.db import models

class InternshipPost(models.Model):
    reference_number = models.CharField(max_length=100, default="FIP/2021/P000")
    organization = models.ForeignKey(User, on_delete=models.CASCADE)
    post_capacity = models.IntegerField()
    post_description = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    expiry_date = models.DateField()
    status = models.CharField(max_length=50, default="test")
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference_number

class InternshipApplication(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_application_id")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applied_organization")
    post = models.ForeignKey(InternshipPost, on_delete=models.CASCADE, related_name="internship_application_post_id")
    test_marks = models.FloatField()
    practical_marks = models.FloatField(null=True, blank=True)
    oral_marks = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, default="received")
    confirmation_status = models.CharField(max_length=100, default="test")
    final_stage = models.CharField(max_length=100, default="inprogress")
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.alumni.username } Application' 

class InternshipApplicationStatus(models.Model):
    status_text = models.CharField(max_length=100)

    def __str__(self):
        return self.status_text 
class ApplicantLevel(models.Model):
    level_name = models.CharField(max_length=100)

    def __str__(self):
        return self.level_name 
class InterviewSchedule(models.Model):
    post = models.ForeignKey(InternshipPost, on_delete=models.CASCADE, related_name="post_scheduled")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actor_organization")
    event_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    requirements = models.CharField(max_length=500, default='')
    post_stage = models.CharField(max_length=100, default='test')



    def __str__(self):
        return f'{self.organization.username } Schedule'