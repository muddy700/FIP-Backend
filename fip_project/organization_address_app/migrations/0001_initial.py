# Generated by Django 3.2 on 2021-04-22 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_phone_number', models.CharField(max_length=100)),
                ('organization_email', models.CharField(max_length=100)),
                ('organization_box_address', models.CharField(max_length=100)),
                ('organization_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organization_app.organization')),
            ],
        ),
    ]