# Generated by Django 2.2.13 on 2020-12-02 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_timer'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
