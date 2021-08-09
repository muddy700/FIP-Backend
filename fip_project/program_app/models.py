from django.db import models
from department_app.models import  Department
class Program(models.Model):
    program_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    program_duration_years = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.program_name