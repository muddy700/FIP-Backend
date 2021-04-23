# Generated by Django 3.2 on 2021-04-23 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_profile_app', '0002_auto_20210422_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='organization_id',
            field=models.OneToOneField(default=38, on_delete=django.db.models.deletion.CASCADE, related_name='organization_id', to='auth.user'),
            preserve_default=False,
        ),
    ]
