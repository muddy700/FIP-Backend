from django.contrib import admin
from .models import Project, ProjectMember

admin.site.register(ProjectMember)
admin.site.register(Project)
# Register your models here.
