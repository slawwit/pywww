# Generated by Django 3.2.9 on 2021-11-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
    ]
