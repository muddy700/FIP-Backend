from django.contrib import admin
from .models import Question, MultipleChoice, ApplicantScore, ApplicantAnswer

admin.site.register(MultipleChoice)
admin.site.register(ApplicantScore)
admin.site.register(Question)
admin.site.register(ApplicantAnswer)
