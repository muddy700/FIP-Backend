# Generated by Django 3.2 on 2021-04-26 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('field_post_app', '0008_rename_post_name_fieldpost_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fieldapplication',
            old_name='field_application_post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='fieldapplication',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='fieldpost',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='fieldpostprofession',
            old_name='field_profession_post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='fieldpostprofession',
            old_name='profession_id',
            new_name='profession',
        ),
    ]
