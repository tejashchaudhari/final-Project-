# Generated by Django 4.1.5 on 2023-03-19 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 19, 11, 37, 29, 474062)),
        ),
    ]
