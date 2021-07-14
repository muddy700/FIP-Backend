from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from profession_app.models import Profession

class OrganizationProfile(models.Model):
    organization_id = models.OneToOneField(User, on_delete=models.CASCADE)
    box_address = models.CharField(max_length=100, blank=True)
    organization_description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.organization_id.username } Profile'

class Contract(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employer")
    start_date = models.DateField(auto_now_add=True)
    finish_date = models.DateField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.alumni.username } Contract'

class Rating(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_rated")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_organization")
    value = models.IntegerField()

    def __str__(self):
        return f'{self.alumni.username } Rating'

class Invitations(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumni_invited")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inviting_organization")
    invitation_message = models.CharField(max_length=1000, blank= True)
    rejection_message = models.CharField(max_length=1000, blank=True)
    status = models.CharField(max_length=50, default='received' ) 
    has_reported = models.BooleanField(default=False)   
    has_released = models.BooleanField(default=False)   

    def __str__(self):
        return f'{self.alumni.username}  Invitation' 

class Notification(models.Model):
    title = models.CharField(max_length=100, blank= True)
    content = models.CharField(max_length=1000, blank= True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

class NotificationView(models.Model):
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="target_organization")
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name="viewed_notification")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.notification.title} View'