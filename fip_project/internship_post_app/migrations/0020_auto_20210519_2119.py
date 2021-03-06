# Generated by Django 3.2 on 2021-05-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship_post_app', '0019_auto_20210519_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshippost',
            name='status',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='internshippost',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='internshippost',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='internshippost',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]
