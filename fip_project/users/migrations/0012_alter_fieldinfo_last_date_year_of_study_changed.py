# Generated by Django 3.2 on 2021-08-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_fieldinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldinfo',
            name='last_date_year_of_study_changed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]