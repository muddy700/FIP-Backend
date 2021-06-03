from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Project(models.Model):
    title = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=10, blank=True)
    sponsor = models.CharField(max_length=100, blank=True)
    report = models.FileField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    recommendation_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        
class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_member")

    def __str__(self):
        return f'{self.project.title } Member'