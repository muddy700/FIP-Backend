# Generated by Django 3.2 on 2021-05-10 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profession_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_body', models.CharField(max_length=500)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profession_app.profession')),
            ],
        ),
    ]