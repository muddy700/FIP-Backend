# Generated by Django 3.2 on 2021-05-10 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0003_rename_content_multiplechoice_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='choice',
            new_name='content',
        ),
    ]
