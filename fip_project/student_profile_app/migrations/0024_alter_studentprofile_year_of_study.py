# Generated by Django 3.2 on 2021-08-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile_app', '0023_alter_studentprofile_marks_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='year_of_study',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
