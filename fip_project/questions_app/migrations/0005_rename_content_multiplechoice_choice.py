# Generated by Django 3.2 on 2021-05-10 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0004_rename_choice_multiplechoice_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='content',
            new_name='choice',
        ),
    ]