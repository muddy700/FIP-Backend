from django.db import models
from designation.models import Designation
from django.contrib.auth.models import User
# from organization_app.models import Organization 

class FieldSupervisorProfile(models.Model):
    supervisor_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="supervisor_id")
    organization_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.supervisor_id.username } Profile'