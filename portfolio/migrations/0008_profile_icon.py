# Generated by Django 4.2 on 2025-01-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_project_profile_profile_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
