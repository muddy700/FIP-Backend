# Generated by Django 3.2 on 2021-05-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_address_app', '0008_organizationprofile_organization_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
