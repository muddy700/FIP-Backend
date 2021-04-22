# Generated by Django 3.2 on 2021-04-22 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profession_app', '0001_initial'),
        ('field_post_app', '0002_alter_fieldpost_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldPostProfession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_profession_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_profession_post_id', to='field_post_app.fieldpost')),
                ('profession_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profession_app.profession')),
            ],
        ),
        migrations.CreateModel(
            name='FieldApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_application_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_application_post_id', to='field_post_app.fieldpost')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_application_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
