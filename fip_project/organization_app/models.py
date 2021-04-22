from django.db import models

class Organization(models.Model):
    organization_name = models.CharField(max_length=100)
    organization_profile_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.organization_name