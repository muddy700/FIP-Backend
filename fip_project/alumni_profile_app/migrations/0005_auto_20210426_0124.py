# Generated by Django 3.2 on 2021-04-25 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_profile_app', '0004_alter_alumniprofile_organization_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumniprofession',
            old_name='alumni_id',
            new_name='alumni',
        ),
        migrations.RenameField(
            model_name='alumniprofession',
            old_name='profession_id',
            new_name='profession',
        ),
        migrations.RenameField(
            model_name='alumniprofile',
            old_name='alumni_id',
            new_name='alumni',
        ),
        migrations.RenameField(
            model_name='alumniprofile',
            old_name='department_id',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='alumniprofile',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='alumniprofile',
            old_name='program_id',
            new_name='program',
        ),
    ]
