from django.contrib import admin
from .models import InternshipPost, InternshipApplication, InternshipPostProfession

admin.site.register(InternshipPost)
admin.site.register(InternshipPostProfession)
admin.site.register(InternshipApplication)
