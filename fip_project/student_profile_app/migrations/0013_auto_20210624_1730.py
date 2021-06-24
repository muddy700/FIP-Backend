# Generated by Django 3.2 on 2021-06-24 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student_profile_app', '0012_fieldreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='has_reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='academic_supervisor',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.CASCADE, related_name='academic_supervisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='field_supervisor',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.CASCADE, related_name='field_supervisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='organization',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.CASCADE, related_name='organization_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
