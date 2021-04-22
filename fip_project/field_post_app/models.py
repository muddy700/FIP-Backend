from program_app.models import Program
from django.db import models
from organization_app.models import Organization

class FieldPost(models.Model):
    post_name = models.CharField(max_length=100)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    post_capacity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    expiry_date = models.CharField(max_length=100)

    def __str__(self):
        return self.post_name