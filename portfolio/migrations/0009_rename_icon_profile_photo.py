# Generated by Django 4.2 on 2025-01-17 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_profile_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='icon',
            new_name='photo',
        ),
    ]
