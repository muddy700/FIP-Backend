# Generated by Django 3.2 on 2021-07-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement_app', '0002_announcement_closing_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='closing_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]