from django.contrib import admin
from .models import (InternshipPost, 
InternshipApplication, InternshipApplicationStatus,
ApplicantLevel, InterviewSchedule)

admin.site.register(InternshipPost)
admin.site.register(InternshipApplicationStatus)
admin.site.register(InternshipApplication)
admin.site.register(InterviewSchedule)
admin.site.register(ApplicantLevel)
