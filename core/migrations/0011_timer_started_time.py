# Generated by Django 2.2.13 on 2020-12-03 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201203_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='started_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
