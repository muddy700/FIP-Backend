# Generated by Django 3.2 on 2021-05-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_post_app', '0012_auto_20210518_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipapplication',
            name='oral_marks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internshipapplication',
            name='practical_marks',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
