from django.db import models

class Designation(models.Model):
    designation_name = models.CharField(max_length=100)

    def __str__(self):
        return self.designation_name