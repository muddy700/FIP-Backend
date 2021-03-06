# Generated by Django 3.2 on 2021-06-24 16:16

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile_app', '0015_alter_studentprofile_date_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='field_report',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='raw/'),
        ),
    ]
