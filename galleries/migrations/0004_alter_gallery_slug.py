# Generated by Django 3.2.9 on 2021-12-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_photo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]