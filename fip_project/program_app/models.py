from django.db import models
from department_app.models import  Department
class Program(models.Model):
    program_name = models.CharField(max_length=100)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.program_name