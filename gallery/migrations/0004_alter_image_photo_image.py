# Generated by Django 3.2.6 on 2021-09-07 08:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20210903_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='photo_image'),
        ),
    ]
