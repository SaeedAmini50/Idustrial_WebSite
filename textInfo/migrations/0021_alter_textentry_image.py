# Generated by Django 5.0.6 on 2025-04-07 20:13

import textInfo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textInfo', '0020_alter_textentry_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=textInfo.models.get_product_image_filepath, verbose_name='تصویر'),
        ),
    ]
