# Generated by Django 5.0 on 2023-12-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
                ('instructor', models.CharField(max_length=255)),
                ('capacity', models.IntegerField(default=30)),
                ('open_seats', models.IntegerField(default=30)),
            ],
        ),
    ]
