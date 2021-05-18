from django.db import models
from django.contrib.auth.models import User
from profession_app.models import Profession

class OrganizationProfile(models.Model):
    organization_id = models.OneToOneField(User, on_delete=models.CASCADE)
    box_address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.organization_id.username } Profile'

class Contract(models.Model):
    alumni = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    organization = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer")
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.alumni.username } Contract'