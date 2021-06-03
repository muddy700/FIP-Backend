from django.contrib.auth.models import User
from users.models import UserProfile
from django.db import models

class PersonalInformation(models.Model):
    alumni = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cv_owner")
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="owner_profile")
    cv_image = models.ImageField(upload_to='images/', blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.alumni.username} Personal Info'
