# Generated by Django 3.2.9 on 2021-11-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts/images/%Y/%m/%d/'),
        ),
    ]