# Generated by Django 3.2 on 2021-04-25 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile_app', '0008_rename_department_id_studentprofile_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='academic_supervisor_id',
            new_name='academic_supervisor',
        ),
    ]
