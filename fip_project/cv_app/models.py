from django.contrib.auth.models import User
from users.models import UserProfile
from django.db import models

class PersonalInformation(models.Model):
    alumni = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cv_personal_owner")
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="owner_profile")
    cv_image = models.ImageField(upload_to='cv_images/', blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.alumni.username} Personal Info'

class EducationInformation(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cv_education_owner")
    institution = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    start_year = models.CharField(max_length=20)
    completion_year = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.alumni.username} Education Info'

class ExperienceInformation(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cv_experience_owner")
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.CharField(max_length=20)
    completion_date = models.CharField(max_length=20, blank=True)
    is_current_job = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.alumni.username} Experience Info'
