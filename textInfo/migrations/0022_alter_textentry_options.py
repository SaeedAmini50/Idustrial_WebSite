# Generated by Django 5.0.6 on 2025-04-07 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textInfo', '0021_alter_textentry_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textentry',
            options={'ordering': ['unique_id'], 'verbose_name': 'متن', 'verbose_name_plural': 'متن\u200cها'},
        ),
    ]
