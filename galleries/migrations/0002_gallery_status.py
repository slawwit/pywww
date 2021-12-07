# Generated by Django 3.2.9 on 2021-12-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='status',
            field=models.CharField(choices=[('hide', 'hide'), ('published', 'published'), ('new', 'new')], default='new', max_length=15),
        ),
    ]