# Generated by Django 4.2.5 on 2023-09-20 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_location_meetup_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='Location',
        ),
    ]