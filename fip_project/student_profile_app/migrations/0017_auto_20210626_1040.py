# Generated by Django 3.2 on 2021-06-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile_app', '0016_studentprofile_field_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='academic_supervisor_marks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='field_supervisor_marks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='report_marks',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
