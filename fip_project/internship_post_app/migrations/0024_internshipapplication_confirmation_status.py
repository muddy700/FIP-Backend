# Generated by Django 3.2 on 2021-05-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_post_app', '0023_auto_20210519_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipapplication',
            name='confirmation_status',
            field=models.CharField(default='test', max_length=100),
        ),
    ]