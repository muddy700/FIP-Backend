# Generated by Django 3.2 on 2021-05-30 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_profile_app', '0006_auto_20210505_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumniprofile',
            old_name='is_active',
            new_name='is_taken',
        ),
    ]