# Generated by Django 4.2.11 on 2024-03-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
