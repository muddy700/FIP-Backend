from django.contrib.auth.models import User
from django.db import models
from designation.models import Designation
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, blank=True, related_name="user_designation")
    profile_image = models.ImageField(upload_to='users_profiles/', blank=True)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class FieldInfo(models.Model):
    start_date = models.DateField(null=True, blank=True)
    number_of_weeks = models.IntegerField(null=True, blank=True)
    last_date_year_of_study_changed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.number_of_weeks} Weeks Of IPT'
