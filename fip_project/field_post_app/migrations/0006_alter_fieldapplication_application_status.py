# Generated by Django 3.2 on 2021-04-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('field_post_app', '0005_fieldapplication_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldapplication',
            name='application_status',
            field=models.BooleanField(default='pending'),
        ),
    ]
