# Generated by Django 3.2.13 on 2022-12-21 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarmhistory',
            name='is_success',
        ),
        migrations.RemoveField(
            model_name='alarmhistory',
            name='traceback',
        ),
    ]
