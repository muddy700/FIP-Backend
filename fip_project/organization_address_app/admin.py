from django.contrib import admin
from .models import Invitations, OrganizationProfile, Contract, Rating, Notification, NotificationView

admin.site.register(OrganizationProfile)
admin.site.register(Rating)
admin.site.register(Contract)
admin.site.register(Notification)
admin.site.register(Invitations)
admin.site.register(NotificationView)