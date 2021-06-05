from django.contrib import admin
from .models import PersonalInformation, EducationInformation, ExperienceInformation

admin.site.register(ExperienceInformation)
admin.site.register(PersonalInformation)
admin.site.register(EducationInformation)
