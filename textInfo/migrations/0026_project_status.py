# Generated by Django 5.0.6 on 2025-04-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textInfo', '0025_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('in_progress', 'در حال اجرا'), ('completed', 'تکمیل شده'), ('planned', 'برنامه\u200cریزی شده')], default='in_progress', max_length=20, verbose_name='وضعیت پروژه'),
        ),
    ]
