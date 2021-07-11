from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Certificate(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    authority = models.CharField(max_length=100, blank=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return f'{self.alumni.username}  Certificate'
