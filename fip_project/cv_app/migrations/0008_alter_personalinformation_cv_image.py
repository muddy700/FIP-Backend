# Generated by Django 3.2 on 2021-07-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0007_alter_experienceinformation_is_current_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='cv_image',
            field=models.ImageField(blank=True, upload_to='cv_images/'),
        ),
    ]
