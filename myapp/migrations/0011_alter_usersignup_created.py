# Generated by Django 4.1.5 on 2023-04-03 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_usersignup_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 1, 58, 46, 553046)),
        ),
    ]
