# Generated by Django 3.2 on 2021-05-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_post_app', '0029_alter_internshippost_reference_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipapplication',
            name='has_released',
            field=models.BooleanField(default=False),
        ),
    ]
