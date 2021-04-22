from django.db import models
from django.contrib.auth.models import User
from organization_app.models import Organization 

class FieldSupervisorProfile(models.Model):
    phone_number = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number