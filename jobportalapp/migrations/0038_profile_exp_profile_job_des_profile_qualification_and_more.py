# Generated by Django 5.0.4 on 2024-07-03 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0037_admin_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='exp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='job_des',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='qualification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Admin_profile',
        ),
    ]
