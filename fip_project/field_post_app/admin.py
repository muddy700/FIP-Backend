from django.contrib import admin
from .models import FieldPost, FieldApplication, FieldPostProfession, FieldPostProgram

admin.site.register(FieldPost)
admin.site.register(FieldPostProfession)
admin.site.register(FieldApplication)
admin.site.register(FieldPostProgram)
