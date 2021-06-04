# Generated by Django 3.2 on 2021-06-04 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv_app', '0002_personalinformation_cv_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinformation',
            name='alumni',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cv_personal_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EducationInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('education_level', models.CharField(max_length=100)),
                ('start_year', models.CharField(max_length=20)),
                ('completion_year', models.CharField(max_length=20)),
                ('alumni', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cv_education_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
