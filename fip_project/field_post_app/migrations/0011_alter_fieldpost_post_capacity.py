# Generated by Django 3.2 on 2021-06-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('field_post_app', '0010_auto_20210612_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldpost',
            name='post_capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]