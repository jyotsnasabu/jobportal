# Generated by Django 5.0.4 on 2024-06-17 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0030_jobapplication_profile_visited_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usermember',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
