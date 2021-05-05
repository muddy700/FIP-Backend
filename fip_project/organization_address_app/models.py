from django.db import models
from django.contrib.auth.models import User

class OrganizationProfile(models.Model):
    organization_id = models.OneToOneField(User, on_delete=models.CASCADE)
    box_address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.organization_id.username } Profile'