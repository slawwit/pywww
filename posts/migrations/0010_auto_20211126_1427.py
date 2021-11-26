# Generated by Django 3.2.9 on 2021-11-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20211124_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Treść'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Opublikowany'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sponsored',
            field=models.BooleanField(default=False, verbose_name='Sponsorowany'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Tytuł'),
        ),
    ]
