from django.contrib import admin
from .models import StudentProfile, StudentProfession, FieldReport

admin.site.register(StudentProfile)
admin.site.register(FieldReport)
admin.site.register(StudentProfession)
