from django.db import models
from organization_app.models import Organization

class OrganizationAddress(models.Model):
    organization_id = models.OneToOneField(Organization, on_delete=models.CASCADE)
    organization_phone_number = models.CharField(max_length=100)
    organization_email = models.CharField(max_length=100)
    organization_box_address = models.CharField(max_length=100)

    def __str__(self):
        return self.organization_email