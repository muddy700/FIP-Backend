# Generated by Django 3.2 on 2021-06-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0006_auto_20210605_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experienceinformation',
            name='is_current_job',
            field=models.BooleanField(default=False),
        ),
    ]