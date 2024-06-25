# Generated by Django 5.0.6 on 2024-06-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='distance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='route',
            name='travel_time',
            field=models.FloatField(default=0.0),
        ),
    ]
