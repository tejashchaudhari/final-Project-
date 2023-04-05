# Generated by Django 4.1.5 on 2023-04-04 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_comment_milanagent_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogreply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 18, 26, 29, 931717))),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 18, 26, 29, 931717)),
        ),
        migrations.AlterField(
            model_name='milanagent',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 18, 26, 29, 931717)),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 4, 18, 26, 29, 931717)),
        ),
    ]
