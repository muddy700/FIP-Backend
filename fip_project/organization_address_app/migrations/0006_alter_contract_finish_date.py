# Generated by Django 3.2 on 2021-05-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization_address_app', '0005_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='finish_date',
            field=models.DateField(),
        ),
    ]