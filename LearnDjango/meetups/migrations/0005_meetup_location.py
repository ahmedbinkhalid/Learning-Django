# Generated by Django 4.2.5 on 2023-09-20 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_remove_meetup_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='Location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
            preserve_default=False,
        ),
    ]