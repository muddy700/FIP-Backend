# Generated by Django 3.2 on 2021-06-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_address_app', '0011_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationprofile',
            name='box_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='organizationprofile',
            name='organization_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]