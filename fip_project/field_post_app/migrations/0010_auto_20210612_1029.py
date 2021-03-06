# Generated by Django 3.2 on 2021-06-12 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profession_app', '0001_initial'),
        ('field_post_app', '0009_auto_20210426_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldpost',
            name='post_title',
        ),
        migrations.AddField(
            model_name='fieldpost',
            name='post_descrption',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='fieldpostprofession',
            name='profession_capacity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fieldpost',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fieldpost',
            name='post_capacity',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='FieldPostProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_capacity', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_program_post_id', to='field_post_app.fieldpost')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profession_app.profession')),
            ],
        ),
    ]
