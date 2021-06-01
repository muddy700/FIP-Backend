from django.contrib import admin
from .models import OrganizationProfile, Contract, Rating

admin.site.register(OrganizationProfile)
admin.site.register(Rating)
admin.site.register(Contract)