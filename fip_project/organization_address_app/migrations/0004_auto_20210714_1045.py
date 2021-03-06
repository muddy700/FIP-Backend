# Generated by Django 3.2 on 2021-07-14 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization_address_app', '0003_rename_notifications_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_opened',
        ),
        migrations.CreateModel(
            name='NotificationView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_notification', to='organization_address_app.notification')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_organization', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
