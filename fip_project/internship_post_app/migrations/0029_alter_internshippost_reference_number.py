# Generated by Django 3.2 on 2021-05-31 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_post_app', '0028_internshippost_reporting_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshippost',
            name='reference_number',
            field=models.CharField(default='FIP/2021/P000', max_length=100, unique=True),
        ),
    ]
