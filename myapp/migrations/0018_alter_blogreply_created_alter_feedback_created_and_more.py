# Generated by Django 4.1.5 on 2023-04-04 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_blogreply_created_alter_feedback_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogreply',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 22, 3, 23, 244530)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 22, 3, 23, 244530)),
        ),
        migrations.AlterField(
            model_name='milanagent',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 22, 3, 23, 244530)),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 22, 3, 23, 244530)),
        ),
    ]
