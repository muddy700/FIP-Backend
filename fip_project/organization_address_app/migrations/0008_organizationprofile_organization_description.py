# Generated by Django 3.2 on 2021-05-27 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_address_app', '0007_rename_alumn_contract_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationprofile',
            name='organization_description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]