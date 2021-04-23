from django.db import models
from designation.models import Designation
from django.contrib.auth.models import User
# from organization_app.models import Organization 

class FieldSupervisorProfile(models.Model):
    phone_number = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images/', blank=True)
    supervisor_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="supervisor_id")
    organization_id = models.ForeignKey(User, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number