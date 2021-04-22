from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Certificate(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.certificate_name
