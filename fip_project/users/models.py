from django.contrib.auth.models import User
from django.db import models
from designation.models import Designation
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    designation = models.OneToOneField(Designation, on_delete=models.CASCADE, blank=True, related_name="user_designation")
    profile_image = models.ImageField(upload_to='images/', blank=True)
    phone = models.CharField(max_length=11, blank=True)
    gender = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
