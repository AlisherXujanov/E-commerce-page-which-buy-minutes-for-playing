# Generated by Django 2.2.13 on 2020-12-02 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_timer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='minute',
            field=models.FloatField(choices=[(0.5, 'Advanced'), (1, 'Normal'), (2, 'Easy')], default=1, help_text='Easy-2-Min/ Normal-1-min/ Advanced-0,5min'),
        ),
    ]
