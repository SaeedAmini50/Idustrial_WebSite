# Generated by Django 5.0.6 on 2025-04-07 01:56

import textInfo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textInfo', '0016_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='image',
            field=models.ImageField(blank=True, default=textInfo.models.get_default_product_image, null=True, upload_to=textInfo.models.get_product_image_filepath),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default=textInfo.models.get_default_product_image, null=True, upload_to=textInfo.models.get_product_image_filepath),
        ),
        migrations.AlterField(
            model_name='headerinfo',
            name='logo',
            field=models.ImageField(blank=True, default=textInfo.models.get_default_product_image, null=True, upload_to=textInfo.models.get_product_image_filepath),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, default=textInfo.models.get_default_product_image, null=True, upload_to=textInfo.models.get_product_image_filepath),
        ),
        migrations.AlterField(
            model_name='textentry',
            name='image',
            field=models.ImageField(blank=True, default=textInfo.models.get_default_product_image, null=True, upload_to=textInfo.models.get_product_image_filepath),
        ),
        migrations.AlterField(
            model_name='textentry',
            name='select_option',
            field=models.CharField(choices=[('1', 'نوشته خیلی بزرگ '), ('2', 'نوشته بزرگ'), ('3', 'نوشته متوسط'), ('4', 'نوشته کوچک'), ('5', 'نوشته خیلی کوچک'), ('6', 'نوشته خیلی خیلی کوچک')], default='1', help_text='Select an option from 1 to 6', max_length=1),
        ),
    ]
