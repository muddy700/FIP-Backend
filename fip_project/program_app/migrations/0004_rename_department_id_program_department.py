# Generated by Django 3.2 on 2021-04-25 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program_app', '0003_rename_program_department_program_department_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='department_id',
            new_name='department',
        ),
    ]
