# Generated by Django 5.0.4 on 2024-06-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0021_alter_job_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_details',
            name='posted_on',
            field=models.DateField(max_length=255, null=True),
        ),
    ]
