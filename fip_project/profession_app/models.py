from django.db import models

class Profession(models.Model):
    profession_name = models.CharField(max_length=100)

    def __str__(self):
        return self.profession_name