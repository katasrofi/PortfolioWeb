# Generated by Django 4.2 on 2025-01-11 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('social_links', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='images/')),
                ('url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('feedback', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('position', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('proficiency', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=60)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
            ],
        ),
    ]
