# Generated by Django 3.2 on 2021-04-23 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni_profile_app', '0003_auto_20210423_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniprofile',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumni_organization_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
