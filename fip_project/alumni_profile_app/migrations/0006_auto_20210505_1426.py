# Generated by Django 3.2 on 2021-05-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_profile_app', '0005_auto_20210426_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumniprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='alumniprofile',
            name='profile_image',
        ),
    ]
