from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    recommendation_status = models.BooleanField(default=False)
    project_report = models.FileField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())


    def __str__(self):
        return self.project_name
class ProjectMember(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    member_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_member_id")

    def __str__(self):
        return self.project_name