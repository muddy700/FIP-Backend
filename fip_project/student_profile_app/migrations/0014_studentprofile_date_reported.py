# Generated by Django 3.2 on 2021-06-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile_app', '0013_auto_20210624_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='date_reported',
            field=models.DateField(blank=True, null=True),
        ),
    ]
