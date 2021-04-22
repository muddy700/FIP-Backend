from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_hod = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name