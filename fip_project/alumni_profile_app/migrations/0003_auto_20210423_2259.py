# Generated by Django 3.2 on 2021-04-23 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni_profile_app', '0002_alumniprofession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumniprofile',
            name='profession_id',
        ),
        migrations.AddField(
            model_name='alumniprofile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alumniprofile',
            name='organization_id',
            field=models.OneToOneField(default=38, on_delete=django.db.models.deletion.CASCADE, related_name='alumni_organization_id', to='auth.user'),
            preserve_default=False,
        ),
    ]
