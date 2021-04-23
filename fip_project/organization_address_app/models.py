from django.db import models
from django.contrib.auth.models import User

class OrganizationProfile(models.Model):
    organization_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    phone_number = models.CharField(max_length=100)
    box_address = models.CharField(max_length=100)

    def __str__(self):
        return self.organization_id.username