# Generated by Django 3.2 on 2021-05-05 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization_address_app', '0003_auto_20210423_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='organizationprofile',
            name='profile_image',
        ),
    ]
