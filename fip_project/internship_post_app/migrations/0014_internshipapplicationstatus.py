# Generated by Django 3.2 on 2021-05-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_post_app', '0013_auto_20210518_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_text', models.CharField(max_length=100)),
            ],
        ),
    ]