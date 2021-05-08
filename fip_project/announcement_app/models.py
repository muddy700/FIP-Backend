from django.db import models
from department_app.models import  Department
from designation.models import Designation

class Announcement(models.Model):
    source = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='sender')
    destination = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='receiver')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    closing_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title