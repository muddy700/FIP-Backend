from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_status = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name