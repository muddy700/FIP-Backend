# Generated by Django 3.2 on 2021-05-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_post_app', '0026_alter_interviewschedule_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipapplication',
            name='has_reported',
            field=models.BooleanField(default=False),
        ),
    ]
