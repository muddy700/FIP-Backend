# Generated by Django 3.2 on 2021-04-24 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization_app', '0002_remove_organization_organization_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
